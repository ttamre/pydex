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


File:           backend.py
Description:    backend for pydex.py

Author:  Tem Tamre
Contact: ttamre@ualberta.ca
Version: 1.0

https://pokeapi.co/
https://github.com/PokeAPI/pokebase

--------------------------------------------------

PLAN
        1) Search pokemon       - Search for a pokemon, return relevant data
        2) Search spirits       - Search for a pokemon and open their sprite
        3) List generations     - List all pokemon from that generation
        4) View search history  - View all searched pokemon
        5) Exit program         - Exit program

    Helper functions
        * search(txt)       - allows users to search by name or ID
        * name_to_id(name)  - gets the ID of a pokemon name
        * id_to_name(id)    - gets the name of a pokemon ID
    
    Constants
        * SEARCH_HISTORY <list>
"""

import os
import pokebase as pb


SEARCH_HISTORY = []


def search_pokemon():
    '''
    Search for a pokemon based on user input
    '''
    results = search()
    print(results)  # Should unpack all class variables
    SEARCH_HISTORY.append(results)


def search_sprites():
    '''
    Search for a pokemon's sprite based on user input
    '''
    results = search()
    sprite = pb.SpriteResource('pokemon', results.id_())
    os.startfile(sprite.path)
    SEARCH_HISTORY.append(results)


def list_generations():
    '''
    List all pokemon that belong to a given generation
    '''
    gen = input("Enter a pokemon generation: ")
    while not gen.isdigit() or gen not in range(1,8):
        gen = input("Enter a pokemon generation: ")

    # https://pokebase.readthedocs.io/en/latest/examples/index.html#getting-all-pokemon-names-from-a-generation
    gen_resource = pb.generation(gen)
    print("-" * 20, "\nGENERATION", gen)
    for pokemon in gen_resource.pokemon_species:
        print(pokemon.name.title())
    print("-" * 20)
    SEARCH_HISTORY.append(gen_resource)


def view_history():
    '''
    Print the search history of the current session
    '''
    for item in SEARCH_HISTORY:
        print(item.name)



def search():
    '''
    Asks the user for input and GETs that pokemon from the API
    User can input a pokemon name or ID number
    '''
    term = input("Enter a pokemon name or ID: ")
    pk = pb.pokemon(term)

    if pk:
        return pk
    else:
        return None

def name_to_id(name):
    '''
    Takes a pokemon name and returns it's ID number
    '''
    pk = pb.pokemon(name)
    id_number = pk.id_()
    return id_number

def id_to_name(id_number):
    '''
    Takes a pokemon's ID number and returns it's name
    '''
    pk = pb.pokemon(id_number)
    name = pk.name
    return name