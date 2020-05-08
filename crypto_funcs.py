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


import random


def rand_hex_bytes(length=24):
    """
    Generate a random byte string, `length` bytes long.
    :param length: String length in octets.
    :return: A random bytes string.
    """

    hashx = random.getrandbits(length * 8)
    return bytes(hashx)



def rand_hex_str(length=24):
    """
    Generate a random hex string, `length` characters long.
    :param length: String length in octets.
    :return: A random string.
    """
    
    hashx = random.getrandbits(length * 8)
    fstr = "{{:{}X}}".format(length)
    rstr = fstr.format(hashx).lower()
    for i in range((length*2) - len(rstr)):
        rstr = "{}0".format(rstr)
    return rstr
