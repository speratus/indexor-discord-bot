import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents)


@client.event
async def on_ready():
    print(f"Successfully logged in as {client.user}")


def run_bot(token):
    client.run(token)
