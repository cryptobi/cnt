"""
    This file is part of crypto.bi CNT - Cardano Network Tools

    crypto.bi CNT is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    crypto.bi CNT is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with crypto.bi CNT. If not, see <https://www.gnu.org/licenses/>.
"""

# crypto.bi CNT - Cardano Network Tools
# Author: Jose Fonseca https://zefonseca.com/
# License: GPL v3
# Development time sponsored by:
# https://crypto.bi/ - Cryptocurrency content for everyone


import subprocess
import re
import grpc
import json
import node_pb2
import node_pb2_grpc
from google.protobuf import json_format
import ipaddress
import crypto_funcs
import yaml
import random
import fileinput
import struct

# for now, assume port 3000
# TODO configurable port # filter
assume_port_nr = 3000
host_id_length = 24
message_length_limit = 100 * 1024 * 1024
request_timeout_ms = 1000
request_retries = 0


def list_hosts_from_stdin():
    """
    Reads host:port list from stdin.
    Input format:
    host1:port1
    host2:port2
    ....
    """
    hosts = []
    for line in fileinput.input():
        hosts.append(line)

    return hosts


def list_hosts_from_file(filename):
    """
    Lists host:port by reading one entry per line from filename.
    File format:
    host1:port1
    host2:port2
    ....
    :param: filename : File to read from.
    """
    hosts = []

    with open(filename, "r") as file:
        count = 0
        line = file.readline().strip()
        while line:
            hosts.append(line)
            line = file.readline().strip()

    return hosts


def list_local_established_connections(limit=20):
    """
    Lists active connections calling netstat.
    :param: limit : Limit the connection test to 20 hosts. Will only test `limit` number of hosts. Set limit <= 0 to remove limit.
    Only works if you have a local jormungandr node running.
    Currently assumes assume_port_nr TCP port number.
    """
    hosts = []
    r = subprocess.run(['netstat', '-tan'], stdout=subprocess.PIPE).stdout.decode('utf-8')

    lins = re.split("[\\n]+", r)

    count = 0
    for line in lins:
        pieces = re.split("\\s+", line)

        if len(pieces) == 6:
            if pieces[5] == "ESTABLISHED":
                count += 1
                ipp = pieces[4]
                [ip, port] = ipp.split(":")
                port = int(port)

                if port == assume_port_nr:
                    hosts.append(ipp)

        if limit > 0:
            if count >= limit:
                break

    return hosts


def rand_host_id():
    return crypto_funcs.rand_hex_str(host_id_length)


def zero_host_id():
    return '0' * host_id_length


def serialize_string(host_id_str):
    """
        A primitive implementation of the serde serialization format used in jormungandr
        Format : str length encoded in 64 bits small endian, followed by ID bytes
        :param: host_id_str: A network node ID string
        :return: Serialized bytes.
    """

    return bytes(
        list(struct.unpack('8B', struct.pack('Q', int(len(host_id_str) / 2)))) + list(bytearray.fromhex(host_id_str))
    )


def get_metadata():
    """
    Generate standard metadata for gRPC requests.
    :return: metadata pairs suitable for gRPC requests
    """
    hid = rand_host_id()
    md = [
        ("node-id-bin", serialize_string(hid)),
    ]
    return md


def get_channel(host):
    """Build channel with standard config."""

    conn = None
    enable_retries = request_retries
    max_message_length = message_length_limit
    max_receive_message_length = message_length_limit
    timeouts_ms = request_timeout_ms

    options = [
        ('grpc.lb_policy_name', 'pick_first'),
        ('grpc.enable_retries', enable_retries),
        ('grpc.server_handshake_timeout_ms', timeouts_ms),
        ('grpc.keepalive_timeout_ms', timeouts_ms),
        ('grpc.max_message_length', max_message_length),
        ('grpc.max_receive_message_length', max_receive_message_length)
    ]

    try:
        conn = grpc.insecure_channel(host, options)
    except:
        pass

    return conn


def get_peers_from_host(host):
    """
    :param host: IP:PORT string
    :return: Json { "peers" : [v4 : { ip: , port: }] } on success.
             None on failure.
    """
    conn = get_channel(host)
    jsx = None

    if conn:
        stub = node_pb2_grpc.NodeStub(conn)
        response = stub.Peers(node_pb2.PeersRequest())
        jsx = json_format.MessageToJson(response)
        conn.close()

    json_o = None

    if jsx:
        json_o = json.loads(jsx)
        if "peers" in json_o:
            for i in range(len(json_o["peers"])):
                ipnum = int(json_o["peers"][i]["v4"]["ip"])
                ipx = ipaddress.ip_address(ipnum)
                json_o["peers"][i]["v4"]["ip"] = str(ipx)

    return json_o


