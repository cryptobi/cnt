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
Push raw header to a remote peer
"""

parser = argparse.ArgumentParser(description='Push raw header to a remote peer.')
parser.add_argument('host', metavar='<Host:Port>', type=str, help='Host:port to attempt to connect to.')
parser.add_argument('header', metavar='<headerbytes>', type=str, help='Raw hex header bytes')
args = parser.parse_args()

ret = peer_funcs.push_headers(args.host, args.header)

if args.format == "JSON":
    print(ret)
elif args.format == "YAML":
    print(yaml.dump(ret))
