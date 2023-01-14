import discord

from discord import app_commands

intents = discord.Intents.default()
intents.message_content = True


class IndexorClient(discord.Client):
    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents)

        self.tree = app_commands.CommandTree(self)


client = IndexorClient(intents)


@client.event
async def on_ready():
    print(f"Successfully logged in as {client.user}")


def run_bot(token):
    client.run(token)
