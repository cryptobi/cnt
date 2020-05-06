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


"""
Tests which hosts from local connections can return new peers.
Prints out JSON or YAML which could be used in a bootstrap peer list.
*** NOTE: Assumes jormungandr is running locally. ***

Default output format: JSON

"""

import json
import funcs
import peer_funcs
import argparse
import os

# Begin ---------------------

parser = argparse.ArgumentParser(description='Fetch and test peers for bootstrapping a Cardano node.')
parser.add_argument('--format', metavar='N', type=str, nargs='?', default='JSON', choices=["JSON", "YAML", "CLI"], help='Output format. Valid choices: JSON, YAML, CLI. Default: JSON')
parser.add_argument('--source', metavar='N', type=str, nargs='?', default='netstat', help='Data source. Valid choices: netstat, stdin or log file path. Default: netstat')
args = parser.parse_args()

hosts = []

if args.source == "netstat":
    hosts = peer_funcs.list_local_established_connections(50)
elif args.source == "netstat":
    hosts = peer_funcs.list_hosts_from_stdin()
else:
    if os.path.isfile(args.source):
        hosts = peer_funcs.list_hosts_from_file(args.source)
    else:
        funcs.zlog_error("ERROR: Invalid source provided. {} is neither netstat, stdin or a valid filename.".format(args.source))
        exit(1)

# tests each host retrieving a list of peers from it
peers = list(peer_funcs.test_peers(hosts))

if args.format == "JSON":
    print(peer_funcs.hosts_to_config_json(peers))
elif args.format == "YAML":
    print(peer_funcs.hosts_to_config_yaml(peers))
else:
    print(peer_funcs.hosts_to_cli(peers))
