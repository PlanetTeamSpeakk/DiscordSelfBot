import logging
import aiohttp
import random
import json
import os
import datetime
import sys
import asyncio
import re
import datetime
from time import *
from subprocess import check_output
try:
	import discord
except:
    print("You don't have discord.py installed, installing it now...")
    try:
        check_output("pip3 install discord.py", shell=True)
        import discord
        print("Discord.py succesfully installed.")
    except:
        sys.exit("Discord.py didn't succesfully install, exiting...")
try:
    from pyfiglet import figlet_format
except:
    print("You don't have pyfiglet installed, installing it now...")
    try:
        check_output("pip3 install pyfiglet", shell=True)
        import pyfiglet
        print("Pyfiglet succesfully installed.")
    except:
        sys.exit("Pyfiglet didn't succesfully install, exiting...")

cmds = {'No Category': {'help': {'help': 'Shows this screen.', 'usage': 'help [command]'}}}
        
started = datetime.datetime.utcnow()
description = "A Discord SelfBot written by PlanetTeamSpeak#4157."
if not os.path.exists("data"):
    os.makedirs("data")
if not os.path.exists("data/dsb"):
    os.makedirs("data/dsb")
if not os.path.exists("data/dsb/settings.json"):
    with open("data/dsb/settings.json", "w") as settings:
        json.dump({'email': 'email_here', 'password': 'password_here', 'whitelist': ['your_id'], 'prefix': 'prefix_here', 'invite': 'invite_here'}, settings, indent=4, sort_keys=True, separators=(',', ' : '))
        settings = None
from discord.ext import commands
with open("data/dsb/settings.json", "r") as settings_file:
    settings = json.load(settings_file)
    email = settings['email']
    password = settings['password']
    whitelist = settings['whitelist']
    prefix = settings['prefix']
    invite = settings['invite']
    bot = commands.Bot(command_prefix=prefix, description=description, self_bot=True)
    settings_file = None
    asked = False
    for key in settings:
        if "_here" in settings[key]:
            if not asked:
                asked = True
                print("First time setup, prepare your anus for some questions.")
                email = input("What's your Discord email address?\n")
                password = input("What's your Discord password?\n")
                prefix = input("What should your prefix be?\n")
                invite = input("What's the permanent invite link for you Discord server? Type None if you don't have one.\n")
                settings['email'] = email
                settings['password'] = password
                settings['prefix'] = prefix
                settings['invite'] = invite
                bot = commands.Bot(command_prefix=prefix, description=description, self_bot=True)
                settings_file = None
                with open("data/dsb/settings.json", "w") as settings_file:
                    json.dump(settings, settings_file, indent=4, sort_keys=True, separators=(',', ' : '))
                print("You're all set! Bot is starting, don't mind the unclosed client session part, just wait a bit.")
    
print("Logging in...")
    
@bot.event
async def on_ready():
    login_time = datetime.datetime.utcnow() - started
    print("\nLogin succesfull, took {}ms, started on {}.".format(login_time.seconds + login_time.microseconds/1E6, started.strftime("%d %b %Y %X")))
    print("DiscordSelfBot written by PlanetTeamSpeak#4157.\n")
    if "your_id" in whitelist:
        id = bot.user.id
        settings['whitelist'].remove("your_id")
        settings['whitelist'].append(id)
        save_settings()
    if not os.path.exists("data"):
        os.makedirs("data")
    if not os.path.exists("extensions"):
        os.makedirs("extensions")
    print("--------")
    print("Logged in as:")
    print(bot.user.name)
    print(bot.user.id)
    print("--------")
    print("Prefix: " + prefix)
    print()
    
@bot.event
async def on_message(message):
    msgchan = message.channel                    
    if await command(message, "help", True):
        cmd = message.content[len(prefix + "help "):]
        help_cmds = ""
        if cmd == "":
            for ext in cmds.keys():
                help_cmds += "\n**{}**:\n".format(ext)
                for cmda in cmds[ext].keys():
                    if len(cmda + cmds[ext][cmda]['help']) > 70:
                        help_cmds += "\t- `{}`: {}...\n".format(cmda, cmds[ext][cmda]['help'][:70])
                    else:
                        help_cmds += "\t- `{}`: {}\n".format(cmda, cmds[ext][cmda]['help'])
                    if len(help_cmds) > 1750:
                        await say(msgchan, help_cmds)
                        help_cmds = ""
            await say(msgchan, help_cmds)
            help_cmds = ""
            await say(msgchan, "To get information of a specific command type {}help <command>".format(prefix))
        else:
            error = 0
            for ext in cmds.keys():
                try:
                    temp = cmds[ext][cmd]['help']
                    await say(msgchan, "`{}` ({}):\n{}\n\nUsage:\n`{}`".format(cmd, ext, cmds[ext][cmd]['help'], prefix + cmds[ext][cmd]['usage']))
                    temp = None
                except:
                    temp = None
                    error += 1
            if error == len(cmds.keys()):
                await say(msgchan, "The command you entered ({}) could not be found.".format(cmd))
                
async def command(message, cmd, del_msg):
    if message.content.lower().startswith(prefix.lower() + cmd):
        if message.author.id in whitelist:
            if del_msg:
                try:
                    await bot.delete_message(message)
                except:
                    pass
            if cmd.endswith(" "):
                print("{} just used the {}command in {} ({}).".format(message.author, cmd, message.server, message.channel))
            else:
                print("{} just used the {} command in {} ({}).".format(message.author, cmd, message.server, message.channel))
            return True
        else:
            return False
    else:
        return False
        
def save_settings():
    with open("data/dsb/settings.json", "w") as settings_file:
        json.dump(settings, settings_file, indent=4, sort_keys=True, separators=(',', ' : '))
    reload_settings()
    
def reload_settings():
    settings = None
    with open("data/dsb/settings.json", "r") as settings_file:
        settings = None
        settings = json.load(settings_file)
        email = settings['email']
        password = settings['password']
        prefix = settings['prefix']
        whitelist = settings['whitelist']
        invite = settings['invite']
        settings_file = None
        
async def say(channel, message=None, embed=None):
    if embed is not None:
        await bot.send_message(channel, embed=embed)
    else:
        await bot.send_message(channel, message)

def is_owner(member):
    if int(member.id) == int(bot.user.id):
        return True
    else:
        return False
        
try:
    bot.load_extension("extensions.owner")
except Exception as e:
    print("Failed to load owner:\n{}".format(e))
asyncio.sleep(0.1)
with open("data/dsb/extensions.json", "r") as extensions:
    extensions = json.load(extensions)
        
for extension in extensions:
    if extensions[extension]:
        try:
            bot.load_extension("extensions." + extension)
        except Exception as e:
            print("Failed to load {}:\n{}".format(extension, e))
bot.run(email, password)