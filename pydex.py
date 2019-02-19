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


File:           pydex.py
Description:    python pokedex application that uses the PokeAPI and the pokebase wrapper

Author:  Tem Tamre
Contact: ttamre@ualberta.ca
Version: 1.0
"""

import backend
from consolemenu import ConsoleMenu
from consolemenu.items import FunctionItem, SubmenuItem


def main():
    '''
    Create a GUI menu within the terminal to act as the main menu
        1) Search pokemon       - Search for a pokemon, return relevant data
        2) Search sprites       - Search for a pokemon and open their sprite
        3) List generations     - List all pokemon from that generation
        4) View search history  - View all searched pokemon
        5) Exit program         - Exit program
    '''

    main_menu = ConsoleMenu("POKEDEX: For all your pokemon-related inquiries")
    
    search_pokemon = FunctionItem("Search for a pokemon", backend.search_pokemon)
    search_spirits = FunctionItem("Search for a pokemon spirit", backend.search_sprites)
    list_gens = FunctionItem("List all pokemon from a given generation", backend.list_generations)
    view_history = FunctionItem("View your search history", backend.view_history)
    exit_program = FunctionItem("Exit program", exit(0))

    main_menu.append_item(search_pokemon)
    main_menu.append_item(search_spirits)
    main_menu.append_item(list_gens)
    main_menu.append_item(view_history)
    main_menu.append_item(exit_program)

    main_menu.show()


main()