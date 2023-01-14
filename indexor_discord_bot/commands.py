import discord
from converter import dict_to_discord_message


def interaction_command(callback):
    async def wrapped_command(interaction: discord.Interaction, *args):
        response = callback(*args)

        discord_data = dict_to_discord_message(response)

        await interaction.response.send_message(discord_data)

    return wrapped_command
