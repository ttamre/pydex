"""
pydex - A pokedex discord boy
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

File:           client.py
Description:    pydex pokedex client

Author:  Tem Tamre
Contact: ttamre@ualberta.ca
Version: 1.0

https://pokeapi.co/docs/v2.html
"""

import json
import logging
import requests
from io import BytesIO
logging.basicConfig(level=logging.INFO)


class Pydex:
    def __init__(self):
        self.host = "https://pokeapi.co/api/v2/pokemon/"
        self.cache = {}

    def search_cache(self, query):
        return self.cache.get(query, None)

    def search_pokemon(self, query):
        url = self.host + query + '/'
        result = requests.get(url)

        if result.status_code == 200:
            # Add result to cache, then return it
            result = result.json()
            self.cache[result["name"]] = result

            return result
        
        raise requests.HTTPError(f"HTTP {result.status_code} response on search for {query}")

    def parse_types(self, ptype):
        if len(ptype) == 1:
            return ptype[0]["type"]["name"]
        elif len(ptype) == 2:
            return f'{ptype[0]["type"]["name"]} {ptype[1]["type"]["name"]}'
        else:
            logging.error(f"(Ignore in workflow build) Parsing error on type {json.dumps(ptype)}")
            return None

    def fetch_images(self, sprites):
        if not sprites:
            return None

        front_default_repsonse = requests.get(sprites.get("front_default"))
        front_default = BytesIO(front_default_repsonse.content)

        front_shiny_response = requests.get(sprites.get("front_shiny"))
        front_shiny = BytesIO(front_shiny_response.content)

        return [front_default, front_shiny]