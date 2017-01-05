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

cmds = {'help': {'help': 'Shows this screen.', 'usage': 'help [command]'},
'restart': {'help': 'Restarts the bot.', 'usage': 'restart'},
'boobs': {'help': 'Shows some boobs.', 'usage': 'boobs'},
'ass': {'help': 'Shows some ass.', 'usage': 'ass'},
'say': {'help': 'Let\'s the bot say something.', 'usage': 'say <message>'},
'server owner': {'help': 'Shows the server owner.', 'usage': 'server owner'},
'server name': {'help': 'Shows the server name.', 'usage': 'server name'},
'server sid': {'help': 'Shows the server id.', 'usage': 'server sid'},
'server channelname': {'help': 'Shows the channel name.', 'usage': 'server channelname'},
'server cid': {'help': 'Shows the channel id.', 'usage': 'server cid'},
'server time': {'help': 'Shows the server time.', 'usage': 'server time'},
'server roles': {'help': 'Shows the server roles.', 'usage': 'server roles'},
'server emojis': {'help': 'Shows the server emojis.', 'usage': 'server emojis'},
'server users': {'help': 'Shows the server users.', 'usage': 'server users'},
'server channels': {'help': 'Shows the server channels', 'usage': 'server channels'},
'server compareids': {'help': 'Compares the ids of the server and the channel to see if it is default.', 'usage': 'server compareids'},
'server icon': {'help': 'Shows the server icon.', 'usage': 'server icon'},
'server channelinfo': {'help': 'Shows information of this channel.', 'usage': 'server channelinfo'},
'server membercount': {'help': 'Counts the members in this server.', 'usage': 'server membercount'},
'server rolecount': {'help': 'Counts the roles in this server.', 'usage': 'server rolecount'},
'server emojicount': {'help': 'Counts the emojis in this server.', 'usage': 'server emojicount'},
'server userinfo': {'help': 'Shows information of the given user, if none given shows information for the bot owner.', 'usage': 'server userinfo [user_name]'},
'server roleinfo': {'help': 'Shows information of the given role.', 'usage': 'server roleinfo <role>'},
'download': {'help': 'Downloads a file from a url and puts it in data/downloads', 'usage': 'download <url>'},
'mentionmsg': {'help': 'Sets the message that will be sent when someone mentions you, if you don\'t want the bot to send one you would put None here.', 'usage': 'mentionmsg <msg>'},
'whitelist add': {'help': 'Adds a user to the whitelist, use ids for this.', 'usage': 'whitelist add <user_id>'},
'whitelist remove': {'help': 'Removes a user from the whitelist, use ids for this.', 'usage': 'whitelist remove <user_id>'},
'lenny': {'help': 'Prints out a lenny face.', 'usage': 'lenny'},
'shrug': {'help': 'Shrugs.', 'usage': 'shrug'},
'shutdown': {'help': 'Shuts down the bot.', 'usage': 'shutdown'},
'name': {'help': 'Sets the name of the owner of the bot, limited by Discord to twice per hour.', 'usage': 'name <name>'},
'greentext': {'help': 'Makes your text green.', 'usage': 'greentext <text>'},
'orangetext': {'help': 'Makes your text orange.', 'usage': 'orangetext <text>'},
'bluetext': {'help': 'Makes your text blue. Looks pretty shitty tbh.', 'usage': 'bluetext <text>'},
'lmgtfy': {'help': 'Makes a lmgtfy (let me google that for you) link.', 'usage': 'lmgtfy <search_quarries>'},
'navyseal': {'help': 'Prints the navyseal copypasta.', 'usage': 'navyseal'},
'edgyshit': {'help': 'Prints the edgyshit copypasta.', 'usage': 'edgyshit'},
'goodshit': {'help': 'Prints the goodshit copypasta.', 'usage': 'goodshit'},
'appache': {'help': 'Prints the attack helicopter copypasta.', 'usage': 'appache'},
'daddy': {'help': 'Prints the daddy copypasta.', 'usage': 'daddy'},
'4chan': {'help': 'Prints the 4chan copypasta.', 'usage': '4chan'},
'triggered': {'help': 'The h3h3 triggered meme gif.', 'usage': 'triggered'},
'setprefix': {'help': 'Sets the prefix of the bot.', 'usage': 'setprefix <prefix>'},
'flirting101': {'help': 'Prints the flirting101 copypasta.', 'usage': 'flirting101'},
'setinvite': {'help': 'Sets the invite to send everybody for the spaminvite and spaminvitedm commands.', 'usage': 'setinvite <invite>'},
'spaminvite': {'help': 'Spams the invite in the channel the command was sent.', 'usage': 'spaminvite <times>'},
'spaminvitedm': {'help': 'Sends the invite to everyone in the server except for mods and admins.', 'usage': 'spaminvitedm <message>'},
'discrim': {'help': 'Searched through all members the bot can see to see if they have the given discriminator (the number after your name (example: YourName#4157))', 'usage': 'discrim <discrim'},
'emoteurl': {'help': 'Gives the url for the given emote.', 'usage': 'emoteurl <emote_name>'},
'genbotoauth': {'help': 'Generates an oauth url of the given bot.', 'usage': 'genbotoauth <bot_name>'},
'genoauth': {'help': 'Generates an oauth url for the given client id.', 'usage': 'genoauth <client_id>'},
'calc': {'help': 'Calculates a math problem so you don\'t have to.', 'usage': 'calc <problem>'},
'avatar': {'help': 'Shows the avatar of the given user.', 'usage': 'avatar <user>'},
'mentionmode': {'help': 'Sets the mode the bot should use when you get mentioned (legit of fast)', 'usage': 'mentionmode <mode>'},
'convert': {'help': 'Converts a file to something like mp4 mp3 png gif all that stuff.', 'usage': 'convert <file_url>'},
'ascii': {'help': 'Converts text to ascii (figlet)', 'usage': 'ascii <text>'},
'penis': {'help': 'Detects a users penis length, this is 100% accurate.', 'usage': 'penis <user_name>'},
'shorten': {'help': 'Shortens a link.', 'usage': 'shorten <url>'},
'ping': {'help': 'Pong!', 'usage': 'ping'},
'qrcode': {'help': 'Creates a qrcode of the given url.', 'usage': 'qrcode <url>'},
'uptime': {'help': 'Shows the bots uptime.', 'usage': 'uptime'},
'clearconsole': {'help': 'Clears the console.', 'usage': 'clearconsole'}
}
        
