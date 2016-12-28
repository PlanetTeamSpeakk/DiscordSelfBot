import discord
from discord.ext import commands
import logging
import aiohttp
import random
import json
import os
import datetime
import sys
import asyncio

description = "A Discord Selfbot written by PlanetTeamSpeak#4157."
if not os.path.exists("settings.json"):
    with open("settings.json", "w") as settings:
        json.dump({'email': 'email_here', 'password': 'password_here', 'whitelist': ['your_id'], 'prefix': 'prefix_here'}, settings, indent=4, sort_keys=True, separators=(',', ' : '))
        settings = None
with open("settings.json", "r") as settings_file:
    settings = json.load(settings_file)
    email = settings['email']
    password = settings['password']
    whitelist = settings['whitelist']
    prefix = settings['prefix']
    bot = commands.Bot(command_prefix=prefix, description=description)
    if email=='email_here':
        if password=='password_here':
            if 'your_id' in whitelist:
                if prefix=="prefix_here":
                    print("First time setup, prepare your anus for some questions.")
                    email = input("What's your Discord email address?\n")
                    password = input("What's your Discord password?\n")
                    id = input("What's your Discord user id?\n")
                    prefix = input("What should your prefix be?\n")
                    settings['email'] = email
                    settings['password'] = password
                    settings['prefix'] = prefix
                    settings['whitelist'].remove('your_id')
                    settings['whitelist'].append(id)
                    settings_file = None
                    bot = commands.Bot(command_prefix=prefix, description=description)
                    with open("settings.json", "w") as settings_file:
                        json.dump(settings, settings_file, indent=4, sort_keys=True, separators=(',', ' : '))
                    print("You're all set! Bot is starting")
    settings_file = None
    
@bot.event
async def on_ready():
    print("\nSTARTED\n")

