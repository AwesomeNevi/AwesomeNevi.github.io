from discord import Client, Intents
from discord.ext.commands import Bot
from discord.commands import slash_command  # This now should work

# Define intents
intents = Intents.default()
intents.messages = True
intents.guilds = True

# Bot setup
bot = Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}!')

@slash_command(guild_ids=[1237307191740993560], description="Say hello")
async def hello(ctx):
    await ctx.respond("Hello from my bot!")

#
bot.run('NTA4Mjk0NzU4MDMzMjYwNTc0.GExjeA.urgN90aRMq6j171oAKC9-BIhl1Hsjxe47o6E8o')
