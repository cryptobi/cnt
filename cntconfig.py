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


import json


def load_config_json():
    # TODO load config from default location
    # ~/.cardano-cnt/config.json
    pass


def load_json_from_file(filename):
    with open(filename, "r") as f:
        return json.load(f)


class CNTConfig:

    def __init__(self, db_user, db_pass, db_host, db_db):
        self.db_user = db_user
        self.db_pass = db_pass
        self.db_host = db_host
        self.db_db = db_db

    def load_from_file(self, filename):
        config_json = load_json_from_file(filename)
        self.db_user = config_json["db"]["user"]
        self.db_pass = config_json["db"]["pass"]
        self.db_host = config_json["db"]["host"]
        self.db_db = config_json["db"]["db"]
