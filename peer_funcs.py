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

# for now, assume port 3000
# TODO configurable port # filter
assume_port_nr = 3000


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


def get_channel(host):
    """Build channel with standard config."""
    conn = None
    timeouts_ms = 1000
    options = [
        ('grpc.lb_policy_name', 'pick_first'),
        ('grpc.enable_retries', 0),
        ('grpc.server_handshake_timeout_ms', timeouts_ms),
        ('grpc.keepalive_timeout_ms', timeouts_ms)
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
