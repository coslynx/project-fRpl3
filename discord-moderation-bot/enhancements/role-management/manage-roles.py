import discord

class RoleManagement:
    def __init__(self, client):
        self.client = client

    async def assign_role(self, member, role_name):
        role = discord.utils.get(member.guild.roles, name=role_name)
        if role:
            await member.add_roles(role)
        else:
            print(f"Role '{role_name}' not found.")

    async def remove_role(self, member, role_name):
        role = discord.utils.get(member.guild.roles, name=role_name)
        if role:
            await member.remove_roles(role)
        else:
            print(f"Role '{role_name}' not found.")

    async def get_member_roles(self, member):
        return [role.name for role in member.roles]