import discord

class WelcomeMessage:
    def __init__(self, client):
        self.client = client

    async def send_welcome_message(self, member):
        channel = member.guild.system_channel
        if channel:
            await channel.send(f'Welcome to the server, {member.mention}!')

def setup(client):
    welcome_message = WelcomeMessage(client)
    client.add_cog(welcome_message)