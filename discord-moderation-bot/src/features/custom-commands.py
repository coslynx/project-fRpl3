import discord

class CustomCommands:
    def __init__(self, bot):
        self.bot = bot
        self.custom_commands = {}

    async def handle_custom_command(self, message):
        command = message.content.split()[0][1:]
        if command in self.custom_commands:
            response = self.custom_commands[command]
            await message.channel.send(response)

    def add_custom_command(self, command, response):
        self.custom_commands[command] = response

    def remove_custom_command(self, command):
        if command in self.custom_commands:
            del self.custom_commands[command]

    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        if message.content.startswith('!'):
            await self.handle_custom_command(message)

    async def on_ready(self):
        print('Custom Commands module loaded.')

def setup(bot):
    custom_commands = CustomCommands(bot)
    bot.add_cog(custom_commands)