import discord
import re

class MessageFiltering:
    def __init__(self, client):
        self.client = client

    async def filter_messages(self, message):
        if await self.check_spam(message):
            await self.client.send_message(message.channel, "Message filtered: spam detected.")
        elif await self.check_offensive_language(message):
            await self.client.send_message(message.channel, "Message filtered: offensive language detected.")
        elif await self.check_violations(message):
            await self.client.send_message(message.channel, "Message filtered: violations detected.")

    async def check_spam(self, message):
        # Implement spam detection logic here
        return False

    async def check_offensive_language(self, message):
        # Implement offensive language detection logic here
        return False

    async def check_violations(self, message):
        # Implement violations detection logic here
        return False

# Initialize the bot
client = discord.Client()
filtering = MessageFiltering(client)

@client.event
async def on_message(message):
    await filtering.filter_messages(message)

# Run the bot
client.run("YOUR_DISCORD_BOT_TOKEN")