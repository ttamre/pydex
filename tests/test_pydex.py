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

File: test_riot_client.py
Description: Unit test for riot_client.py
"""

import requests
import unittest
from client import Pydex


class TestPydex(unittest.TestCase):
    def setUp(self):
        self.client = Pydex()

    def test_init(self):
        assert self.client.host == "https://pokeapi.co/api/v2/pokemon/"
        assert self.client.cache == {}

    def test_valid_search_pokemon(self):
        pikachu = self.client.search_pokemon("pikachu")
        assert pikachu["name"] == "pikachu"
        assert pikachu["id"] == 25
        assert self.client.search_cache("pikachu") == pikachu

    def test_invalid_search_pokemon(self):
        try:
            self.client.search_pokemon("invalid_pokemon")
        except requests.HTTPError:
            return True

    def test_valid_search_cache(self):
        self.client.search_pokemon("pikachu")
        assert "pikachu" in list(self.client.cache.keys())
        
        pikachu = self.client.search_cache("pikachu")

        assert pikachu["name"] == "pikachu"
        assert pikachu["id"] == 25
        assert self.client.search_cache("pikachu") == pikachu

    def test_invalid_search_cache(self):
        assert "invalid_pokemon" not in list(self.client.cache.keys())
        invalid_pokemon = self.client.search_cache("invalid_pokemon")
        assert not invalid_pokemon

    def test_single_parse_types(self):
        ptype = [
            {
                "slot": 2,
                "type": {
                    "name": "flying",
                    "url": "https://pokeapi.co/api/v2/type/3/"
                }
            }
        ]
        assert self.client.parse_types(ptype) == "flying"

    def test_double_parse_types(self):
        ptype = [
            {
                "slot": 1,
                "type": {
                    "name": "fire",
                    "url": "https://pokeapi.co/api/v2/type/1/"
                }
            },
            {
                "slot": 2,
                "type": {
                    "name": "flying",
                    "url": "https://pokeapi.co/api/v2/type/3/"
                }
            }
        ]
        assert self.client.parse_types(ptype) == "fire flying"

    def test_invalid_parse_types(self):
        ptype = [
            {
                "slot": 1,
                "type": {
                    "name": "fire",
                    "url": "https://pokeapi.co/api/v2/type/1/"
                }
            },
            {
                "slot": 2,
                "type": {
                    "name": "flying",
                    "url": "https://pokeapi.co/api/v2/type/3/"
                }
            },
            {
                "slot": 3,
                "type": {
                    "name": "water",
                    "url": "https://pokeapi.co/api/v2/type/2/"
                }
            }
        ]
        assert self.client.parse_types(ptype) == None

    def tearDown(self):
        del self.client