def peers_to_host_list(peers):
    """
    Converts peers as returned from get_peers_from_host into host:port list
    :param peers:
    :return:
    """
    ret = []

    for peer in peers["peers"]:
        host = str(peer["v4"]["ip"])
        port = str(peer["v4"]["port"])
        ipp = ":".join([host, port])
        ret.append(ipp)

    return ret


def test_peers(peers, t_callback=None, pf_callback=None, zf_callback=None, gh_callback=None):
    """
    Tests an iterable of peers  (strings with host:port format) for peer listing.
    This function can be used to build a list of good peers for seeding nodes.
    :param peers: Iterable of peers. E.g. ["1.1.1.1:3000", "2.2.2.2:3100",]
    :param t_callback: Function t_callback(host) to call when a new host begins being tested.
    :param pf_callback: Function pf_callback(new_peers, host) to call with iterable of new peers received from host.
    :param zf_callback: Function zf_callback(host) to call when zero new peers are received from host.
    :param gh_callback: Function gh_callback(host) to call when a new host is retrieved.
    :return: Set of peers which return other peers when queried.
    """

    good_hosts = set()

    for host in peers:

        if t_callback:
            t_callback(host)

        jsx = None

        try:
            jsx = get_peers_from_host(host)
        except:
            if zf_callback:
                zf_callback(host)
            pass

        if jsx:

            new_hosts = jsx["peers"]
            len_new_hosts = len(new_hosts)

            if len_new_hosts > 0:
                # the tested host returns new peers
                # mark good
                good_hosts.add(host)
                if gh_callback:
                    gh_callback(host)

            if pf_callback:
                pf_callback(new_hosts, host)

    return good_hosts


def peers_to_config_format(peers):
    """
    Transforms peers from PeersResponse format to jormungandr config format.
    e.g. [{ "address": "/ip4/13.56.0.226/tcp/3000", "id": "7ddf203c86a012e8863ef19d96aabba23d2445c492d86267" }, ... ]
    :param peers: Iterable of PeersResponse format peers.
    :return: Iterable of peers in jormungandr format.
    """
    ret = []
    for peer in peers:
        host = peer["v4"]["ip"]
        port = peer["v4"]["port"]
        idx = crypto_funcs.rand_hex_str(24)
        _peer = {
            "address": "/ip4/{}/tcp/{}".format(host, port),
            "id": idx
        }
        ret.append(_peer)
    return ret


def peers_to_config_json(peers):
    jsx = peers_to_config_format(peers)
    return json.dumps(jsx, indent=4)


def peers_to_config_yaml(peers):
    jsx = peers_to_config_format(peers)
    return yaml.dump(jsx)


def peers_to_cli(peers):
    """
    Generates a string for use bootstrapping jormungandr from the CLI.
    :param peers: Iterable of peers as returned by a PeersRequest
    :return: str with CLI peer
    """
    ret1 = "--trusted-peer "
    jsx = peers_to_config_format(peers)
    peerstrs = ["{}@{}".format(p["address"], p["id"]) for p in jsx]
    peer = random.choice(peerstrs)
    return "jormungandr {} {} --config <your config.yaml> --genesis-block-hash <genesis-hash>".format(ret1, peer)


def hosts_to_config_format(hosts):
    """
    Transforms a list of hosts ["host:port", "host2:port2"]
    :param hosts: Iterable of host:port strings
    :return: Iterable of peers in jormungandr format.
    """
    ret = []
    for peer in hosts:
        host, port = peer.split(":")
        idx = crypto_funcs.rand_hex_str(24)
        _peer = {
            "address": "/ip4/{}/tcp/{}".format(host, port),
            "id": idx
        }
        ret.append(_peer)
    return ret


def hosts_to_config_json(hosts):
    jsx = hosts_to_config_format(hosts)
    return json.dumps(jsx, indent=4)


def hosts_to_config_yaml(hosts):
    jsx = hosts_to_config_format(hosts)
    return yaml.dump(jsx)


