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

import yaml
import peer_funcs
import argparse

"""
Fetch block headers in a range from from_block_id to to_block_id
Sequential calls to this function allows client to rebuild chain
"""

parser = argparse.ArgumentParser(description='Fetch a range of block headers from a remote peer.')
parser.add_argument('-f', '--format', metavar='<Output Format>', nargs='?', default='JSON', choices=["JSON", "YAML"],
                    type=str, help='Output format. Valid choices: JSON, YAML. Default: JSON')
parser.add_argument('host', metavar='<Host:Port>', type=str, help='Host:port to attempt to connect to.')
parser.add_argument('from_block_id', metavar='<initial_block_hash>', type=str, help='Initial block hash')
parser.add_argument('to_block_id', metavar='<final_block_hash>', type=str, help='Final block hash')
args = parser.parse_args()

ret = peer_funcs.pull_headers(args.host, args.from_block_id, args.to_block_id)

if args.format == "JSON":
    print(ret)
elif args.format == "YAML":
    print(yaml.dump(ret))
