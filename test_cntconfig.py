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
import cntconfig
import os
import json

thispath = os.path.dirname(os.path.realpath(__file__))
jsonpath = os.path.join(thispath, "json/test.json")


class TestCNTConfig(unittest.TestCase):

    def test_load_json_from_file(self):

        jsx = cntconfig.load_json_from_file(jsonpath)

        self.assertEqual(jsx["db"]["user"], "test_user")
        self.assertEqual(jsx["db"]["host"], "test_host")
        self.assertEqual(jsx["db"]["pass"], "test_pass")
        self.assertEqual(jsx["db"]["db"], "test_db_schema")

        for i in range(6):
            self.assertEqual(jsx["my_array"][i], i)


