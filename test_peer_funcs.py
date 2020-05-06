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


import unittest
import peer_funcs

# also used in test_peer
invalid_host_port = "192.0.2.0:0000"


class TestPeerFuncs(unittest.TestCase):

    def test_test_peers(self):
        # must return empty
        peers = peer_funcs.test_peers([])
        self.assertTrue(len(peers) == 0)

    def test_get_peers_from_peer(self):
        # test IP + invalid port
        # must return None
        self.assertIsNone(peer_funcs.get_peers_from_host(invalid_host_port))

    def test_get_channel(self):
        # test IP + invalid port
        # must return None
        self.assertIsNone(peer_funcs.get_channel(invalid_host_port))

    def test_list_local_established_connections(self):
        self.assertTrue(len(peer_funcs.list_local_established_connections(0)) == 0)
