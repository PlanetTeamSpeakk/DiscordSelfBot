import discord
from discord.ext import commands
import __main__ as main
import datetime

class serverinfo:
    """Gives a lot of information about the server."""
    
    def __init__(self, bot):
        self.bot = bot
        main.cmds['serverinfo'] =  {'server owner': {'help': 'Shows the server owner.', 'usage': 'server owner'},
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
                                        'server roleinfo': {'help': 'Shows information of the given role.', 'usage': 'server roleinfo <role>'}}
        
    async def on_message(self, message):
        msgchan = message.channel
        if await main.command(message, "server owner", True):
            await main.say(msgchan, embed=discord.Embed(title="Server owner", description="{}, the server owner is {}.".format(message.author.mention, message.server.owner.mention), colour=0X008CFF))
            
        elif await main.command(message, "server name", True):
            await main.say(msgchan, embed=discord.Embed(title="Server name", description="{}, the server name is {}.".format(message.author.mention, message.server), colour=0X008CFF))
            
        elif await main.command(message, "server sid", True):
            await main.say(msgchan, embed=discord.Embed(title="Server ID", description="{}, the Server ID is {}.".format(message.author.mention, message.server.id), colour=0X008CFF))
            
        elif await main.command(message, "server channelname", True):
            await main.say(msgchan, embed=discord.Embed(title="Channel name", description="{}, the channelname is #{}.".format(message.author.mention, message.channel.name), colour=0X008CFF))
            
        elif await main.command(message, "server cid", True):
            await main.say(msgchan, embed=discord.Embed(title="Channel ID", description="{}, the Channel ID is {}.".format(message.author.mention, message.channel.id), colour=0X008CFF))
            
        elif await main.command(message, "server time", True):
            await main.say(msgchan, embed=discord.Embed(title="Server time", description="{}, the server time is {}.".format(message.author.mention, datetime.datetime.now()), colour=0X008CFF))
            
        elif await main.command(message, "server roles", True):
            await main.say(msgchan, embed=discord.Embed(title="Roles", description="{}, the current roles are \n{}.".format(message.author.mention, ", ".join([r.name for r in message.server.role_hierarchy])), colour=0X008CFF))

        elif await main.command(message, "server emojis", True):
            comma = ", "
            emojis = [e.name for e in message.server.emojis]
            await main.say(msgchan, embed=discord.Embed(title="Emojis", description="{}, the current emojis are \n{}.".format(message.author.mention, comma.join(emojis)), colour=0X008CFF))
                
        elif await main.command(message, "server users", True):
            comma = "**, **"
            members = [m.name for m in message.server.members]
            if len(message.server.members) < 32:
                await main.say(msgchan, embed=discord.Embed(title="Users", description="{}, the current users are \n**{}**.".format(message.author.mention, comma.join(members)), colour=0X008CFF))
            else:
                await bot.send_message(message.author, embed=discord.Embed(title="Users", description="The current users in **{}** are \n**{}**.".format(message.server.name, comma.join(members)), colour=0X008CFF))
                
        elif await main.command(message, "server channels", True):
            comma = "**, **"
            voicechans = [x.name for x in message.server.channels if x.type == discord.ChannelType.voice]
            textchans = [x.name for x in message.server.channels if x.type == discord.ChannelType.text]
            await main.say(msgchan, embed=discord.Embed(title="Channels", description="{}, the current voice channels are \n**{}**.\nThe current text channels are\n**{}**.".format(message.author.mention, comma.join(voicechans), comma.join(textchans)), colour=0X008CFF))
                
        elif await main.command(message, "server compareids", True):
            if message.server.id == message.channel.id:
                await main.say(msgchan, embed=discord.Embed(title="Channel is default", description=
                "{}, the ids of the channel and the server are the same, so this is the default channel.\n(SID=`{}`, CID=`{}`)".format(message.author.mention, message.server.id, message.channel.id), colour=0X008CFF))
            else:
                await main.say(msgchan, embed=discord.Embed(title="Channel isn't default", description=
                "{}, The ids of the channel and the server are not the same, this is not the default channel. If there is a #general try it in that channel first.\n(SID=`{}`, CID=`{}`)".format(message.author.mention, message.server.id, message.channel.id), colour=0X008CFF))
                
        elif await main.command(message, "server icon", True):
            icon = message.server.icon_url
            embed = discord.Embed(title="Server icon", description="{}, the server icon is {}.".format(message.author.mention, icon), colour=0X008CFF)
            await main.say(msgchan, embed=embed)
            
        elif await main.command(message, "server info", True):
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
                await main.say(msgchan, embed=em)
            except discord.HTTPException:
                await main.say(msgchan, "An unknown error occured while sending the embedded message, maybe try giving me the `embed links` permission?")

        elif await main.command(message, "server channelinfo", True):
            channel = message.content[len(main.prefix + "server channelinfo "):]
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
                await main.say(msgchan, embed=em)
            except discord.HTTPException:
                channel_created_at = ("Created on {} ({} days ago!)".format(channel.created_at.strftime("%d %b %Y %H:%M"), passed))            
                em = discord.Embed(description="{}, here you go:".format(message.author.mention), title="Channel Info", color=0X008CFF)
                em.add_field(name="Channel Name", value=str(channel.name))
                em.add_field(name="Channel ID", value=str(channel.id))
                em.add_field(name="Channel Default", value=str(channel.is_default))
                em.add_field(name="Channel Position", value=str(channel.position + 1))
                em.add_field(name="Channel Topic", value="None")
                em.set_footer(text=channel_created_at)
                await main.say(msgchan, embed=em)
            
        elif await main.command(message, "server membercount", True):
            members = set(message.server.members)
            bots = filter(lambda m: m.bot, members)
            bots = set(bots)
            users = members - bots
            await main.say(msgchan, embed=discord.Embed(title="Server Membercount", description="{}, there are currently **{}** users and **{}** bots with a total of **{}** members in this server.".format(message.author.mention, len(users), len(bots), len(message.server.members)), colour=0X008CFF))
            
        elif await main.command(message, "server channelcount", True):
            chans = message.server.channels
            textchans = [x for x in message.server.channels if x.type == discord.ChannelType.text]
            voicechans = [x for x in message.server.channels if x.type == discord.ChannelType.voice]
            await main.say(msgchan, embed=discord.Embed(title="Server Channelcount", description="{}, there are currently **{}** text channels and **{}** voice channels with a total of **{}** channels in this server.".format(message.author.mention, len(textchans), len(voicechans), len(chans)), colour=0X008CFF))
                
        elif await main.command(message, "server rolecount", True):
            await main.say(msgchan, embed=discord.Embed(title="Server Rolecount", description="{}, there are currently **{}** roles in this server.".format(message.author.mention, len(message.server.role_hierarchy)), colour=0X008CFF))
            
        elif await main.command(message, "server emojicount", True):
            await main.say(msgchan, embed=discord.Embed(title="Server Emojicount", description="{}, there are currently **{}** emojis in this server.".format(message.author.mention, len(message.server.emojis)), colour=0X008CFF))
            
        elif await main.command(message, "server userinfo", True):
            user = message.content[len(main.prefix + "server userinfo "):]
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

            await main.say(msgchan, embed=em)
            
        elif await main.command(message, "server roleinfo", True):
            role = message.content[len(main.prefix + "server roleinfo "):]
            roleObj = discord.utils.get(message.server.roles, name=role)
            if roleObj is None:
                await main.say(msgchan, "`{}` is not a valid role".format(role))
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
            await main.say(msgchan, embed=em)
            
def setup(bot):
    bot.add_cog(serverinfo(bot))