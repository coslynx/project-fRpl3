import discord

intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!kick'):
        if message.author.guild_permissions.kick_members:
            member = message.mentions[0]
            await member.kick()
            await message.channel.send(f'{member} has been kicked from the server.')
        else:
            await message.channel.send('You do not have permission to kick members.')

    if message.content.startswith('!ban'):
        if message.author.guild_permissions.ban_members:
            member = message.mentions[0]
            await member.ban()
            await message.channel.send(f'{member} has been banned from the server.')
        else:
            await message.channel.send('You do not have permission to ban members.')

client.run('your_token_here')