started = datetime.datetime.now()
description = "A Discord SelfBot written by PlanetTeamSpeak#4157."
if not os.path.exists("data"):
    os.makedirs("data")
if not os.path.exists("data/dsb"):
    os.makedirs("data/dsb")
if not os.path.exists("data/dsb/settings.json"):
    with open("data/dsb/settings.json", "w") as settings:
        json.dump({'email': 'email_here', 'password': 'password_here', 'whitelist': ['your_id'], 'prefix': 'prefix_here', 'mentionmsg': 'mentionmsg_here', 'invite': 'invite_here', 'mentionmode': 'mentionmode_here'}, settings, indent=4, sort_keys=True, separators=(',', ' : '))
        settings = None
from discord.ext import commands
with open("data/dsb/settings.json", "r") as settings_file:
    settings = json.load(settings_file)
    email = settings['email']
    password = settings['password']
    whitelist = settings['whitelist']
    prefix = settings['prefix']
    mentionmsg = settings['mentionmsg']
    invite = settings['invite']
    mentionmode = settings['mentionmode']
    bot = commands.Bot(command_prefix=prefix, description=description)
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
                mentionmsg = input("What should you respond when you get mentioned? Type None to not respond. You can always set this later with {}mentionmsg\n".format(prefix))
                if mentionmsg != "None":
                    mentionmode = input("Do you want the message that the bot sends when you get mentioned to look legit (waits 2 secs, sends typing for 2 secs, sends message)\nOr would you like it to be fast (just send the message)\n(choose from legit or fast)\n")
                invite = input("What's the permanent invite link for you Discord server? Type None if you don't have one.\n")
                settings['email'] = email
                settings['password'] = password
                settings['prefix'] = prefix
                settings['mentionmsg'] = mentionmsg
                settings['invite'] = invite
                if mentionmsg != "None":
                    settings['mentionmode'] = mentionmode
                else:
                    settings['mentionmode'] = "fast"
                bot = commands.Bot(command_prefix=prefix, description=description)
                settings_file = None
                with open("data/dsb/settings.json", "w") as settings_file:
                    json.dump(settings, settings_file, indent=4, sort_keys=True, separators=(',', ' : '))
                print("You're all set! Bot is starting")
    
@bot.event
async def on_ready():
    print("\nStarted on {}".format(started.strftime("%d %b %Y %X")))
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
    if await command(message, "restart", True):
        await main.say(msgchan, "Restarting...")
        bot.run(email, password)
                    
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
        mentionmsg = settings['mentionmsg']
        invite = settings['invite']
        mentionmode = settings['mentionmode']
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
      
with open("data/dsb/extensions.json", "r") as extensions:
    extensions = json.load(extensions)
        
for extension in extensions:
    if extensions[extension]:
        try:
            bot.load_extension("extensions." + extension)
        except Exception as e:
            print("Failed to load {}:\n{}".format(extension, e))
bot.run(email, password)