import discord
from discord.ext import commands

intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command(name='customcommand')
async def custom_command(ctx, command_name):
    # Your custom command logic here
    await ctx.send(f'Executing custom command: {command_name}')

bot.run('YOUR_BOT_TOKEN')