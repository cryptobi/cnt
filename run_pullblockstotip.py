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
Fetch blocks starting with from_block_id all the way to the chain tip.
"""

parser = argparse.ArgumentParser(description='Fetch blocks starting from a block hash until the chain tip.')
parser.add_argument('-f', '--format', metavar='<Output Format>', nargs='?', default='JSON', choices=["JSON", "YAML"],
                    type=str, help='Output format. Valid choices: JSON, YAML. Default: JSON')
parser.add_argument('host', metavar='<Host:Port>', type=str, help='Host:port to attempt to connect to.')
parser.add_argument('from_block_id', metavar='<initial_block_hash>', type=str, help='Initial block hash')
args = parser.parse_args()

ret = peer_funcs.pull_blocks_to_tip(args.host, args.from_block_id)

if args.format == "JSON":
    print(ret)
elif args.format == "YAML":
    print(yaml.dump(ret))
