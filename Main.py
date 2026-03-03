import discord
from discord.ext import commands
from discord import app_commands
import random
from dotenv import load_dotenv
import os
from datetime import timedelta

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

MY_GUILD = discord.Object(id=guild id)

balances = {}

class MyClient(discord.Client):
    user: discord.ClientUser

    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents=intents)

        self.tree = app_commands.CommandTree(self)


    async def setup_hook(self):
        self.tree.copy_global_to(guild=MY_GUILD)
        await self.tree.sync(guild=MY_GUILD)

    

intents = discord.Intents.default()
intents.members = True
client = MyClient(intents=intents)


@client.event
async def on_ready():
    print(f'Logged as {client.user}')
    print('-------')


@client.event
async def on_member_join(member):
        channel = member.guild.get_channel(channel id)
        role = member.guild.get_role(role id)
        to_send = f'Welcome {member.mention} to Rays`s restaurant hope you enjoy!'
        await channel.send(to_send)
        await member.add_roles(role)

#Joined
@client.tree.command(name='joined',description='Show when a user joined the server')
async def joined(ctx: discord.Interaction, member:discord.Member):
    if member.joined_at is None:
        await ctx.response.send_message(f'{member} has no join date')
    else:
        await ctx.response.send_message(f'{member} joined {discord.utils.format_dt(member.joined_at)}')

#Github
@client.tree.command(name='git',description='Show the github profile')
async def git(ctx: discord.Interaction):
    await ctx.response.send_message('Here`s my owner profile on github: https://github.com/XxTofu')

#clear
@client.tree.command(name='clear', description='Delete channel messages (max 100)')
@app_commands.checks.has_permissions(manage_messages=True)
async def clear(ctx: discord.Interaction, times: int):

    # Limit to 1–100 messages
    if times < 1 or times > 100:
        await ctx.response.send_message(
            "❌ I can only delete between 1 and 100 messages.",
            ephemeral=True
        )
        return

    # Check bot permissions
    if not ctx.guild.me.guild_permissions.manage_messages:
        await ctx.response.send_message(
            "❌ You don't have permission to manage messages.",
            ephemeral=True
        )
        return

    await ctx.response.defer(ephemeral=True)

    deleted = await ctx.channel.purge(limit=times)

    await ctx.followup.send(
        f'✅ Deleted {len(deleted)} messages.',
        ephemeral=True
    )

#Timeout
@client.tree.command(name='timeout', description='Timeout a member')
@app_commands.checks.has_permissions(moderate_members=True)
async def timeout(ctx: discord.Interaction, member: discord.Member, minutes: int):
    await member.timeout(timedelta(minutes=minutes))
    await ctx.response.send_message(f'⏳ {member.mention} timed out for {minutes} minutes.')

#Ban
@client.tree.command(name='ban', description='Ban a member from the server')
@app_commands.checks.has_permissions(ban_members=True)
async def ban(ctx: discord.Interaction, member: discord.Member, reason: str = None):

    if member.top_role >= ctx.user.top_role:
        await ctx.response.send_message(
            '❌ You cannot ban someone with an equal or higher role.',
            ephemeral=True
        )
        return

    if not ctx.guild.me.guild_permissions.ban_members:
        await ctx.response.send_message(
            '❌ I don`t have permission to ban members.',
            ephemeral=True
        )
        return

    await member.ban(reason=reason)

    await ctx.response.send_message(
        f'✅ {member} was banned.\nReason: {reason or "No reason provided"}',
        ephemeral=True
    )

#Unban
@client.tree.command(name='unban', description='Unban a member from the server')
@app_commands.checks.has_permissions(ban_members=True)
async def unban(ctx: discord.Interaction, member: discord.User):

    if not ctx.guild.me.guild_permissions.ban_members:
        await ctx.response.send_message(
            '❌ I don`t have permission to unban members.',
            ephemeral=True
        )
        return

    async for entry in ctx.guild.bans():
        if entry.user.id == member.id:
            await ctx.guild.unban(member)
            await ctx.response.send_message(
                f'✅ {member.mention} was unbanned.',
                ephemeral=True
            )
            return

    await ctx.response.send_message(
        f'❌ {member} was not banned.',
        ephemeral=True
    )

#kick
@client.tree.command(name='kick', description='Kick a member from the server')
@app_commands.checks.has_permissions(kick_members=True)
async def kick(ctx: discord.Interaction, member: discord.Member, reason: str = None):

    if member == ctx.user:
        await ctx.response.send_message(
            '❌ You cannot kick yourself.',
            ephemeral=True
        )
        return

    if member.top_role >= ctx.user.top_role:
        await ctx.response.send_message(
            '❌ You cannot kick someone with an equal or higher role.',
            ephemeral=True
        )
        return

    if not ctx.guild.me.guild_permissions.kick_members:
        await ctx.response.send_message(
            '❌ I don`t have permission to kick members.',
            ephemeral=True
        )
        return

    if member.top_role >= ctx.guild.me.top_role:
        await ctx.response.send_message(
            '❌ I cannot kick this member due to role hierarchy.',
            ephemeral=True
        )
        return

    await member.kick(reason=reason)

    await ctx.response.send_message(
        f'✅ {member.mention} was kicked.\nReason: {reason or "No reason provided"}',
        ephemeral=True
    )

#ship
@client.tree.command(name='ship', description='Calculate love compatibility and generate a cute ship name 💕')
async def ship(ctx:discord.Interaction, member1: discord.Member, member2 : discord.Member):
    percent = random.randint(1, 100)
    name1 = str(member1.display_name)
    name2 = str(member2.display_name)
    name1 = name1.capitalize()
    name2 = name2.capitalize()  
    if len(name1) >= 3 and len(name2) >= 3:
        shipname = name1[:3] + name2[-2:]
    elif len(name1) >= 3 and len(name2) < 3:
        shipname = name1[:3] + name2[-1:]
    elif len(name1) < 3 and len(name2) >= 3:
        shipname = name1[:1] + name2[-2:] 
    else:
        shipname = name1[:1] + name2[-1:]
     
    await ctx.response.send_message(f'Ship Name: {shipname} \n❤️{member1.mention} has a {percent}% compatibility with {member2.mention}❤️')

#rob
@client.tree.command(name='rob', description='Steal a user`s avatar')
async def rob(ctx:discord.Interaction, member: discord.Member):
    role = ctx.guild.get_role(roleid)
    if role in ctx.user.roles:
        if member.display_avatar == member.default_avatar:
            await ctx.response.send_message('The user has the default avatar')
        else:
            await ctx.response.send_message(f'✅Here is the icon: {member.display_avatar}')
    else:
        await ctx.response.send_message('❌You do not have the role for this ')


@clear.error
@ban.error
@unban.error
@kick.error
async def permission_error(ctx: discord.Interaction, error):
    if isinstance(error, app_commands.errors.MissingPermissions):
        await ctx.response.send_message(
            '❌ You don`t have the required permissions to use this command.',
            ephemeral=True
        )


client.run(token)
