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


File:           bot.py
Description:    Discord bot for Pydex

Author:  Tem Tamre
Contact: ttamre@ualberta.ca
Version: 1.0
"""

import discord
import logging
import json
from client import Pydex

logging.basicConfig(level=logging.INFO)
client = Pydex()
owners = ["tei#0397"]


class Bot(discord.Client):

    async def on_ready(self):
        print("-" * 24)
        print("Logged in as {}\n".format(self.user))
        print("A discord bot that allows users to search for pokemon")
        print("Developed and maintained as a personal project by Tem Tamre (ttamre@ualberta.ca)")
        print("Source code available at https://github.com/ttamre/pydex")
        print("-" * 24)

        await self.change_presence(status=discord.Status.online, activity=discord.Activity(name="$help for help"))

    async def on_message(self, message):
        """
        Sends a message to the channel that a command was issued in
        :param message:message  Command issued by a user
        """
        if message.author == self.user:
            return

        if message.content.startswith("$"):
            input_message = message.content.lower().split(" ")
            logging.info("{user} said: {message}".format(user=message.author, message=message.content))

            if "$pokemon" == input_message[0]:
                output_message, images = self._pokemon(query=" ".join(input_message[1:]))
                await message.channel.send(content=output_message, files=images)
            
            elif "$author" == input_message[0]:
                await message.channel.send(self._author())
            
            elif "$help" == input_message[0]:
                await message.channel.send(self._help())
            
            elif "$exit" == input_message[0]:
                if str(message.author) in owners:
                    await message.channel.send("`Logging off`")
                    await self.logout()
                else:
                    output_message = "You do not have permission to use that command"
            
            else:
                output_message = "Invalid command. For a list of commands, enter `$help`"
            
    def _pokemon(self, query):
        if query == "god":
            return ("", [discord.File(fp=client.god(), filename="god.jpg")])

        pokemon = client.search_cache(query)
        if not pokemon:
            pokemon = client.search_pokemon(query)

        name = pokemon["name"]
        ptype = client.parse_types(pokemon["types"])
        height = pokemon["height"] / 10
        weight = pokemon["weight"] / 10
        
        images = client.fetch_images(pokemon.get("sprites"))
        if images:
            images = [discord.File(fp=f[1], filename=f"file{f[0]+1}.png") for f in enumerate(images)]

        output = f"**{name.title()}** is a **{ptype}** type pokemon, measuring at {height} metres tall with a weight of {weight}kg"
        return (output, images)

    def _author(self):
        author = "**Author:** Tem Tamre\n"
        contact = "**Contact:** ttamre@ualberta.ca\n"
        github = "**Github:** https://www.github.com/ttamre"
        return author + contact + github

    def _help(self):
        pokemon = "To search for a pokemon, enter `$pokemon pokemon_name`\n"
        author = "To view author contact info, enter `$author`\n"
        exit_ = "To log the bot off, enter `$exit` (only owners of this bot can execute this command, contact the server owner or tei#0397 for assistance)"
        return pokemon + author + exit_

    
