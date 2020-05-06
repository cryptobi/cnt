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
Attempts to retrieve a list of peers from a remote host.
Prints out JSON or YAML 
Default output format: JSON
"""

import json
import funcs
import peer_funcs
import argparse

# Program defaults  ---------------------

output_format = "JSON"

# Begin ---------------------

parser = argparse.ArgumentParser(description='Attempt to fetch more peers from another network peer like a running node does in normal operation.')
parser.add_argument('-f', '--format', metavar='<Output Format>', nargs='?', default='JSON', choices=["JSON", "YAML", "CLI"], type=str, help='Output format. Valid choices: JSON, YAML, CLI. Default: JSON')
parser.add_argument('-s', '--source', metavar='<Data Source>', nargs='?', default='netstat', type=str, help='Data source. Valid choices: netstat, stdin or log file path. Default: netstat')
parser.add_argument('host', metavar='<Host:Port>', type=str, help='Host:port to attempt to fetch peers from.')
args = parser.parse_args()

peers = peer_funcs.get_peers_from_host(args.host)

if args.format == "JSON":
    print(peer_funcs.peers_to_config_json(peers["peers"]))
elif args.format == "YAML":
    print(peer_funcs.peers_to_config_yaml(peers["peers"]))
else:
    print(peer_funcs.peers_to_cli(peers["peers"]))
