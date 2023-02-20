import discord
from converter import dict_to_discord_message
from discord import Color

from indexor_core.config import Config
from indexor_core.searcher import search_async


def interaction_command(callback):
    async def wrapped_command(interaction: discord.Interaction, *args):
        response = callback(*args)

        discord_data = dict_to_discord_message(response)

        await interaction.response.send_message(discord_data)

    return wrapped_command


async def search(terms: str, config: Config) -> dict:
    results = await search_async(terms, config)

    response_data = str(results)[0:250] + '...'

    print(response_data)

    top_5 = results['results'][0:25]

    response_info = {
        'content': f'Top 5 Results for Search "{terms}":',
    }

    embeds = []

    for r in top_5:
        if 'content' not in r:
            continue

        embeds.append({
            'title': r['title'],
            'url': r['url'],
            'description': r['content'] + '\n\n' + r['url'] + '\nengines: ' + ', '.join(r['engines']),
            'color': Color.from_str('#37b9d9'),
        })

    response_info['embeds'] = embeds[0:5]

    return response_info
