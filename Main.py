import discord
from discord.ext import commands
from discord import app_commands
import random

token = input('Token: ')

MY_GUILD = discord.Object(id='guild id)


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
        channel = member.guild.get_channel('channel id)
        role = member.guild.get_role('role id)
        to_send = f'Welcome {member.mention} to Rays`s restaurant hope you enjoy!'
        await channel.send(to_send)
        await member.add_roles(role)

@client.tree.command(name='joined',description='Show when a user joined the server')
async def joined(ctx: discord.Interaction, member:discord.Member):
    if member.joined_at is None:
        await ctx.response.send_message(f'{member} has no join date')
    else:
        await ctx.response.send_message(f'{member} joined {discord.utils.format_dt(member.joined_at)}')


@client.tree.command(name='git',description='Show the github profile')
async def git(ctx: discord.Interaction):
    await ctx.response.send_message('Here`s my owner profile on github: https://github.com/XxTofu')

@client.tree.command(name='clear', description='Delete channel messages')
async def clear(ctx: discord.Interaction, times:int):
    role = ctx.guild.get_role('role id)
    role1 = ctx.guild.get_role('role id)
    if role in ctx.user.roles or role1 in ctx.user.roles:
        await ctx.response.defer(ephemeral=True)

        deleted = await ctx.channel.purge(limit=times)

        await ctx.followup.send(
            f'✅ Deleted {len(deleted)} messages.',
            ephemeral=True
        )

    else:
        await ctx.response.send_message('❌ You dont have the necessary permission for that.',
            ephemeral=True)


@client.tree.command(name='ban', description='Ban a member from the server')
async def ban(ctx: discord.Interaction, member: discord.Member, reason: str=None):
    role = ctx.guild.get_role('role id)
    role1 = ctx.guild.get_role('role id)
    if role in ctx.user.roles or role1 in ctx.user.roles:
         await member.ban(reason=reason)
         await ctx.response.send_message(
             f'✅{member} was banned! {reason}'
             )

    else:
        await ctx.response.send_message(
            f'❌{ctx.user} does not have the permission for that',
              ephemeral=True
            )

@client.tree.command(name='unban', description='Unban a member from the server')
async def unban(ctx: discord.Interaction, member: discord.User):
    role = ctx.guild.get_role(role id)
    role1 = ctx.guild.get_role('role id)
    if role in ctx.user.roles or role1 in ctx.user.roles:
        async for entry in ctx.guild.bans():
            if entry.user.id == member.id:
                await ctx.guild.unban(member)
                await ctx.response.send_message(
                    f'✅{member.mention} was unbanned'
                    )
                return
        await ctx.response.send_message(
            f'❌{member} was not banned'
            )
        return
    else:
        await ctx.response.send_message(
            f'❌{ctx.user} does not have the permission for that',
              ephemeral=True
            )

@client.tree.command(name='kick', description='Kick a member from the server')
async def kick(interaction: discord.Interaction, member: discord.Member, reason: str = None):

    role = interaction.guild.get_role(roleid)
    role1 = interaction.guild.get_role(roleid)

    if role in interaction.user.roles or role1 in interaction.user.roles:

        if member == interaction.user:
            await interaction.response.send_message(
                '❌ You cannot kick yourself.',
                ephemeral=True
            )
            return

        if member.top_role >= interaction.user.top_role:
            await interaction.response.send_message(
                '❌ You cannot kick someone with an equal or higher role.',
                ephemeral=True
            )
            return

        await member.kick(reason=reason)

        await interaction.response.send_message(
            f'✅ {member.mention} was kicked.\nReason: {reason or 'No reason provided'}',
            ephemeral=True
        )

    else:
        await interaction.response.send_message(
            '❌ You do not have permission for that.',
            ephemeral=True
        )        

@client.tree.command(name='ship')
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


@client.tree.command(name='rob')
async def rob(ctx:discord.Interaction, member: discord.Member):
    if member.display_avatar == member.default_avatar:
        await ctx.response.send_message(f'Default Discord avatar...')
    else:
        await ctx.response.send_message(f'Here is the icon: {member.display_avatar}')



client.run(token)
