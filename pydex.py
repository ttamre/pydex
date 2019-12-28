#!/usr/bin/env python3

"""
pydex - a python pokedex application

Copyright (C) 2019 Tem Tamre

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import json
import logging
import os
from bot import Bot


logging.basicConfig(level=logging.INFO)

license_text = """
pydex Copyright (C) 2019 Tem Tamre
    This program comes with ABSOLUTELY NO WARRANTY.
    This is free software, and you are welcome to redistribute it under certain conditions.
    For further information, please refer to the source at which you obtained this software.
"""

if __name__ == "__main__":
    logging.info(license_text)
    token = os.environ.get("PYDEX_BOT_TOKEN")
    
    if token:
        bot = Bot()
        bot.run()
    else:
        logging.critical("Bot token not found")