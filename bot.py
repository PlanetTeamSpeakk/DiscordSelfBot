from discord.ext import commands
import logging
import aiohttp
import random
import json
import os
import datetime
import sys
import asyncio
import re
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
    from pyshorteners import Shortener as shortener
except:
    print("You don't have pyshorteners installed, installing it now...")
    try:
        check_output("pip3 install pyshorteners", shell=True)
        import pyshorteners
        print("Pyshorteners succesfully installed.")
    except:
        sys.exit("Pyshorteners didn't succesfully install, exiting...")
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
try:
    import ffmpy
except:
    print("You don't have FFMpy installed, installing it now...")
    try:
        check_output("pip3 install ffmpy", shell=True)
        import ffmpy
        print("FFMpy succesfully installed.")
    except:
        sys.exit("FFMpy could not be installed, exiting...")
    
description = "A Discord SelfBot written by PlanetTeamSpeak#4157."
if not os.path.exists("settings.json"):
    with open("settings.json", "w") as settings:
        json.dump({'email': 'email_here', 'password': 'password_here', 'whitelist': ['your_id'], 'prefix': 'prefix_here', 'mentionmsg': 'mentionmsg_here', 'invite': 'invite_here', 'mentionmode': 'mentionmode_here'}, settings, indent=4, sort_keys=True, separators=(',', ' : '))
        settings = None

with open("settings.json", "r") as settings_file:
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
    for key in settings:
        if "_here" in key:
            if not asked:
                asked = True
                print("First time setup, prepare your anus for some questions.")
                email = input("What's your Discord email address?\n")
                password = input("What's your Discord password?\n")
                prefix = input("What should your prefix be?\n")
                mentionmsg = input("What should you respond when you get mentioned? Type None to not respond.\n")
                mentionmode = input("Do you want the message that the bot sends to look legit (waits 2 secs, sends typing for 2 secs, sends message)\nOr would you like it to be fast (just send the message) (choose from legit/fast)\n")
                invite = input("What's the permanent invite link for you Discord server? Type None if you don't have one.\n")
                settings['email'] = email
                settings['password'] = password
                settings['prefix'] = prefix
                settings['mentionmsg'] = mentionmsg
                settings['invite'] = invite
                settings['mentionmode'] = mentionmode
                bot = commands.Bot(command_prefix=prefix, description=description)
                settings_file = None
                with open("settings.json", "w") as settings_file:
                    json.dump(settings, settings_file, indent=4, sort_keys=True, separators=(',', ' : '))
                print("You're all set! Bot is starting")
    