def hosts_to_cli(hosts):
    """
    Generates a string for use bootstrapping jormungandr from the CLI.
    :param hosts: Iterable of host:port strings
    :return: str with CLI peer
    """
    ret1 = "--trusted-peer "
    jsx = peers_to_config_format(hosts)
    peerstrs = ["{}@{}".format(p["address"], p["id"]) for p in jsx]
    peer = random.choice(peerstrs)
    return "jormungandr {} {} --config <your config.yaml> --genesis-block-hash <genesis-hash>".format(ret1, peer)


def handshake(host):
    """
    :param host: IP:PORT string
    :return: json format reply from Handshake message
    """
    conn = get_channel(host)
    jsx = None

    if conn:
        stub = node_pb2_grpc.NodeStub(conn)
        response = stub.Handshake(node_pb2.HandshakeRequest())
        jsx = json_format.MessageToJson(response)
        conn.close()

    json_o = None

    if jsx:
        json_o = json.loads(jsx)

    return json_o


def tip(host):
    """
    :param host: IP:PORT string
    :return: json format reply from Tip message
    """
    conn = get_channel(host)
    jsx = None

    if conn:
        stub = node_pb2_grpc.NodeStub(conn)
        response = stub.Tip(node_pb2.TipRequest())
        jsx = json_format.MessageToJson(response)
        conn.close()

    json_o = None

    if jsx:
        json_o = json.loads(jsx)

    return json_o


def get_blocks(host, block_ids):
    """
    :param host: IP:PORT string
    :param block_ids: comma separated block ID's
    :return: Array of raw block contents (byte arrays) for each queried block.
    """
    conn = get_channel(host)
    ret = []

    if conn:
        stub = node_pb2_grpc.NodeStub(conn)
        bids = [bytes(bytearray.fromhex(b.strip())) for b in block_ids.split(",")]

        req = node_pb2.BlockIds(ids=bids)

        response = stub.GetBlocks(req)
        for block in response:
            ret.append(block.content)

        conn.close()

    return ret


def get_headers(host, block_ids):
    """
    :param host: IP:PORT string
    :param block_ids: comma separated block ID's
    :return: Array of raw block header contents (byte arrays) for each queried block.
    """
    conn = get_channel(host)
    ret = []

    if conn:
        stub = node_pb2_grpc.NodeStub(conn)
        bids = [bytes(bytearray.fromhex(b.strip())) for b in block_ids.split(",")]

        req = node_pb2.BlockIds(ids=bids)

        response = stub.GetHeaders(req)
        for block in response:
            ret.append(block.content)

        conn.close()

    return ret


def get_fragments(host, fragment_ids):
    """
    :param host: IP:PORT string
    :param fragment_ids: comma separated fragment ID's
    :return: Array of raw fragment contents (byte arrays) for each queried ID.
    """
    conn = get_channel(host)
    ret = []

    if conn:
        stub = node_pb2_grpc.NodeStub(conn)
        bids = [bytes(bytearray.fromhex(b.strip())) for b in fragment_ids.split(",")]

        req = node_pb2.FragmentIds(ids=bids)

        response = stub.GetFragments(req)
        for fragment in response:
            ret.append(fragment.content)

        conn.close()

    return ret


def pull_headers(host, from_block_id, to_block_id):
    """
    Pulls headers for a range of blocks starting with from_block_id until to_block_id
    :param host: IP:PORT string
    :param from_block_id: Initial block ID
    :param to_block_id: Final block ID
    :return: Array of raw block header contents (byte arrays) for each queried block.
    """
    conn = get_channel(host)
    ret = []

    if conn:
        stub = node_pb2_grpc.NodeStub(conn)
        from_id = bytes(bytearray.fromhex(from_block_id.strip()))
        to_id = bytes(bytearray.fromhex(to_block_id.strip()))
        _pr1 = {"from": [from_id], "to": to_id}
        req = node_pb2.PullHeadersRequest(**_pr1)
        response = stub.PullHeaders(req)

        for header in response:
            ret.append(header.content)

        conn.close()

    return ret


def pull_blocks_to_tip_iterator(host, from_id):
    """
    Pull blocks from from_id until tip of chain.
    :param host: IP:PORT string
    :param from_id: Pull blocks starting from from_id
    :return: An array containing the connection and a Block iterator.
    """
    conn = get_channel(host)
    ret = []

    if conn:
        stub = node_pb2_grpc.NodeStub(conn)
        from_bid = bytes(bytearray.fromhex(from_id.strip()))
        _pr1 = {"from": [from_bid]}

        req = node_pb2.PullBlocksToTipRequest(**_pr1)

        return [conn, stub.PullBlocksToTip(req)]


