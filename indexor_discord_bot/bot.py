import discord

from discord import app_commands
from converter import dict_to_discord_message

from indexor_core.config import ini_file_loader
import commands

from bot_config import BotConfig


intents = discord.Intents.default()
intents.message_content = True


class IndexorClient(discord.Client):
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


@client.tree.command(name="test-command")
async def test_command(interaction: discord.Interaction):
    await interaction.response.send_message(content="It works!")


@client.tree.command(name="echo")
@app_commands.describe(text="Enter the text to echo")
async def echo(interaction: discord.Interaction, text: str):
    data = {
        'content': 'You ran the echo command!',
        'embed': {
            "title": "Echoed Text",
            "description": text,
        },
    }

    response_data = dict_to_discord_message(data)

    print(response_data)

    await interaction.response.send_message(**response_data)


@client.tree.command(name="search")
@app_commands.describe(search="What you want to know")
async def search(interaction: discord.Interaction, search: str):
    c = ini_file_loader('config.ini')

    await interaction.response.defer(ephemeral=False, thinking=True)

    response_info = await commands.search(search, c)

    await interaction.followup.send(**dict_to_discord_message(response_info))


def run_bot(token):
    client.run(token)
