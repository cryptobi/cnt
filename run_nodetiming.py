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

import peer_funcs
import argparse
import timing_funcs
import time
import funcs
import random

"""

run_nodetiming.py is a network speed tool.

It continuously fetches peers from the network and time peer requests.

Example usage:

python3 run_nodetiming.py 127.0.0.1:3000 /disk5/jormungandr/local/peer_speed_data.csv

Output format: CSV
Columns: request_type,unix_timestamp,host,port,seconds

"""

# how many times to sample each message type
timing_sample_count = 3

parser = argparse.ArgumentParser(description='Fetch block headers from a remote peer.')
parser.add_argument('-f', '--format', metavar='<Output Format>', nargs='?', default='JSON', choices=["JSON", "YAML"],
                    type=str, help='Output format. Valid choices: JSON, YAML. Default: JSON')
parser.add_argument('host', metavar='<Host:Port>', type=str, help='Host:port to attempt to connect to.')
parser.add_argument('csv', metavar='<csv_filename>', type=str, help='CSV file name to write to.')
args = parser.parse_args()

host, port = args.host.split(":")
discovered_hosts = {args.host}
tested_hosts = set()
total_tested_count = 0


def gpfh_builder(remote_peer):
    global discovered_hosts

    def gpfh():
        global discovered_hosts
        try:
            funcs.zlog_error("Testing {} ...".format(remote_peer))
            new_peers = peer_funcs.get_peers_from_host(remote_peer)
            funcs.zlog_error("Received {} hosts from {}.".format(len(new_peers), remote_peer))
            host_list = peer_funcs.peers_to_host_list(new_peers)
            discovered_hosts.update(host_list)
        except:
            pass

    return gpfh


with open(args.csv, "a+") as csv_file:

    timing_funcs.time_print_func(gpfh_builder(args.host), "get_peers_from_host", host, port, csv_file, True)
    total_tested_count += 1

    if not len(discovered_hosts) > 1:
        funcs.zlog_error("ERROR: Zero hosts retrieved from {}. Aborting.".format(args.host))
        exit()


    def host_iterator():
        global discovered_hosts
        while True:
            yield random.sample(discovered_hosts, 1)[0]


    for host in host_iterator():
        hostx, portx = host.split(":")
        timing_funcs.time_print_func(gpfh_builder(host), "get_peers_from_host", hostx, portx, csv_file, True)
        total_tested_count += 1
        tested_hosts.add(host)
        tests_per_host = total_tested_count / len(tested_hosts)
        funcs.zlog_error("TOTAL {} HOSTS DISCOVERED, {} TESTS, {} HOSTS TESTED, {} TESTS PER HOST".format(
            len(discovered_hosts),
            total_tested_count,
            len(tested_hosts),
            tests_per_host
        ))
        time.sleep(1)
