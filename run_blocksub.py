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
import time

"""
Starts a reactive Block subscription to a remote peer.
Since we do not produce blocks on this node, in practice it's a unidirectional subscription.
(We just listen to new blocks from the network.)

To make it bidirectional, edit or create a new version of block_subscription which accepts a
custom iterator as source for blocks. 

This implementation meant as a reference only.
"""

parser = argparse.ArgumentParser(description='Subscribe to receive blocks from a remote peer.')
parser.add_argument('-f', '--format', metavar='<Output Format>', nargs='?', default='JSON', choices=["JSON", "YAML"],
                    type=str, help='Output format. Valid choices: JSON, YAML. Default: JSON')
parser.add_argument('host', metavar='<Host:Port>', type=str, help='Host:port to attempt to connect to.')
args = parser.parse_args()


def my_block_iter():
    """
        Null iterator, since we won't be sending blocks.
    """
    for h in []:
        yield h


[conn, block_iter] = peer_funcs.block_subscription(args.host, my_block_iter())

for block in block_iter:

    if args.format == "JSON":
        print(block)
    elif args.format == "YAML":
        print(yaml.dump(block))


conn.close()
