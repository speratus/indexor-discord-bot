import os

import discord

from discord import app_commands
from converter import dict_to_discord_message

from indexor_core.config import Config
import commands

from bot_config import BotConfig


intents = discord.Intents.default()
intents.message_content = True


class IndexorClient(discord.AutoShardedClient):
    def __init__(self, intents: discord.Intents):
        super().__init__(intents=intents)

        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self) -> None:
        config = BotConfig('config.ini')

        guild_id = None

        if config.bot.environment == 'dev':
            guild_id = discord.Object(id=config.bot.guild_id)
            self.tree.copy_global_to(guild=guild_id)

        await self.tree.sync(guild=guild_id)


client = IndexorClient(intents)


@client.event
async def on_ready():
    print(f"Successfully logged in as {client.user}")


@client.tree.command(name="search")
@app_commands.describe(search="What you want to know")
async def search(interaction: discord.Interaction, search: str):
    c = Config(engine_url=os.getenv("ENGINE_URL"))

    await interaction.response.defer(ephemeral=False, thinking=True)

    try:
        response_info = await commands.search(search, c)
    except Exception as e:
        await interaction.followup.send(content=f"Dewey Encountered an error and couldn't get results for the search: \"{search}\".", ephemeral=True)
        print(f"Failed to get results for: {search}")
        print("STACK TRACE-------------------------")
        print(e)
        return

    try:
        await interaction.followup.send(**dict_to_discord_message(response_info))
    except (discord.HTTPException, discord.InteractionResponded) as e:
        await interaction.followup.send(content="Message Deleted")
        await client.get_channel(interaction.channel_id).send(content="Dewey crashed and cannot respond at the moment", delete_after=300)
        print(f"Dewey crashed while trying to respond!")


def run_bot(token):
    client.run(token)
