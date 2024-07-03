import discord

class Warn:
    def __init__(self, client):
        self.client = client

    async def issue_warning(self, message, user):
        try:
            await message.channel.send(f'{user.mention}, you have received a warning for violating the server rules.')
        except discord.errors.Forbidden:
            await message.author.send('I do not have permission to send messages in that channel.')

    async def warn_user(self, message, user):
        if user.bot:
            await message.channel.send('Bots cannot receive warnings.')
        else:
            await self.issue_warning(message, user)

    async def handle_warn_command(self, message):
        if len(message.mentions) == 0:
            await message.channel.send('Please mention the user you want to warn.')
        else:
            user = message.mentions[0]
            await self.warn_user(message, user)

    async def on_message(self, message):
        if message.content.startswith('!warn'):
            await self.handle_warn_command(message)

def setup(client):
    warn = Warn(client)
    client.add_cog(warn)