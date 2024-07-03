import discord

class Logging:
    def __init__(self, client):
        self.client = client

    async def log_action(self, action_type, user, reason):
        log_channel = discord.utils.get(user.guild.text_channels, name="mod-logs")
        if log_channel is not None:
            embed = discord.Embed(title=f"{action_type} Action", color=discord.Color.red())
            embed.add_field(name="User", value=user.display_name, inline=False)
            embed.add_field(name="Reason", value=reason, inline=False)
            await log_channel.send(embed=embed)

    async def log_warn(self, user, reason):
        await self.log_action("Warning", user, reason)

    async def log_mute(self, user, reason):
        await self.log_action("Mute", user, reason)

    async def log_kick(self, user, reason):
        await self.log_action("Kick", user, reason)

    async def log_ban(self, user, reason):
        await self.log_action("Ban", user, reason)