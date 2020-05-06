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
import dao

# these tests will be expanded once the DAO has been implemented


class TestCNTDBConnection(unittest.TestCase):
    def test_get_connection(self):
        self.assertTrue("save" in dao.CNTDBConnection)


class TestRecentPeerDAO(unittest.TestCase):

    def test_save(self):
        self.assertTrue("save" in dao.RecentPeerDAO)

    def test_delete(self):
        self.assertTrue("delete" in dao.RecentPeerDAO)

    def test_delete_by_ip(self):
        self.assertTrue("delete_by_ip" in dao.RecentPeerDAO)

    def test_delete_all(self):
        self.assertTrue("delete_all" in dao.RecentPeerDAO)

    def test_list(self):
        self.assertTrue("list" in dao.RecentPeerDAO)
