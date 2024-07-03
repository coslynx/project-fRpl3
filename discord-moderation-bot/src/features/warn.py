import discord

class Warn(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def warn(self, ctx, member: discord.Member, *, reason="No reason provided"):
        # Logic to issue a warning to a user
        await ctx.send(f'{member.mention} has been warned for: {reason}')

def setup(client):
    client.add_cog(Warn(client))