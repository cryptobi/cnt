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


import timeit
import time
import funcs


def time_func(func):
    """
    Time a function call.
    :param func: Function to call
    :return: Array of [unix_timestamp, function_timing_seconds]
    """
    timing = timeit.timeit(func, number=1)
    t0 = int(time.time())
    return [t0, timing]


def time_print_func(func, request_type, host, port, file, verbose=False):
    """
    :param func: Function to time
    :param request_type: Short string describing this operation.
    :param host: Network hostname
    :param port: Network TCP port
    :param file: Open CSV file to write to
    :param verbose: Print feedback to stderr?
    :return: void
    """
    [ts, timing] = time_func(func)
    strx = "{},{},{},{},{}".format(request_type, ts, host, port, timing)
    file.write("{}\n".format(strx))
    file.flush()
    if verbose:
        funcs.zlog_error(strx)
