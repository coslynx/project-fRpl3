import discord

class Logging:
    def __init__(self):
        self.log_channel = None

    async def set_log_channel(self, channel):
        self.log_channel = channel

    async def log_action(self, action, user, reason):
        if self.log_channel:
            await self.log_channel.send(f"Action: {action}\nUser: {user}\nReason: {reason}")
        else:
            print("Log channel not set. Unable to log action.")

    async def log_mute(self, user, duration):
        if self.log_channel:
            await self.log_channel.send(f"{user} has been muted for {duration}.")
        else:
            print("Log channel not set. Unable to log action.")

    async def log_warn(self, user, reason):
        if self.log_channel:
            await self.log_channel.send(f"{user} has been warned. Reason: {reason}")
        else:
            print("Log channel not set. Unable to log action.")

    async def log_kick(self, user, reason):
        if self.log_channel:
            await self.log_channel.send(f"{user} has been kicked. Reason: {reason}")
        else:
            print("Log channel not set. Unable to log action.")

    async def log_ban(self, user, reason):
        if self.log_channel:
            await self.log_channel.send(f"{user} has been banned. Reason: {reason}")
        else:
            print("Log channel not set. Unable to log action.")