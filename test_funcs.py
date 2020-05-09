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
import funcs
import crypto_funcs

msg = crypto_funcs.rand_hex_str(24)


class TestFuncs(unittest.TestCase):

    def test_zlog(self):
        # must return empty
        ret = funcs.zlog(msg, False)
        # this is a silly test
        # just make sure the function is there
        self.assertTrue(ret >= len(msg))
        self.assertTrue(hasattr(funcs,"zlog"))

