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


"""
Database routines.
"""

import mysql.connector
from peer import Peer


class CNTDBConnection:

    @staticmethod
    def get_connection(config):
        """
        Singleton or connection pool.
        :param: config: a ZeConfig object instance containing database credentials
        :return: mysql connection
        """
        if not CNTDBConnection.cnx:

            CNTDBConnection.cnx = mysql.connector.connect(
                user=config["db"]["user"],
                password=config["db"]["pass"],
                host=config["db"]["host"],
                database=config["db"]["db"]
            )

        return CNTDBConnection.cnx


class RecentPeerDAO:
    """
    DAO class for recent peers.
    """
    @staticmethod
    def save(conn, p: Peer):
        pass

    @staticmethod
    def delete(conn, recent_peers_id: int):
        pass

    @staticmethod
    def delete_by_ip(conn, recent_peers_id: int):
        pass

    @staticmethod
    def delete_all(conn):
        pass

    @staticmethod
    def list(conn):
        pass

