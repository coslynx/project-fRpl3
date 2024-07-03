import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix='!', intents=intents)

@client.event
async def on_ready():
    print('Bot is ready.')

@client.event
async def on_member_join(member):
    await member.send('Welcome to the server!')

client.run('your_bot_token')