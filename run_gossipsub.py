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
import funcs

"""
Starts a reactive Gossip subscription to a remote peer.
Since we do not spread peer info on this node, in practice it's a unidirectional subscription.
(We just listen to gossip on the network.)

To make it bidirectional, edit or create a new version of gossip_subscription which accepts a
custom iterator as source for gossip. 

This implementation meant as a reference only.
"""

parser = argparse.ArgumentParser(description='Subscribe to receive gossip from a remote peer.')
parser.add_argument('-f', '--format', metavar='<Output Format>', nargs='?', default='JSON', choices=["JSON", "YAML"],
                    type=str, help='Output format. Valid choices: JSON, YAML. Default: JSON')
parser.add_argument('host', metavar='<Host:Port>', type=str, help='Host:port to attempt to connect to.')
args = parser.parse_args()

gossip_iter = peer_funcs.gossip_subscription(args.host)

for gossip in gossip_iter:

    if args.format == "JSON":
        print(gossip)
    elif args.format == "YAML":
        print(yaml.dump(gossip))