def pull_blocks_to_tip(host, from_id):
    """
    Pull blocks from from_id until tip of chain.
    :param host: IP:PORT string
    :param from_id: Pull blocks starting from from_id
    :return: Array of raw block contents (byte arrays) for each returned block.
    """
    ret = []
    conn, response = pull_blocks_to_tip_iterator(host, from_id)
    for block in response:
        ret.append(block.content)

    conn.close()
    return ret


def push_headers(host, header_str):
    """
    Pushes raw headers to the remote host when a remote header is reported missing in a BlockSubscription
    From the original jormungander documentation:
        // Sends headers of blocks to the service in response to a `missing`
        // item received from the BlockSubscription response stream.
        // The headers are streamed the in chronological order of the chain.
    :param host: IP:PORT string
    :param header_str: Raw hex encoded string of header bytes.
    :return: A (likely empty) PushHeaderResponse
    """
    conn = get_channel(host)
    jsx = None

    def header_iter():
        """
            Simple header iterator.
            This is just a closure over a single header in args.header.
            Create your own implementation for more advanced usage.
        """
        for h in [bytes(bytearray.fromhex(header_str.strip())) ]:
            yield node_pb2.Header(content=h)

    if conn:
        stub = node_pb2_grpc.NodeStub(conn)
        header_iterator = header_iter()
        response = stub.PushHeaders(header_iterator)
        jsx = json_format.MessageToJson(response)
        conn.close()

    json_o = None

    if jsx:
        json_o = json.loads(jsx)

    return json_o


def upload_block(host, block_str):
    """
    Push a raw block to the remote host in response to a solicit request during a BlockSubscription session.
    From the original jormungander documentation:
        // Uploads blocks to the service in response to a `solicit` item
        // received from the BlockSubscription response stream.
    :param host: IP:PORT string
    :param block_str: Raw hex encoded string of block bytes.
    :return: Empty UploadBlocksResponse
    """
    conn = get_channel(host)
    jsx = None

    def block_iter():
        """
            Simple block iterator.
            This is just a closure over a single header in args.header.
        """
        for h in [bytes(bytearray.fromhex(block_str.strip())), ]:
            yield node_pb2.Block(content=h)

    if conn:
        stub = node_pb2_grpc.NodeStub(conn)
        block_iterator = block_iter()
        response = stub.UploadBlocks(block_iterator)
        jsx = json_format.MessageToJson(response)
        conn.close()

    json_o = None

    if jsx:
        json_o = json.loads(jsx)

    return json_o


def gossip_subscription(host, gossip_iterator):
    """
    Subscribe to receive peer gossip from host.
    Caller must close the connection after the iterator reaches EOF
    :param host: IP:PORT string
    :param gossip_iterator: Input Gossip iterator.
    :return: Returns an array of [connection, output Gossip iterator].
    """

    conn = get_channel(host)

    if conn:
        stub = node_pb2_grpc.NodeStub(conn)
        md = get_metadata()
        ret = stub.GossipSubscription(gossip_iterator, metadata=md)

        return [conn, ret]

    return None


def block_subscription(host, block_iter):
    """
    Subscribe to receive block messages from host.
    Caller must close the connection after the iterator reaches EOF
    :param host: IP:PORT string
    :param block_iter: Input block iterator.
    :return: Returns an array of [connection, output Block iterator].
    """

    conn = get_channel(host)

    if conn:
        stub = node_pb2_grpc.NodeStub(conn)
        md = get_metadata()
        return [conn, stub.BlockSubscription(block_iter, metadata=md)]

    return None


def fragment_subscription(host, fragment_iterator):
    """
    Subscribe to receive fragment messages from host.
    Caller must close the connection after the iterator reaches EOF
    :param host: IP:PORT string
    :param fragment_iterator: Input fragment iterator
    :return: Returns an array of [connection, output Fragment iterator].
    """

    conn = get_channel(host)

    if conn:
        stub = node_pb2_grpc.NodeStub(conn)
        md = get_metadata()
        return [conn, stub.FragmentSubscription(fragment_iterator, metadata=md)]

    return None
