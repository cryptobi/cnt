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
import peer
import crypto_funcs
import test_peer_funcs
import time
import random

peer_id = crypto_funcs.rand_hex_str(24)
[invalid_host, invalid_port] = test_peer_funcs.invalid_host_port.split(":")
timestamp = time.time()
table_id = random.randint(1, 223457823)


class TestPeer(unittest.TestCase):

    def test_init(self):
        # must return empty
        peer_o = peer.Peer(table_id, peer_id, invalid_host, invalid_port, timestamp)
        self.assertEquals(peer_o.ts, timestamp)
        self.assertEquals(peer_o.table_id, table_id)
        self.assertEquals(peer_o.peer_id, peer_id)
        self.assertEquals(peer_o.host, invalid_host)
        self.assertEquals(peer_o.port, invalid_port)

