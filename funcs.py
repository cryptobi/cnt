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

import datetime
import sys

"""
General purpose functions
"""


def zlog(msg, output_console=True, is_error=False):
    """
    Prints timestamped messages to stdout
    :param msg: Messsage
    :param output_console: Print to console? Boolean. Default True.
    :param is_error: If true, prints to stderr.
    :return: Number of characters written.
    """
    xfile = sys.stdout
    if is_error:
        xfile = sys.stderr

    if output_console:
        print("{}: {}".format(datetime.datetime.now(), msg), file=xfile)
    else:
        # log to file in the future?
        pass

    return len(msg)


def zlog_error(msg, output_console=True):
    """
    Utility function to call zlog with file=stderr.
    :param msg: Messsage
    :param output_console: Print to console? Boolean. Default True.
    :return: Number of characters written.
    """
    return zlog(msg, output_console, True)
