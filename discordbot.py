from discord import Client, Intents
from discord_slash import SlashCommand, SlashContext

# Set up intents
intents = Intents.default()
intents.messages = True
intents.guilds = True

# Create client instance
client = Client(intents=intents)
slash = SlashCommand(client, sync_commands=True)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}!')

@slash.slash(name="hello", description="Responds with Hello!", guild_ids=[your_guild_id])
async def hello(ctx: SlashContext):
    await ctx.send("Hello from my bot!")

# Replace 'your_token_here' with your actual bot token
client.run('NTA4Mjk0NzU4MDMzMjYwNTc0.GExjeA.urgN90aRMq6j171oAKC9-BIhl1Hsjxe47o6E8o')
