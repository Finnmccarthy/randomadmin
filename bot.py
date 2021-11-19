import asyncio
import discord
from discord.ext import commands
from discord.utils import get
from discord_slash import SlashCommand
import logging
import json
from datetime import datetime
import random
from pathlib import Path

description = 'A Discord bot that randomly give someone admin on join'

# Date & Time Variable
timestamp = datetime.now()
gettime = timestamp.strftime(r"%d/%m/%Y %I:%M%p")

cwd = Path(__file__).parents[0]
cwd = str(cwd)
print(f"{cwd}\n-----")

intents = discord.Intents.all()

bot = discord.Client()
config_file = json.load(open(cwd+'/bot_config/config.json'))
bot.config_prefix = config_file['prefix']
bot = commands.Bot(bot.config_prefix, intents=intents, description=description, case_insensitive=True)
slash = SlashCommand(bot)

# Token
token_file = json.load(open(cwd+'/bot_config/token.json'))
bot.token_file = token_file['token']
logging.basicConfig(level=logging.INFO)

# Bot ready log
@bot.event
async def on_ready():
    print(f"-----\nLogged in as: {bot.user.name} : {bot.user.id}\n-----\nCurrent prefix = {config_file['prefix']} & /\n-----\nDate & Time: {gettime}\n-----\nBot is ready\n-----")



@bot.event
async def on_member_join(member):
    #role_id_admin = config_file['role_id_admin']
    role_name_admin = config_file['role_name_admin']
    role_admin = discord.utils.get(member.guild.roles, name=role_name_admin)
    #role_id_member = config_file['role_id_member']
    role_name_member = config_file['role_name_member']
    role_member  = discord.utils.get(member.guild.roles, name=role_name_member)
    
    rand = random.randint(1, 5)

    channel_id = 746967709174071349
    channel = bot.get_channel(channel_id)

    with open('cache/joincache.txt', 'r+') as f:
        if str(member.id) in f.read():
            await member.add_roles(role_member)
            
            embedvar0 = discord.Embed(title="Welcome", description=f"{member.mention} has already joined this server before, stop trying to cheat.", color=0x00ff00)
            await channel.send(embed=embedvar0, delete_after=60)
        
        elif rand == 1:
            await member.add_roles(role_admin)
            f.write(f"{member.id}\n ")

            embedvar1 = discord.Embed(title="Welcome", description=f"Congratulations {member.mention}, you have been randomly selected to be an Admin.", color=0x00ff00)
            await channel.send(embed=embedvar1, delete_after=120)

        else:
            await member.add_roles(role_member)

            embedvar2 = discord.Embed(title="Welcome", description=f"{member.mention} has randomly roled the {role_name_member} role, unlucky champion.", color=0x00ff00)
            await channel.send(embed=embedvar2, delete_after=60)












bot.run(bot.token_file)