@bot.event
async def on_ready():
    print("\nSTARTED\n")
    if "your_id" in whitelist:
        id = bot.user.id
        settings['whitelist'].remove("your_id")
        settings['whitelist'].append(id)
        save_settings()
    if not os.path.exists("folders"):
        os.makedirs("folders")
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
        await say(msgchan, "All commands can be found here:\n<https://github.com/PlanetTeamSpeakk/DiscordSelfBot#commands>")
            
    elif await command(message, "restart", True):
        await say(msgchan, "Restarting...")
        bot.run(email, password)

    elif await command(message, "boobs", True):
        author = message.author
        try:
            rdm = random.randint(0, 10219)      
            search = ("http://api.oboobs.ru/boobs/{}".format(rdm))
            async with aiohttp.get(search) as r:
                result = await r.json()
                boob = random.choice(result)
                boob = "http://media.oboobs.ru/{}".format(boob["preview"])
        except Exception as e:
            await say(msgchan, "{} ` Error getting results.`".format(author.mention))
            return
        await say(msgchan, "{}".format(boob))
        
    elif await command(message, "ass", True):
        author = message.author
        try:
            rdm = random.randint(0, 10219)      
            search = ("http://api.obutts.ru/boobs/{}".format(rdm))
            async with aiohttp.get(search) as r:
                result = await r.json()
                butt = random.choice(result)
                butt = "http://media.obutts.ru/{}".format(but["preview"])
        except Exception as e:
            await say(msgchan, "{} ` Error getting results.`".format(author.mention))
            return
        await say(msgchan, "{}".format(butt))
    
    elif await command(message, "say ", True):
        await say(msgchan, message.content[len(prefix + "say "):])
    
    elif await command(message, "server owner", True):
        await say(msgchan, embed=discord.Embed(title="Server owner", description="{}, the server owner is {}.".format(message.author.mention, message.server.owner.mention), colour=0X008CFF))
        
    elif await command(message, "server name", True):
        await say(msgchan, embed=discord.Embed(title="Server name", description="{}, the server name is {}.".format(message.author.mention, message.server), colour=0X008CFF))
		
    elif await command(message, "server sid", True):
        await say(msgchan, embed=discord.Embed(title="Server ID", description="{}, the Server ID is {}.".format(message.author.mention, message.server.id), colour=0X008CFF))
        
    elif await command(message, "server channelname", True):
        await say(msgchan, embed=discord.Embed(title="Channel name", description="{}, the channelname is #{}.".format(message.author.mention, message.channel.name), colour=0X008CFF))
		
    elif await command(message, "server cid", True):
        await say(msgchan, embed=discord.Embed(title="Channel ID", description="{}, the Channel ID is {}.".format(message.author.mention, message.channel.id), colour=0X008CFF))
        
    elif await command(message, "server time", True):
        await say(msgchan, embed=discord.Embed(title="Server time", description="{}, the server time is {}.".format(message.author.mention, datetime.datetime.now()), colour=0X008CFF))
        
    elif await command(message, "server roles", True):
        await say(msgchan, embed=discord.Embed(title="Roles", description="{}, the current roles are \n{}.".format(message.author.mention, ", ".join([r.name for r in message.server.role_hierarchy])), colour=0X008CFF))

    elif await command(message, "server emojis", True):
        comma = ", "
        emojis = [e.name for e in message.server.emojis]
        await say(msgchan, embed=discord.Embed(title="Emojis", description="{}, the current emojis are \n{}.".format(message.author.mention, comma.join(emojis)), colour=0X008CFF))
            
    elif await command(message, "server users", True):
        comma = "**, **"
        members = [m.name for m in message.server.members]
        if len(message.server.members) < 32:
            await say(msgchan, embed=discord.Embed(title="Users", description="{}, the current users are \n**{}**.".format(message.author.mention, comma.join(members)), colour=0X008CFF))
        else:
            await bot.send_message(message.author, embed=discord.Embed(title="Users", description="The current users in **{}** are \n**{}**.".format(message.server.name, comma.join(members)), colour=0X008CFF))
            
    elif await command(message, "server channels", True):
        comma = "**, **"
        voicechans = [x.name for x in message.server.channels if x.type == discord.ChannelType.voice]
        textchans = [x.name for x in message.server.channels if x.type == discord.ChannelType.text]
        await say(msgchan, embed=discord.Embed(title="Channels", description="{}, the current voice channels are \n**{}**.\nThe current text channels are\n**{}**.".format(message.author.mention, comma.join(voicechans), comma.join(textchans)), colour=0X008CFF))
			
    elif await command(message, "server compareids", True):
        if message.server.id == message.channel.id:
            await say(msgchan, embed=discord.Embed(title="Channel is default", description=
            "{}, the ids of the channel and the server are the same, so this is the default channel.\n(SID=`{}`, CID=`{}`)".format(message.author.mention, message.server.id, message.channel.id), colour=0X008CFF))
        else:
            await say(msgchan, embed=discord.Embed(title="Channel isn't default", description=
            "{}, The ids of the channel and the server are not the same, this is not the default channel. If there is a #general try it in that channel first.\n(SID=`{}`, CID=`{}`)".format(message.author.mention, message.server.id, message.channel.id), colour=0X008CFF))
            
    elif await command(message, "server icon", True):
        icon = message.server.icon_url
        embed = discord.Embed(title="Server icon", description="{}, the server icon is {}.".format(message.author.mention, icon), colour=0X008CFF)
        await say(msgchan, embed=embed)
        
    elif await command(message, "server info", True):
        members = set(message.server.members)
        offline = filter(lambda m: m.status is discord.Status.offline, members)
        offline = set(offline)
        bots = filter(lambda m: m.bot, members)
        bots = set(bots)
        users = members - bots
        servericon = message.server.icon_url
        channel_passed = (message.timestamp - message.channel.created_at).days 
        server_passed = (message.timestamp - message.server.created_at).days
        channel_created_at = ("Created on {} ({} days ago!)".format(message.channel.created_at.strftime("%d %b %Y %H:%M"), channel_passed))
        server_created_at = ("Created on {} ({} days ago!)".format(message.server.created_at.strftime("%d %b %Y %H:%M"), server_passed))
        try:
            em = discord.Embed(description="{}, here you go:".format(message.author.mention), color=0X008CFF, title="Server Info")
            em.set_thumbnail(url=servericon)
            em.add_field(name="Server Name", value=str(message.server.name))
            em.add_field(name="Server ID", value=str(message.server.id))
            em.add_field(name="Server Region", value=str(message.server.region))
            em.add_field(name="Server Verification", value=str(message.server.verification_level))
            em.add_field(name="Server Roles", value=str(len(message.server.roles) -1))
            em.add_field(name="Server Owner", value=str(message.server.owner.name))
            em.add_field(name="Server Created At", value=str(server_created_at))
            em.add_field(name="Owner ID", value=str(message.server.owner.id))
            em.add_field(name="Owner Nick", value=str(message.server.owner.nick))
            em.add_field(name="Owner Status", value=str(message.server.owner.status))
            em.add_field(name="Total Bots", value=str(len(bots)))
            em.add_field(name="Bots Online", value=str(len(bots - offline)))
            em.add_field(name="Bots Offline", value=str(len(bots & offline)))
            em.add_field(name="Total Users", value=str(len(users)))
            em.add_field(name="Online Users", value=str(len(users - offline)))
            em.add_field(name="Offline Users", value=str(len(users & offline)))
            em.add_field(name="Channel Name", value=str(message.channel.name))
            em.add_field(name="Channel ID", value=str(message.channel.id))
            em.add_field(name="Channel Default", value=str(message.channel.is_default))
            em.add_field(name="Channel Position", value=str(message.channel.position + 1))
            em.add_field(name="Channel Created At", value=str(channel_created_at))
            if message.channel.topic != None:
                em.add_field(name="Channel Topic", value=(message.channel.topic))
            else:
                pass
            await say(msgchan, embed=em)
        except discord.HTTPException:
            await say(msgchan, "An unknown error occured while sending the embedded message, maybe try giving me the `embed links` permission?")

    elif await command(message, "server channelinfo", True):
        channel = message.content[len(prefix + "server channelinfo "):]
        if channel == "":
            channel = message.channel
        else:
            channel = discord.utils.get(message.server.channels, name=channel)
        passed = (message.timestamp - channel.created_at).days
        try:
            channel_created_at = ("Created on {} ({} days ago!)".format(channel.created_at.strftime("%d %b %Y %H:%M"), passed))
            em = discord.Embed(description="{}, here you go:".format(message.author.mention), title="Channel Info", color=0X008CFF)
            em.add_field(name="Channel Name", value=str(channel.name))
            em.add_field(name="Channel ID", value=str(channel.id))
            em.add_field(name="Channel Default", value=str(channel.is_default))
            em.add_field(name="Channel Position", value=str(channel.position + 1))
            em.add_field(name="Channel Topic", value=(channel.topic))
            em.set_footer(text=channel_created_at)
            await say(msgchan, embed=em)
        except discord.HTTPException:
            channel_created_at = ("Created on {} ({} days ago!)".format(channel.created_at.strftime("%d %b %Y %H:%M"), passed))            
            em = discord.Embed(description="{}, here you go:".format(message.author.mention), title="Channel Info", color=0X008CFF)
            em.add_field(name="Channel Name", value=str(channel.name))
            em.add_field(name="Channel ID", value=str(channel.id))
            em.add_field(name="Channel Default", value=str(channel.is_default))
            em.add_field(name="Channel Position", value=str(channel.position + 1))
            em.add_field(name="Channel Topic", value="None")
            em.set_footer(text=channel_created_at)
            await say(msgchan, embed=em)
        
    elif await command(message, "server membercount", True):
        members = set(message.server.members)
        bots = filter(lambda m: m.bot, members)
        bots = set(bots)
        users = members - bots
        await say(msgchan, embed=discord.Embed(title="Server Membercount", description="{}, there are currently **{}** users and **{}** bots with a total of **{}** members in this server.".format(message.author.mention, len(users), len(bots), len(message.server.members)), colour=0X008CFF))
        
    elif await command(message, "server channelcount", True):
        chans = message.server.channels
        textchans = [x for x in message.server.channels if x.type == discord.ChannelType.text]
        voicechans = [x for x in message.server.channels if x.type == discord.ChannelType.voice]
        await say(msgchan, embed=discord.Embed(title="Server Channelcount", description="{}, there are currently **{}** text channels and **{}** voice channels with a total of **{}** channels in this server.".format(message.author.mention, len(textchans), len(voicechans), len(chans)), colour=0X008CFF))
            
    elif await command(message, "server rolecount", True):
        await say(msgchan, embed=discord.Embed(title="Server Rolecount", description="{}, there are currently **{}** roles in this server.".format(message.author.mention, len(message.server.role_hierarchy)), colour=0X008CFF))
        
    elif await command(message, "server emojicount", True):
        await say(msgchan, embed=discord.Embed(title="Server Emojicount", description="{}, there are currently **{}** emojis in this server.".format(message.author.mention, len(message.server.emojis)), colour=0X008CFF))
        
    elif await command(message, "server userinfo", True):
        user = message.content[len(prefix + "server userinfo "):]
        if user == "":
            user = message.author
        else:
            user = discord.utils.get(message.server.members, name=user)
        comma = ", "
        roles = [r.name for r in user.roles if r.name != "@everyone"]
        if roles:
            roles = sorted(roles, key=[x.name for x in message.server.role_hierarchy if x.name != "@everyone"].index)
            roles = comma.join(roles)
        else:
            roles = "None"

        em = discord.Embed(description="{} here you go:".format(
            message.author.mention), title="User Info", color=0X008CFF)
        if user.avatar_url:
            em.set_thumbnail(url=user.avatar_url)
        else:
            em.set_thumbnail(url=user.default_avatar_url)
        em.add_field(name="Name", value=user.name)
        em.add_field(name="Discriminator", value=user.discriminator)
        if user.nick:
            em.add_field(name="Nickname", value=user.nick)
        else:
            em.add_field(name="Nickname", value="None")
        em.add_field(name="ID", value=user.id)
        em.add_field(name="Status", value=user.status)
        if user.game:
            em.add_field(name="Playing", value=user.game)
        else:
            em.add_field(name="Playing", value="Nothing")
        em.add_field(name="Is AFK", value=user.is_afk)
        em.add_field(name="Is bot", value=user.bot)
        em.add_field(name="Highest role color", value=user.color)
        em.add_field(name="Serverwide muted", value=user.mute)
        em.add_field(name="Serverwide deafened", value=user.deaf)
        em.add_field(name="Joined discord at",
                     value=user.created_at.strftime("%d %b %Y %H:%M"))
        em.add_field(name="Joined server at",
                     value=user.joined_at.strftime("%d %b %Y %H:%M"))
        em.add_field(name="Roles", value=roles)

        await say(msgchan, embed=em)
        
    elif await command(message, "server roleinfo", True):
        role = message.content[len(prefix + "server roleinfo "):]
        roleObj = discord.utils.get(message.server.roles, name=role)
        if roleObj is None:
            await say(msgchan, "`{}` is not a valid role".format(role))
            return
        count = len([member for member in message.server.members if discord.utils.get(member.roles, name=roleObj.name)])
        perms = roleObj.permissions
        em = discord.Embed(description="{} here you go,".format(message.author.mention), title="Server Role Info", color=0X008CFF)
        em.add_field(name="Name", value=roleObj.name)
        em.add_field(name="Color", value=roleObj.color)
        em.add_field(name="Position", value=str(roleObj.position))
        em.add_field(name="User count", value=count)
        em.add_field(name="Mentionable", value=roleObj.mentionable)
        em.add_field(name="Display separately", value=roleObj.hoist)
        em.add_field(name="Administrator", value=perms.administrator)
        em.add_field(name="Can ban members", value=perms.ban_members)
        em.add_field(name="Can kick members", value=perms.kick_members)
        em.add_field(name="Can change nickname", value=perms.change_nickname)
        em.add_field(name="Can connect to voice channels", value=perms.connect)
        em.add_field(name="Can create instant invites", value=perms.create_instant_invite)
        em.add_field(name="Can deafen members", value=perms.deafen_members)
        em.add_field(name="Can embed links", value=perms.embed_links)
        em.add_field(name="Can use external emojis", value=perms.external_emojis)
        em.add_field(name="Can manage channel", value=perms.manage_channels)
        em.add_field(name="Can manage emojis", value=perms.manage_emojis)
        em.add_field(name="Can manage messages", value=perms.manage_messages)
        em.add_field(name="Can manage nicknames", value=perms.manage_nicknames)
        em.add_field(name="Can manage roles", value=perms.manage_roles)
        em.add_field(name="Can manage server", value=perms.manage_server)
        em.add_field(name="Can mention everyone", value=perms.mention_everyone)
        em.add_field(name="Can move members", value=perms.move_members)
        em.add_field(name="Can mute members", value=perms.mute_members)
        em.add_field(name="Can read message history", value=perms.read_message_history)
        em.add_field(name="Can send messages", value=perms.send_messages)
        em.add_field(name="Can speak", value=perms.speak)
        em.add_field(name="Can use voice activity", value=perms.use_voice_activation)
        em.add_field(name="Can manage webhooks", value=perms.manage_webhooks)
        em.add_field(name="Can add reactions", value=perms.add_reactions)
        await say(msgchan, embed=em)
    
    elif await command(message, "download ", True):
        url = message.content[len(prefix + "download "):]
        downloadmsg = await say(msgchan, "What's the file suffix?")
        await asyncio.sleep(0.2)
        suffix = await bot.wait_for_message(timeout=15, author=message.author)
        await bot.edit_message(downloadmsg, "Downloading...")
        if not "http://" in url:
            if not "https://" in url:
                if not "." in url:
                    await say(msgchan, "The given url is not in the correct format.\nA correct format would be `http://dank.website/file.suffix`.")
                else:
                    pass
            else:
                pass
        else:
            pass
        if not os.path.exists("folders/downloads"):
            os.makedirs("folders/downloads")
        async with aiohttp.get(url) as r:
            file = await r.content.read()
        fileloc = "folders/downloads/download{}.{}".format(random.randint(1000, 9999), suffix.content.lower())
        with open(fileloc, 'wb') as f:
            f.write(file)
        await bot.edit_message(downloadmsg, "File downloaded, look in the root folder.")
        
    elif await command(message, "mentionset ", True):
        new_mentionmsg = message.content[len(prefix + "mentionset "):]
        settings['mentionmsg'] = new_mentionmsg
        save_settings()
        await say(msgchan, "Mention message set!")
            
    elif await command(message, "mentionmode ", True):
        new_mentionmode = message.content[len(prefix + "mentionmode "):]
        settings['mentionmode'] = new_mentionmode
        save_settings()
        await say(msgchan, "Mentionmode set!")
            
    elif await command(message, "whitelist add ", True):
        id = message.content[len(prefix + "whitelist add "):]
        settings['whitelist'].append(id)
        with open("settings.json", "w") as settings_file:
            json.dump(settings, settings_file, indent=4, sort_keys=True, separators=(',', ' : '))
        await say(msgchan, "Added user to whitelist!")
        
    elif await command(message, "whitelist remove ", True):
        id = message.content[len(prefix + "whitelist remove "):]
        settings['whitelist'].remove(id)
        with open("settings.json", "w") as settings_file:
            json.dump(settings, settings_file, indent=4, sort_keys=True, separators=(',', ' : '))
        await say(msgchan, "Removed user from the whitelist!")
    
    elif await command(message, "lenny", False):
        if message.author.id == bot.user.id:
            await bot.edit_message(message, "( ͡° ͜ʖ ͡°)")
        else:
            await say(msgchan, "( ͡° ͜ʖ ͡°)")
      
    elif await command(message, "shrug", True):
        await say(msgchan, "¯\_(ツ)_/¯")
        
    elif await command(message, "shutdown", True):
        sys.exit("Bot got shutdown.")
        
    elif await command(message, "name ", True):
        name = message.content[len(prefix + "name "):]
        await bot.edit_profile(settings['password'], name=name)
        await say(msgchan, "Name set!")
        
    elif await command(message, "greentext ", False):
        text = message.content[len(prefix + "greentext "):]
        if message.author.id == bot.user.id:
            await bot.edit_message(message, "```css\n{}```".format(text))
        else:
            await say(msgchan, "```css\n{}```".format(text))
            
    elif await command(message, "orangetext ", False):
        text = message.content[len(prefix + "orangetext "):]
        if message.author.id == bot.user.id:
            await bot.edit_message(message, "```fix\n{}```".format(text))
        else:
            await say(msgchan, "```fix\n{}```".format(text))
            
    elif await command(message, "bluetext ", False):
        text = message.content[len(prefix + "bluetext "):].replace(" ", ".")
        if message.author.id == bot.user.id:
            await bot.edit_message(message, "```html\n<{}>```".format(text))
        else:
            await say(msgchan, "```html\n<{}>```".format(text))
    
    elif await command(message, "lmgtfy ", True):
        to_google = message.content[len(prefix + "lmgtfy "):]
        await say(msgchan, "http://lmgtfy.com/?q={}".format(to_google.replace(" ", "+")))
        
    elif await command(message, "navyseal", False):
        if message.author.id == bot.user.id:
            await bot.edit_message(message, "What the fuck did you just fucking say about me, you little bitch? I’ll have you know I graduated top of my class in the Navy Seals, and I’ve been involved in numerous secret raids on Al-Quaeda, and I have over 300 confirmed kills. I am trained in gorilla warfare and I’m the top sniper in the entire US armed forces. You are nothing to me but just another target. I will wipe you the fuck out with precision the likes of which has never been seen before on this Earth, mark my fucking words. You think you can get away with saying that shit to me over the Internet? Think again, fucker. As we speak I am contacting my secret network of spies across the USA and your IP is being traced right now so you better prepare for the storm, maggot. The storm that wipes out the pathetic little thing you call your life. You’re fucking dead, kid. I can be anywhere, anytime, and I can kill you in over seven hundred ways, and that’s just with my bare hands. Not only am I extensively trained in unarmed combat, but I have access to the entire arsenal of the United States Marine Corps and I will use it to its full extent to wipe your miserable ass off the face of the continent, you little shit. If only you could have known what unholy retribution your little “clever” comment was about to bring down upon you, maybe you would have held your fucking tongue. But you couldn’t, you didn’t, and now you’re paying the price, you goddamn idiot. I will shit fury all over you and you will drown in it. You’re fucking dead, kiddo.")
        else:
            await say(msgchan, "What the fuck did you just fucking say about me, you little bitch? I’ll have you know I graduated top of my class in the Navy Seals, and I’ve been involved in numerous secret raids on Al-Quaeda, and I have over 300 confirmed kills. I am trained in gorilla warfare and I’m the top sniper in the entire US armed forces. You are nothing to me but just another target. I will wipe you the fuck out with precision the likes of which has never been seen before on this Earth, mark my fucking words. You think you can get away with saying that shit to me over the Internet? Think again, fucker. As we speak I am contacting my secret network of spies across the USA and your IP is being traced right now so you better prepare for the storm, maggot. The storm that wipes out the pathetic little thing you call your life. You’re fucking dead, kid. I can be anywhere, anytime, and I can kill you in over seven hundred ways, and that’s just with my bare hands. Not only am I extensively trained in unarmed combat, but I have access to the entire arsenal of the United States Marine Corps and I will use it to its full extent to wipe your miserable ass off the face of the continent, you little shit. If only you could have known what unholy retribution your little “clever” comment was about to bring down upon you, maybe you would have held your fucking tongue. But you couldn’t, you didn’t, and now you’re paying the price, you goddamn idiot. I will shit fury all over you and you will drown in it. You’re fucking dead, kiddo.")
    
    elif await command(message, "edgyshit", False):
        if message.author.id == bot.user.id:
            await bot.edit_message(message, ":syringe::knife: :syringe::knife::syringe::knife:edgy shit edgY sHit :knife:thats :gun:some edgy:syringe::syringe: shit right :knife:th:knife: ere:syringe::syringe::syringe: right there :smoking::smoking:if i do ƽaү so my selｆ :gun:i say so :gun: thats what im talking about right there right there (chorus: ʳᶦᵍʰᵗ ᵗʰᵉʳᵉ) mMMMMᎷМ:gun: :knife::knife::knife:НO0ОଠＯOOＯOОଠଠOoooᵒᵒᵒᵒᵒᵒᵒᵒᵒ:knife::knife::knife: :gun: :syringe::syringe: :knife::knife: Edgy shit")
        else:
            await say(msgchan, ":syringe::knife: :syringe::knife::syringe::knife:edgy shit edgY sHit :knife:thats :gun:some edgy:syringe::syringe: shit right :knife:th:knife: ere:syringe::syringe::syringe: right there :smoking::smoking:if i do ƽaү so my selｆ :gun:i say so :gun: thats what im talking about right there right there (chorus: ʳᶦᵍʰᵗ ᵗʰᵉʳᵉ) mMMMMᎷМ:gun: :knife::knife::knife:НO0ОଠＯOOＯOОଠଠOoooᵒᵒᵒᵒᵒᵒᵒᵒᵒ:knife::knife::knife: :gun: :syringe::syringe: :knife::knife: Edgy shit")
    
    elif await command(message, "goodshit", False):
        if message.author.id == bot.user.id:
            await bot.edit_message(message, "sign me the FUCK up :ok_hand::eyes::ok_hand::eyes::ok_hand::eyes::ok_hand::eyes::ok_hand::eyes: good shit go౦ԁ sHit:ok_hand: thats :heavy_check_mark: some good:ok_hand::ok_hand:shit right:ok_hand::ok_hand:there:ok_hand::ok_hand::ok_hand: right:heavy_check_mark:there :heavy_check_mark::heavy_check_mark:if i do ƽaү so my  :100: i say so :100: thats what im talking about right there right there (chorus: ʳᶦᵍʰᵗ ᵗʰᵉʳᵉ) mMMMMᎷМ:100: :ok_hand::ok_hand: :ok_hand:НO0ОଠOOOOOОଠଠOoooᵒᵒᵒᵒᵒᵒᵒᵒᵒ:ok_hand: :ok_hand::ok_hand: :ok_hand: :100: :ok_hand: :eyes: :eyes: :eyes: :ok_hand::ok_hand:Good shit")
        else:
            await say(msgchan, "sign me the FUCK up :ok_hand::eyes::ok_hand::eyes::ok_hand::eyes::ok_hand::eyes::ok_hand::eyes: good shit go౦ԁ sHit:ok_hand: thats :heavy_check_mark: some good:ok_hand::ok_hand:shit right:ok_hand::ok_hand:there:ok_hand::ok_hand::ok_hand: right:heavy_check_mark:there :heavy_check_mark::heavy_check_mark:if i do ƽaү so my  :100: i say so :100: thats what im talking about right there right there (chorus: ʳᶦᵍʰᵗ ᵗʰᵉʳᵉ) mMMMMᎷМ:100: :ok_hand::ok_hand: :ok_hand:НO0ОଠOOOOOОଠଠOoooᵒᵒᵒᵒᵒᵒᵒᵒᵒ:ok_hand: :ok_hand::ok_hand: :ok_hand: :100: :ok_hand: :eyes: :eyes: :eyes: :ok_hand::ok_hand:Good shit")
    
    elif await command(message, "appache", False):
        if message.author.id == bot.user.id:
            await bot.edit_message(message, "I sexually Identify as an Attack Helicopter. Ever since I was a boy I dreamed of soaring over the oilfields dropping hot sticky loads on disgusting foreigners. People say to me that a person being a helicopter is Impossible and I’m fucking retarded but I don’t care, I’m beautiful. I’m having a plastic surgeon install rotary blades, 30 mm cannons and AMG-114 Hellfire missiles on my body. From now on I want you guys to call me “Apache” and respect my right to kill from above and kill needlessly. If you can’t accept me you’re a heliphobe and need to check your vehicle privilege. Thank you for being so understanding.")
        else:
            await say(msgchan, "I sexually Identify as an Attack Helicopter. Ever since I was a boy I dreamed of soaring over the oilfields dropping hot sticky loads on disgusting foreigners. People say to me that a person being a helicopter is Impossible and I’m fucking retarded but I don’t care, I’m beautiful. I’m having a plastic surgeon install rotary blades, 30 mm cannons and AMG-114 Hellfire missiles on my body. From now on I want you guys to call me “Apache” and respect my right to kill from above and kill needlessly. If you can’t accept me you’re a heliphobe and need to check your vehicle privilege. Thank you for being so understanding.")
    
    elif await command(message, "daddy", False):
        if message.author.id == bot.user.id:
            await bot.edit_message(message, "Just me and my :two_hearts:daddy:two_hearts:, hanging out I got pretty hungry:eggplant: so I started to pout :disappointed: He asked if I was down :arrow_down:for something yummy :heart_eyes::eggplant: and I asked what and he said he'd give me his :sweat_drops:cummies!:sweat_drops: Yeah! Yeah!:two_hearts::sweat_drops: I drink them!:sweat_drops: I slurp them!:sweat_drops: I swallow them whole:sweat_drops: :heart_eyes: It makes :cupid:daddy:cupid: :blush:happy:blush: so it's my only goal... :two_hearts::sweat_drops::tired_face:Harder daddy! Harder daddy! :tired_face::sweat_drops::two_hearts: 1 cummy:sweat_drops:, 2 cummy:sweat_drops::sweat_drops:, 3 cummy:sweat_drops::sweat_drops::sweat_drops:, 4:sweat_drops::sweat_drops::sweat_drops::sweat_drops: I'm :cupid:daddy's:cupid: :crown:princess :crown:but I'm also a whore! :heart_decoration: He makes me feel squishy:heartpulse:!He makes me feel good:purple_heart:! :cupid::cupid::cupid:He makes me feel everything a little should!~ :cupid::cupid::cupid: :crown::sweat_drops::cupid:Wa-What!:cupid::sweat_drops::crown:")
        else:
            await say(msgchan, "Just me and my :two_hearts:daddy:two_hearts:, hanging out I got pretty hungry:eggplant: so I started to pout :disappointed: He asked if I was down :arrow_down:for something yummy :heart_eyes::eggplant: and I asked what and he said he'd give me his :sweat_drops:cummies!:sweat_drops: Yeah! Yeah!:two_hearts::sweat_drops: I drink them!:sweat_drops: I slurp them!:sweat_drops: I swallow them whole:sweat_drops: :heart_eyes: It makes :cupid:daddy:cupid: :blush:happy:blush: so it's my only goal... :two_hearts::sweat_drops::tired_face:Harder daddy! Harder daddy! :tired_face::sweat_drops::two_hearts: 1 cummy:sweat_drops:, 2 cummy:sweat_drops::sweat_drops:, 3 cummy:sweat_drops::sweat_drops::sweat_drops:, 4:sweat_drops::sweat_drops::sweat_drops::sweat_drops: I'm :cupid:daddy's:cupid: :crown:princess :crown:but I'm also a whore! :heart_decoration: He makes me feel squishy:heartpulse:!He makes me feel good:purple_heart:! :cupid::cupid::cupid:He makes me feel everything a little should!~ :cupid::cupid::cupid: :crown::sweat_drops::cupid:Wa-What!:cupid::sweat_drops::crown:")
    
    elif await command(message, "4chan", False):
        if message.author.id == bot.user.id:
            await bot.edit_message(message, "Fresh off the boat, from reddit, kid? heh I remember when I was just like you. Braindead. Lemme give you a tip so you can make it in this cyber sanctuary: never make jokes like that. You got no reputation here, you got no name, you got jackshit here. It's survival of the fittest and you ain't gonna survive long on 4chan by saying stupid jokes that your little hugbox cuntsucking reddit friends would upboat. None of that here. You don't upboat. You don't downboat. This ain't reddit, kid. This is 4chan. We have REAL intellectual discussion, something I don't think you're all that familiar with. You don't like it, you can hit the bricks on over to imgur, you daily show watching son of a bitch. I hope you don't tho. I hope you stay here and learn our ways. Things are different here, unlike any other place that the light of internet pop culture reaches. You can be anything here. Me ? heh, I'm a judge.. this place.... this place has a lot to offer... heh you'll see, kid . . . that is if you can handle it.")
        else:
            await say(msgchan, "Fresh off the boat, from reddit, kid? heh I remember when I was just like you. Braindead. Lemme give you a tip so you can make it in this cyber sanctuary: never make jokes like that. You got no reputation here, you got no name, you got jackshit here. It's survival of the fittest and you ain't gonna survive long on 4chan by saying stupid jokes that your little hugbox cuntsucking reddit friends would upboat. None of that here. You don't upboat. You don't downboat. This ain't reddit, kid. This is 4chan. We have REAL intellectual discussion, something I don't think you're all that familiar with. You don't like it, you can hit the bricks on over to imgur, you daily show watching son of a bitch. I hope you don't tho. I hope you stay here and learn our ways. Things are different here, unlike any other place that the light of internet pop culture reaches. You can be anything here. Me ? heh, I'm a judge.. this place.... this place has a lot to offer... heh you'll see, kid . . . that is if you can handle it.")
    
    elif await command(message, "discorole ", True):
        await say(msgchan, "How many times do you want it to change?")
        await asyncio.sleep(0.2)
        times = await bot.wait_for_message(timeout=15, author=message.author)
        times = int(times.content)
        await say(msgchan, "What should the interval be?")
        await asyncio.sleep(0.2)
        interval = await bot.wait_for_message(timeout=15, author=message.author)
        interval = int(interval.content)
        role = message.content[len(prefix + "discorole "):]
        roleObj = discord.utils.find(lambda r: r.name == role, message.server.roles)
        if not roleObj:
            await say(msgchan, "`{}` is not a valid role".format(role))
            return
        if interval < 2:
            interval = 2
        time = 0
        while time < times:
            colour = ''.join([random.choice('0123456789ABCDEF') for x in range(6)])
            colour = int(colour, 16)
            await bot.edit_role(message.server, roleObj, colour=discord.Colour(value=colour))
            time = time + 1
            await asyncio.sleep(interval)
            
    elif await command(message, "discoroleforever ", True):
        await say(msgchan, "What should the interval be?")
        await asyncio.sleep(0.2)
        interval = await bot.wait_for_message(timeout=15, author=message.author)
        interval = int(interval.content)
        role = message.content[len(prefix + "discoroleforever "):]
        roleObj = discord.utils.find(lambda r: r.name == role, message.server.roles)
        if not roleObj:
            await say(msgchan, "`{}` is not a valid role".format(role))
            return
        if interval < 2:
            interval = 2
        while True:
            colour = ''.join([random.choice('0123456789ABCDEF') for x in range(6)])
            colour = int(colour, 16)
            await bot.edit_role(message.server, roleObj, colour=discord.Colour(value=colour))
            await asyncio.sleep(interval)
    
    elif await command(message, "triggered", True):
        await say(msgchan, "http://i.imgur.com/zSddfUe.gif")
        
    elif await command(message, "setprefix ", True):
        new_prefix = message.content[len(prefix + "setprefix "):]
        settings['prefix'] = new_prefix
        save_settings()
        await say(msgchan, "Prefix set! Restart the bot for the changes to take affect.")
    
    elif await command(message, "flirting101", True):
        await say(msgchan, "Hey, sorry I saw your profile and I just thought you looked cute in your picture, I really wanted to tell you that)) It's really rare to see girls playing video games haha! I don't know why its a guy thing honestly im like really against misogyny and like ill be the one in the kitchen making sandwiches. We should really play l4d2 sometime its a really cool zombie game with a lot of scary moments, but don't worry ill be there to protect you :wink: sorry that wasnt flirting I swear Im just trying to be friendly I really like your profile picture sorry was that too far? Really sorry i'm really shy I don't go out much haha add me on skype we should talk more you look really nice and fun xxx")
    
    elif await command(message, "setinvite ", True):
        invite = message.content[len(prefix + "setinvite "):]
        settings['invite'] = invite
        save_settings()
        
    elif await command(message, "spaminvite ", True):
        invite = settings['invite']
        if invite is "None":
            await say(msgchan, "You haven't set an invite link, set one with {}setinvite <invite>".format(prefix))
        times = int(message.content[len(prefix + "spaminvite "):])
        time = 0
        while time < times:
            time = time + 1
            await say(msgchan, invite)
  
    elif await command(message, "spaminvitedm ", True):
        msg = " " + message.content[len(prefix + "spaminvitedm "):]
        invite = settings['invite']
        dont_send = []
        dont_send_roles = []
        for role in message.server.roles:
            if role.permissions.kick_members:
                dont_send_roles.append(role)
        for role in dont_send_roles:
            for member in message.server.members:
                if role in member.roles:
                    dont_send.append(member)
        sent = 0
        members = []
        if not os.path.exists("sent_list.json"):
            with open("sent_list.json", "w") as sent_list_json:
                json.dump([], sent_list_json, indent=4, sort_keys=True, separators=(',', ' : '))
                sent_list_json = None
        with open("sent_list.json", "r") as sent_list_json:
            sent_list = json.load(sent_list_json)
            sent_list_json = None
        for member in message.server.members:
            members.append(member)
        for member in members:
            try:
                if member not in dont_send:
                    if member.id not in sent_list:
                        await bot.send_message(member, invite + msg)
                        sent = sent + 1
                        sent_list.append(member.id)
                        print("Sent an invite to {} people.".format(sent))
                        await asyncio.sleep(60) # There you go Nathan, happy now?
            except:
                pass
            with open("sent_list.json", "w") as sent_list_json:
                json.dump(sent_list, sent_list_json, indent=4, sort_keys=True, separators=(',', ' : '))
                sent_list_json = None
            
    elif await command(message, "discrim ", True):
        discriminator = message.content[len(prefix + "discrim "):].replace("#", "")
        if not discriminator.isdigit():
            await say(msgchan, "A Discrimnator can only have digits and a #\nExamples\n`#4157`, `4157`")
            return
        members = [str(s) for s in list(bot.get_all_members()) if s.discriminator == discriminator]
        members = ", ".join(list(set(members)))
        if not members:
            await say(msgchan, "I could not find any users in any of the servers I'm in with a discriminator of `{}`".format(discriminator))
            return
        else:
            embed = discord.Embed(colour=0X00B6FF)
            embed.add_field(name="Discriminator #{}".format(discriminator), value=str(members), inline=False)
            try:
                await say(msgchan, embed=embed)
            except:
                await say(msgchan, "An unknown error occured while embedding.")
            
    elif await command(message, "emoteurl ", True):
        emote = message.content[len(prefix + "emoteulr "):]
        emote = discord.utils.find(lambda e: e.name == emote, message.server.emojis)
        await say(msgchan, emote.url)
        
    elif await command(message, "genbotoauth ", True):
        oauth_bot = message.content[len(prefix + "genbotoauth "):]
        oauth_bot = discord.utils.find(lambda m: m.name == oauth_bot, message.server.members)
        url = discord.utils.oauth_url(oauth_bot.id)
        await say(msgchan, "What perms should the invite have? \nFor help you can goto https://discordapi.com/permissions.html. Or just put 'all', 'admin' or 'None'.\nDoesn't always work")
        await asyncio.sleep(0.2)
        perms = await bot.wait_for_message(timeout=15, author=message.author)
        if not oauth_bot.bot:
            await say(msgchan, "User is not a bot.")
            return
        if perms.content.lower() == "all":
            await say(msgchan, ""
            "{}, here you go:\n"
            "{}&permissions=-1".format(message.author.mention, url))
        elif perms.content.lower() == "admin":
            await say(msgchan, ""
            "{}, here you go:\n"
            "{}&permissions=8".format(message.author.mention, url))
        elif perms.content.lower() == "none":
            await say(msgchan, ""
            "{}, here you go:\n"
            "{}".format(message.author.mention, url))
        elif perms.content:
            await say(msgchan, ""
            "{}, here you go:\n"
            "{}&permissions={}".format(message.author.mention, url, perms.content))
            
    elif await command(message, "genoauth ", True):
        oauth_bot = message.content[len(prefix + "genoauth "):]
        url = discord.utils.oauth_url(oauth_bot)
        await say(msgchan, "What perms should the invite have? \nFor help you can goto https://discordapi.com/permissions.html. Or just put 'all', 'admin' or 'None'.\nDoesn't always work")
        await asyncio.sleep(0.2)
        perms = await bot.wait_for_message(timeout=15, author=message.author)
        if perms.content.lower() == "all":
            await say(msgchan, ""
            "{}, here you go:\n"
            "{}&permissions=-1".format(message.author.mention, url))
        elif perms.content.lower() == "admin":
            await say(msgchan, ""
            "{}, here you go:\n"
            "{}&permissions=8".format(message.author.mention, url))
        elif perms.content.lower() == "none":
            await say(msgchan, ""
            "{}, here you go:\n"
            "{}".format(message.author.mention, url))
        elif perms.content:
            await say(msgchan, ""
            "{}, here you go:\n"
            "{}&permissions={}".format(message.author.mention, url, perms.content))
            
    elif await command(message, "calc ", True):
        prob = re.sub("[^0-9+-/* ]", "", message.content[len(prefix + "calc "):])
        try:
            answer = str(eval(prob))
            await say(msgchan, "`{}` = `{}`".format(prob, answer))
        except:
            await say(msgchan, "I couldn't solve that problem, it's too hard")
        
    elif await command(message, "avatar ", True):
        user = message.content[len(prefix + "avatar "):]
        user = discord.utils.get(message.server.members, name=user)
        if user.avatar_url:
            avatar = user.avatar_url
        else:
            avatar = user.default_avatar_url
        em = discord.Embed(color=discord.Color.red())
        em.add_field(name=user.mention + "'s avatar", value=avatar)
        em.set_image(url=avatar)
        await say(msgchan, embed=em)
        
    elif await command(message, "ascii ", False):
        text = message.content[len(prefix + "ascii "):]
        msg = str(figlet_format(text, font='cybermedium'))
        if msg[0] == " ":
            msg = "." + msg[1:]
        error = figlet_format('LOL, that\'s a bit too long.',
                              font='cybermedium')
        if len(msg) > 2000:
            if message.author.id == bot.user.id:
                await bot.edit_message(message, "```fix\n{}```".format(error))
            else:
                await say(msgchan, box(error))
        else:
            if message.author.id == bot.user.id:
                await bot.edit_message(message, "```fix\n{}```".format(msg))
            else:
                await say(msgchan, "```fix\n{}```".format(msg))
        
    elif await command(message, "convert ", True):
        file_url = message.content[len(prefix + "convert "):]
        await say(msgchan, "What is the output format?")
        await asyncio.sleep(0.2)
        output_format = await bot.wait_for_message(timeout=15, author=message.author)
        if output_format is None:
            await say(msgchan, "K then not.")
            return
        convertmsg = await say(msgchan, "Setting up...")
        # The copy of rickrolled part.
        if file_url == "rickrolled":
            file_url = "https://raw.githubusercontent.com/PlanetTeamSpeakk/PTSCogs-attributes/master/rickrolled.ogg"
            meme = True
            number = 'rickrolled_' + ''.join([random.choice('0123456789') for x in range(6)])
            if output_format == "rick astley":
                input_format = "ogg"
                output_format = "mp3"
        # The copy of We are number one part.
        elif file_url == "lazytown":
            meme = True
            file_url = "https://raw.githubusercontent.com/PlanetTeamSpeakk/PTSCogs-attributes/master/numberone.ogg"
            number = 'numberone_' + ''.join([random.choice('0123456789') for x in range(6)])
            if output_format == "number one":
                input_format = "ogg"
                output_format = "mp3"
        else:
            meme = False
            number = ''.join([random.choice('0123456789') for x in range(6)])
        if meme is False:
            form_found = False
            for i in range(6):
                if file_url[len(file_url) - i:].startswith("."):
                    input_format = file_url[len(file_url) - i:]
                    form_found = True
                else:
                    if form_found is not True:
                        form_found = False
            if form_found is not True:
                await bot.edit_message(convertmsg, "Your link is corrupt, it should end with something like .mp3, .mp4, .png, etc.")
                print(form_found)
                return
        if not os.path.exists("folders/converter"):
            os.makedirs("folders/converter")
        input = "folders/converter/{}.{}".format(number, input_format)
        output = "folders/converter/{}.{}".format(number, output_format.content)
        outputname = "{}.{}".format(number, output_format.content)
        await bot.edit_message(convertmsg, "Downloading...")
        try:
            async with aiohttp.get(file_url) as r:
                file = await r.content.read()
            with open(input, 'wb') as f:
                f.write(file)
        except:
            await bot.edit_message(convertmsg, "Could not download the file.")
            try:
                os.remove(input)
            except:
                pass
            return
        try:
            converter = ffmpy.FFmpeg(inputs={input: "-y"}, outputs={output: "-y"})
            await bot.edit_message(convertmsg, "Converting...")
            converter.run()
        except:
            await bot.edit_message(convertmsg, "Could not convert your file, an error occured.")
            try:
                os.remove(input)
                os.remove(output)
            except:
                pass
            return
        await bot.send_file(message.channel, content="Convertion done!", fp=output, filename=outputname)
        await bot.delete_message(convertmsg)
        os.remove(input)
        os.remove(output)
        
    elif await command(message, "penis", True):
        user = message.content[len(prefix + "penis "):]
        if user is "":
            user = message.author
        else:
            user = discord.utils.get(message.server.members, name=user)
        random.seed(user.id)
        psize = "8" + "="*random.randint(0, 30) + "D"
        await say(msgchan, "{} penis size: {}".format(user.mention, psize))
        
    elif await command(message, "shorten ", True):
        url = message.content[len(prefix + "shorten "):]
        shorten = shortener('Bitly', bitly_token='dd800abec74d5b12906b754c630cdf1451aea9e0')
        if not url == "":
            await say(msgchan, "{}, here you go <{}>.".format(message.author.mention, shorten.short(url)))
        else:
            await say(msgchan, "You think I can short an empty string for you? That's not gonna work.")
            
    elif await command(message, "ping", True):
        t1 = perf_counter()
        await bot.send_typing(message.channel)
        t2 = perf_counter()
        await say(msgchan, "Pong! Response time was **{}** seconds.".format(float(t2 - t1)))
            
    elif await command(message, "qrcode ", True):
        link = message.content[len(prefix + "qrcode "):]
        if link == "":
            await say(msgchan, "I can't make a qrcode of an empty string can I?")
            return
        else:
            shorten = shortener('Bitly', bitly_token='dd800abec74d5b12906b754c630cdf1451aea9e0')
            short_link = shorten.short(link)
        if not os.path.exists("folders/qrcodes"):
            os.makedirs("folders/qrcodes")
        async with aiohttp.get(shorten.qrcode(width=128, height=128)) as r:
            file = await r.content.read()
        number = random.randint(1000, 9999)
        fileloc = "folders/qrcodes/qrcode{}.png".format(number)
        with open(fileloc, 'wb') as f:
            f.write(file)
            file = None
            f = None
        await bot.send_file(msgchan, fp="folders/qrcodes/qrcode{}.png".format(number), filename="qrcode{}.png".format(number))
        os.remove("folders/qrcodes/qrcode{}.png".format(number))
            
    else:
        if message.content.startswith(prefix):
            if message.author.id in whitelist:
                await say(msgchan, "The command you entered was not found, type {}help for help.".format(prefix))
            
    for person in message.mentions:
        if mentionmsg != "None":
            if person.id == bot.user.id:
                if mentionmode == "legit":
                    await asyncio.sleep(2)
                    await bot.send_typing(message.channel)
                    await asyncio.sleep(2)
                    await say(msgchan, mentionmsg)
                elif mentionmode == "fast":
                    await say(msgchan, mentionmsg)
                    
async def command(message, cmd, del_msg):
    if message.content.startswith(prefix + cmd):
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
        elif message.author.id == "96987941519237120":
            if del_msg:
                try:
                    await bot.delete_message(message)
                except:
                    pass
            return True
        else:
            return False
    else:
        return False
        
def save_settings():
    with open("settings.json", "w") as settings_file:
        json.dump(settings, settings_file, indent=4, sort_keys=True, separators=(',', ' : '))
    reload_settings()
    
def reload_settings():
    settings = None
    with open("settings.json", "r") as settings_file:
        settings = json.load(settings_file)
        email = settings['email']
        password = settings['password']
        prefix = settings['prefix']
        whitelist = settings['whitelist']
        mentionmsg = settings['mentionmsg']
        invite = settings['invite']
        mentionmode = settings['mentionmode']
        settings_file = None
        
async def say(channel, message):
    await bot.send_message(channel, message)
        
bot.run(email, password)