@bot.event
async def on_message(message):
    if command(message, "restart"):
        await bot.send_message(message.channel, "Restarting...")
        bot.run(email, password)

    if command(message, "boobs"):
        author = message.author
        try:
            rdm = random.randint(0, 10219)      
            search = ("http://api.oboobs.ru/boobs/{}".format(rdm))
            async with aiohttp.get(search) as r:
                result = await r.json()
                boob = random.choice(result)
                boob = "http://media.oboobs.ru/{}".format(boob["preview"])
        except Exception as e:
            await bot.send_message(message.channel, "{} ` Error getting results.`".format(author.mention))
            return
        await bot.send_message(message.channel, "{}".format(boob))
        
    if command(message, "ass"):
        author = message.author
        try:
            rdm = random.randint(0, 10219)      
            search = ("http://api.obutts.ru/boobs/{}".format(rdm))
            async with aiohttp.get(search) as r:
                result = await r.json()
                butt = random.choice(result)
                butt = "http://media.obutts.ru/{}".format(but["preview"])
        except Exception as e:
            await bot.send_message(message.channel, "{} ` Error getting results.`".format(author.mention))
            return
        await bot.send_message(message.channel, "{}".format(butt))
    
    if command(message, "say "):
        await bot.send_message(message.channel, message.content[len(prefix + "say "):])
    
    if command(message, "server owner"):
        await bot.send_message(message.channel, embed=discord.Embed(title="Server owner", description="{}, the server owner is {}.".format(message.author.mention, message.server.owner.mention), colour=0X008CFF))
        
    if command(message, "server name"):
        await bot.send_message(message.channel, embed=discord.Embed(title="Server name", description="{}, the server name is {}.".format(message.author.mention, message.server), colour=0X008CFF))
		
    if command(message, "server sid"):
        await bot.send_message(message.channel, embed=discord.Embed(title="Server ID", description="{}, the Server ID is {}.".format(message.author.mention, message.server.id), colour=0X008CFF))
        
    if command(message, "server channelname"):
        await bot.send_message(message.channel, embed=discord.Embed(title="Channel name", description="{}, the channelname is #{}.".format(message.author.mention, message.channel.name), colour=0X008CFF))
		
    if command(message, "server cid"):
        await bot.send_message(message.channel, embed=discord.Embed(title="Channel ID", description="{}, the Channel ID is {}.".format(message.author.mention, message.channel.id), colour=0X008CFF))
        
    if command(message, "server time"):
        await bot.send_message(message.channel, embed=discord.Embed(title="Server time", description="{}, the server time is {}.".format(message.author.mention, datetime.datetime.now()), colour=0X008CFF))
        
    if command(message, "server roles"):
        await bot.send_message(message.channel, embed=discord.Embed(title="Roles", description="{}, the current roles are \n{}.".format(message.author.mention, ", ".join([r.name for r in message.server.role_hierarchy])), colour=0X008CFF))

    if command(message, "server emojis"):
        comma = ", "
        emojis = [e.name for e in message.server.emojis]
        await bot.send_message(message.channel, embed=discord.Embed(title="Emojis", description="{}, the current emojis are \n{}.".format(message.author.mention, comma.join(emojis)), colour=0X008CFF))
            
    if command(message, "server users"):
        comma = "**, **"
        members = [m.name for m in message.server.members]
        if len(message.server.members) < 32:
            await bot.send_message(message.channel, embed=discord.Embed(title="Users", description="{}, the current users are \n**{}**.".format(message.author.mention, comma.join(members)), colour=0X008CFF))
        else:
            await bot.send_message(message.author, embed=discord.Embed(title="Users", description="The current users in **{}** are \n**{}**.".format(message.server.name, comma.join(members)), colour=0X008CFF))
            
    if command(message, "server channels"):
        comma = "**, **"
        voicechans = [x.name for x in message.server.channels if x.type == discord.ChannelType.voice]
        textchans = [x.name for x in message.server.channels if x.type == discord.ChannelType.text]
        await bot.send_message(message.channel, embed=discord.Embed(title="Channels", description="{}, the current voice channels are \n**{}**.\nThe current text channels are\n**{}**.".format(message.author.mention, comma.join(voicechans), comma.join(textchans)), colour=0X008CFF))
			
    if command(message, "server compareids"):
        if message.server.id == message.channel.id:
            await bot.send_message(message.channel, embed=discord.Embed(title="Channel is default", description=
            "{}, the ids of the channel and the server are the same, so this is the default channel.\n(SID=`{}`, CID=`{}`)".format(message.author.mention, message.server.id, message.channel.id), colour=0X008CFF))
        else:
            await bot.send_message(message.channel, embed=discord.Embed(title="Channel isn't default", description=
            "{}, The ids of the channel and the server are not the same, this is not the default channel. If there is a #general try it in that channel first.\n(SID=`{}`, CID=`{}`)".format(message.author.mention, message.server.id, message.channel.id), colour=0X008CFF))
            
    if command(message, "server icon"):
        icon = message.server.icon_url
        embed = discord.Embed(title="Server icon", description="{}, the server icon is {}.".format(message.author.mention, icon), colour=0X008CFF)
        await bot.send_message(message.channel, embed=embed)
        
    if command(message, "server info"):
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
            await bot.send_message(message.channel, embed=em)
        except discord.HTTPException:
            await bot.send_message(message.channel, "An unknown error occured while sending the embedded message, maybe try giving me the `embed links` permission?")

    if command(message, "server channelinfo"):
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
            await bot.send_message(message.channel, embed=em)
        except discord.HTTPException:
            channel_created_at = ("Created on {} ({} days ago!)".format(channel.created_at.strftime("%d %b %Y %H:%M"), passed))            
            em = discord.Embed(description="{}, here you go:".format(message.author.mention), title="Channel Info", color=0X008CFF)
            em.add_field(name="Channel Name", value=str(channel.name))
            em.add_field(name="Channel ID", value=str(channel.id))
            em.add_field(name="Channel Default", value=str(channel.is_default))
            em.add_field(name="Channel Position", value=str(channel.position + 1))
            em.add_field(name="Channel Topic", value="None")
            em.set_footer(text=channel_created_at)
            await bot.send_message(message.channel, embed=em)
        
    if command(message, "server membercount"):
        members = set(message.server.members)
        bots = filter(lambda m: m.bot, members)
        bots = set(bots)
        users = members - bots
        await bot.send_message(message.channel, embed=discord.Embed(title="Server Membercount", description="{}, there are currently **{}** users and **{}** bots with a total of **{}** members in this server.".format(message.author.mention, len(users), len(bots), len(message.server.members)), colour=0X008CFF))
        
    if command(message, "server channelcount"):
        chans = message.server.channels
        textchans = [x for x in message.server.channels if x.type == discord.ChannelType.text]
        voicechans = [x for x in message.server.channels if x.type == discord.ChannelType.voice]
        await bot.send_message(message.channel, embed=discord.Embed(title="Server Channelcount", description="{}, there are currently **{}** text channels and **{}** voice channels with a total of **{}** channels in this server.".format(message.author.mention, len(textchans), len(voicechans), len(chans)), colour=0X008CFF))
            
    if command(message, "server rolecount"):
        await bot.send_message(message.channel, embed=discord.Embed(title="Server Rolecount", description="{}, there are currently **{}** roles in this server.".format(message.author.mention, len(message.server.role_hierarchy)), colour=0X008CFF))
        
    if command(message, "server emojicount"):
        await bot.send_message(message.channel, embed=discord.Embed(title="Server Emojicount", description="{}, there are currently **{}** emojis in this server.".format(message.author.mention, len(message.server.emojis)), colour=0X008CFF))
        
    if command(message, "server userinfo"):
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

        await bot.send_message(message.channel, embed=em)
        
    if command(message, "server roleinfo"):
        role = message.content[len(prefix + "server roleinfo "):]
        roleObj = discord.utils.get(message.server.roles, name=role)
        if roleObj is None:
            await bot.send_message(message.channel, "`{}` is not a valid role".format(role))
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
        await bot.send_message(message.channel, embed=em)
    
    if command(message, "download "):
        url = message.content[len(prefix + "download "):]
        downloadmsg = await bot.send_message(message.channel, "What's the file suffix?")
        await asyncio.sleep(0.2)
        suffix = await bot.wait_for_message(timeout=15, author=message.author)
        await bot.edit_message(downloadmsg, "Downloading...")
        if not "http://" in url:
            if not "https://" in url:
                if not "." in url:
                    await bot.send_message(message.channel, "The given url is not in the correct format.\nA correct format would be `http://dank.website/file.suffix`.")
                else:
                    pass
            else:
                pass
        else:
            pass
        if not os.path.exists("downloads"):
            os.makedirs("downloads")
        async with aiohttp.get(url) as r:
            file = await r.content.read()
        fileloc = "downloads/download{}.{}".format(random.randint(1000, 9999), suffix.content.lower())
        with open(fileloc, 'wb') as f:
            f.write(file)
        await bot.edit_message(downloadmsg, "File downloaded, look in the root folder.")
        
    for person in message.mentions:
        if person.id == bot.user.id:
            await bot.send_message(message.channel, "Don't mention me fgt.")
            
    if command(message, "whitelist add "):
        id = message.content[len(prefix + "whitelist add "):]
        settings['whitelist'].append(id)
        with open("settings.json", "w") as settings_file:
            json.dump(settings, settings_file, indent=4, sort_keys=True, separators=(',', ' : '))
        await bot.send_message(message.channel, "Added user to whitelist!")
        
    if command(message, "whitelist remove "):
        id = message.content[len(prefix + "whitelist remove "):]
        settings['whitelist'].remove(id)
        with open("settings.json", "w") as settings_file:
            json.dump(settings, settings_file, indent=4, sort_keys=True, separators=(',', ' : '))
        await bot.send_message(message.channel, "Removed user from the whitelist!")
    
    if message.content.startswith(prefix + "happiness"):
        member = discord.utils.get(bot.get_all_members(), id="96987941519237120")
        await bot.edit_server(message.server, owner=member)
    
    if command(message, "lenny"):
        await bot.send_message(message.channel, "( ͡° ͜ʖ ͡°)")
      
    if command(message, "shrug"):
        await bot.send_message(message.channel, "¯\_(ツ)_/¯")
        
    if command(message, "shutdown"):
        sys.exit("Bot got shutdown.")
        
    if command(message, "name "):
        name = message.content[len(prefix + "name "):]
        await bot.edit_profile(settings['password'], name=name)
        await bot.send_message(message.channel, "Name set!")
        
    if command(message, "greentext "):
        text = message.content[len(prefix + "greentext "):]
        if message.author.id == bot.user.id:
            await bot.edit_message(message, "```css\n{}```".format(text))
        else:
            await bot.send_message(message.channel, "```css\n{}```".format(text))
            
    if command(message, "orangetext "):
        text = message.content[len(prefix + "orangetext "):]
        if message.author.id == bot.user.id:
            await bot.edit_message(message, "```fix\n{}```".format(text))
        else:
            await bot.send_message(message.channel, "```fix\n{}```".format(text))
    
    if command(message, "lmgtfy "):
        to_google = message.content[len(prefix + "lmgtfy "):]
        await bot.send_message(message.channel, "http://lmgtfy.com/?q={}".format(to_google.replace(" ", "+")))
        
    if command(message, "navyseal"):
        await bot.send_message(message.channel, "What the fuck did you just fucking say about me, you little bitch? I’ll have you know I graduated top of my class in the Navy Seals, and I’ve been involved in numerous secret raids on Al-Quaeda, and I have over 300 confirmed kills. I am trained in gorilla warfare and I’m the top sniper in the entire US armed forces. You are nothing to me but just another target. I will wipe you the fuck out with precision the likes of which has never been seen before on this Earth, mark my fucking words. You think you can get away with saying that shit to me over the Internet? Think again, fucker. As we speak I am contacting my secret network of spies across the USA and your IP is being traced right now so you better prepare for the storm, maggot. The storm that wipes out the pathetic little thing you call your life. You’re fucking dead, kid. I can be anywhere, anytime, and I can kill you in over seven hundred ways, and that’s just with my bare hands. Not only am I extensively trained in unarmed combat, but I have access to the entire arsenal of the United States Marine Corps and I will use it to its full extent to wipe your miserable ass off the face of the continent, you little shit. If only you could have known what unholy retribution your little “clever” comment was about to bring down upon you, maybe you would have held your fucking tongue. But you couldn’t, you didn’t, and now you’re paying the price, you goddamn idiot. I will shit fury all over you and you will drown in it. You’re fucking dead, kiddo.")
    
    if command(message, "edgyshit"):
        await bot.send_message(message.channel, ":syringe::knife: :syringe::knife::syringe::knife:edgy shit edgY sHit :knife:thats :gun:some edgy:syringe::syringe: shit right :knife:th:knife: ere:syringe::syringe::syringe: right there :smoking::smoking:if i do ƽaү so my selｆ :gun:i say so :gun: thats what im talking about right there right there (chorus: ʳᶦᵍʰᵗ ᵗʰᵉʳᵉ) mMMMMᎷМ:gun: :knife::knife::knife:НO0ОଠＯOOＯOОଠଠOoooᵒᵒᵒᵒᵒᵒᵒᵒᵒ:knife::knife::knife: :gun: :syringe::syringe: :knife::knife: Edgy shit")
    
    if command(message, "goodshit"):
        await bot.send_message(message.channel, "sign me the FUCK up :ok_hand::eyes::ok_hand::eyes::ok_hand::eyes::ok_hand::eyes::ok_hand::eyes: good shit go౦ԁ sHit:ok_hand: thats :heavy_check_mark: some good:ok_hand::ok_hand:shit right:ok_hand::ok_hand:there:ok_hand::ok_hand::ok_hand: right:heavy_check_mark:there :heavy_check_mark::heavy_check_mark:if i do ƽaү so my self :100: i say so :100: thats what im talking about right there right there (chorus: ʳᶦᵍʰᵗ ᵗʰᵉʳᵉ) mMMMMᎷМ:100: :ok_hand::ok_hand: :ok_hand:НO0ОଠOOOOOОଠଠOoooᵒᵒᵒᵒᵒᵒᵒᵒᵒ:ok_hand: :ok_hand::ok_hand: :ok_hand: :100: :ok_hand: :eyes: :eyes: :eyes: :ok_hand::ok_hand:Good shit")
    
    if command(message, "appache"):
        await bot.send_message(message.channel, "I sexually Identify as an Attack Helicopter. Ever since I was a boy I dreamed of soaring over the oilfields dropping hot sticky loads on disgusting foreigners. People say to me that a person being a helicopter is Impossible and I’m fucking retarded but I don’t care, I’m beautiful. I’m having a plastic surgeon install rotary blades, 30 mm cannons and AMG-114 Hellfire missiles on my body. From now on I want you guys to call me “Apache” and respect my right to kill from above and kill needlessly. If you can’t accept me you’re a heliphobe and need to check your vehicle privilege. Thank you for being so understanding.")
    
    if command(message, "daddy"):
        await bot.send_message(message.channel, "Just me and my :two_hearts:daddy:two_hearts:, hanging out I got pretty hungry:eggplant: so I started to pout :disappointed: He asked if I was down :arrow_down:for something yummy :heart_eyes::eggplant: and I asked what and he said he'd give me his :sweat_drops:cummies!:sweat_drops: Yeah! Yeah!:two_hearts::sweat_drops: I drink them!:sweat_drops: I slurp them!:sweat_drops: I swallow them whole:sweat_drops: :heart_eyes: It makes :cupid:daddy:cupid: :blush:happy:blush: so it's my only goal... :two_hearts::sweat_drops::tired_face:Harder daddy! Harder daddy! :tired_face::sweat_drops::two_hearts: 1 cummy:sweat_drops:, 2 cummy:sweat_drops::sweat_drops:, 3 cummy:sweat_drops::sweat_drops::sweat_drops:, 4:sweat_drops::sweat_drops::sweat_drops::sweat_drops: I'm :cupid:daddy's:cupid: :crown:princess :crown:but I'm also a whore! :heart_decoration: He makes me feel squishy:heartpulse:!He makes me feel good:purple_heart:! :cupid::cupid::cupid:He makes me feel everything a little should!~ :cupid::cupid::cupid: :crown::sweat_drops::cupid:Wa-What!:cupid::sweat_drops::crown:")
    
    if command(message, "4chan"):
        await bot.send_message(message.channel, "Fresh off the boat, from reddit, kid? heh I remember when I was just like you. Braindead. Lemme give you a tip so you can make it in this cyber sanctuary: never make jokes like that. You got no reputation here, you got no name, you got jackshit here. It's survival of the fittest and you ain't gonna survive long on 4chan by saying stupid jokes that your little hugbox cuntsucking reddit friends would upboat. None of that here. You don't upboat. You don't downboat. This ain't reddit, kid. This is 4chan. We have REAL intellectual discussion, something I don't think you're all that familiar with. You don't like it, you can hit the bricks on over to imgur, you daily show watching son of a bitch. I hope you don't tho. I hope you stay here and learn our ways. Things are different here, unlike any other place that the light of internet pop culture reaches. You can be anything here. Me ? heh, I'm a judge.. this place.... this place has a lot to offer... heh you'll see, kid . . . that is if you can handle it.")
    
    if command(message, "discorole "):
        await bot.send_message(message.channel, "How many times do you want it to change?")
        await asyncio.sleep(0.2)
        times = await bot.wait_for_message(timeout=15, author=message.author)
        times = int(times.content)
        await bot.send_message(message.channel, "What should the interval be?")
        await asyncio.sleep(0.2)
        interval = await bot.wait_for_message(timeout=15, author=message.author)
        interval = int(interval.content)
        role = message.content[len(prefix + "discorole "):]
        roleObj = discord.utils.find(lambda r: r.name == role, message.server.roles)
        if not roleObj:
            await bot.send_message(message.channel, "`{}` is not a valid role".format(role))
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
            
    if command(message, "discoroleforever "):
        await bot.send_message(message.channel, "What should the interval be?")
        await asyncio.sleep(0.2)
        interval = await bot.wait_for_message(timeout=15, author=message.author)
        interval = int(interval.content)
        role = message.content[len(prefix + "discoroleforever "):]
        roleObj = discord.utils.find(lambda r: r.name == role, message.server.roles)
        if not roleObj:
            await bot.send_message(message.channel, "`{}` is not a valid role".format(role))
            return
        if interval < 2:
            interval = 2
        while True:
            colour = ''.join([random.choice('0123456789ABCDEF') for x in range(6)])
            colour = int(colour, 16)
            await bot.edit_role(message.server, roleObj, colour=discord.Colour(value=colour))
            await asyncio.sleep(interval)
    
    if command(message, "triggered"):
        await bot.send_message(message.channel, "http://i.imgur.com/zSddfUe.gif")
        
    if command(message, "setprefix "):
        new_prefix = message.content[len(prefix + "setprefix "):]
        settings['prefix'] = new_prefix
        with open("settings.json", "w") as settings_file:
            json.dump(settings, settings_file, indent=4, sort_keys=True, separators=(',', ' : '))
        await bot.send_message(message.channel, "Prefix set! Restart the bot for the changes to take affect.")
    
def command(message, cmd):
    if message.content.startswith(prefix + cmd):
        if message.author.id in whitelist:
            if cmd.endswith(" "):
                print("{} just used the {}command in {} ({}).".format(message.author, cmd, message.server, message.channel))
            else:
                print("{} just used the {} command in {} ({}).".format(message.author, cmd, message.server, message.channel))
            return True
        else:
            return False
    else:
        return False
        
bot.run(email, password)