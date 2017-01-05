# DiscordSelfBot
1. [Description](#description)
2. [Installation](#installation)
3. [Commands](#commands)
4. [Annotations](#annotations)
5. [Creating your own extension](#extensions)

## Description
A nice selfbot for discord

## Installation
For installation you will need 
- [Python latest (v3 not v2)](http://python.org/getit/) **MAKE SURE TO ADD TO PATH**
- [Git](http://git-scm.com) **DON'T CHANGE ANY OF THE SETTINGS**
- Then just download and extract the bot, the rest will be automatically done.

## Commands
- `[p]help` Shows all the commands and help for them.
- `[p]restart` Restarts the bot.
- `[p]boobs` Shows some boobs.
- `[p]ass` Shows some ass.
- `[p]say` Let's the bot say something.
- `[p]server owner` Shows the server owner.
- `[p]server name` Shows the server name.
- `[p]server sid` Shows the server id.
- `[p]server channelname` Shows the channelname.
- `[p]server cid` Shows the channel id.
- `[p]server time` Shows the server time.
- `[p]server roles` Shows the server roles.
- `[p]server emojis` Shows the server emojis.
- `[p]server users` Shows the server users.
- `[p]server channels` Shows the server channels.
- `[p]server compareids` Compares the id of the server and the channel to see if it's default.
- `[p]server icon` Shows the server icon.
- `[p]server info` Shows all information of the server.
- `[p]server channelinfo` Shows all information of the channel.
- `[p]server membercount` Counts all the members in the server.
- `[p]server rolecount` Counts all the roles of the server.
- `[p]server emojicount` Counts all the emojis of the server.
- `[p]server userinfo [user]` Shows information for a user, if None given it shows yours.
- `[p]server roleinfo <role>` Shows information for a role.
- `[p]download <download_url>` Downloads a file and puts it in the bots root folder so you don't have to.
- `[p]mentionmsg <msg>` Sets the message that the bot should send if you get mentioned.
- `[p]whitelist add <user_id>` Adds a user to the whitelist so they can use your selfbot too!
- `[p]whitelist remove <user_id>` Removes a user from the whitelist so they can't use your selfbot anymore.
- `[p]lenny` Prints out a lenny face.
- `[p]shrug` Shrugs.
- `[p]shutdown` Shuts down the bot.
- `[p]name <name>` Sets the bots name.
- `[p]greentext <text>` Prints out a green text.
- `[p]orangetext <text>` Prints out an orange text.
- `[p]bluetext <text>` Prints out a blue text.
- `[p]lmgtfy <search_quary>` Gives a lmgtfy link.
- `[p]navyseal` Navyseal copypasta.
- `[p]edgyshit` Edgyshit copypasta.
- `[p]goodshit` Goodshit copypasta.
- `[p]appache` Attack helicopter copypasta.
- `[p]daddy` Daddy and me copypasta.
- `[p]4chan` Found it on 4chan copypasta.
- `[p]triggered` The triggered meme.
- `[p]setprefix` Changes the prefix of the bot.
- `[p]flirting101` The flirting101 copypasta.
- `[p]setinvite <invite>` Sets the invite link to spam for
- `[p]spaminvite <times>` Spams the invite link of your server.
- `[p]spaminvitedm <message>` Sends the invite link of your server to everyone in the server where this command was sent to.
- `[p]discrim <discrim_number>` Tells you all the people you can see with the discrim you gave.
- `[p]emoteurl <emote_name>` Gives you an url for the given CUSTOM emote.
- `[p]genbotoauth <bot_name>` Generates an oauth url for the given bot, names no mentions.
- `[p]genoauth <id>` Generates an oauth url for the given id.
- `[p]calc <problem>` Calculates a math problem so you don't have to.
- `[p]avatar <user_name>` Shows the avatar of the given user, names no mentions.
- `[p]mentionmode <mode>` Sets the mention mode (legit or fast)
- `[p]convert <file_url>` Converts stuff like mp3, mp4, png to anything you like.
- `[p]ascii <text>` Converts text to ascii.
- `[p]penis <user_name>` Tells you how long someone's penis is, 100% accurate.
- `[p]shorten <url>` Shortens a long url using bit.ly.
- `[p]ping` Pong!
- `[p]qrcode <url>` Makes a qr code of a url.
- `[p]uptime` Shows the uptime.

## Annotations
[] = optional.

<> = needed.

[p] = the prefix you set.

## Extensions
So you want to make your own extension?

Well that's pretty easy, all you need to begin with is this:

```py
import discord
from discord.ext import commands
import __main__ as main

class myextension:
    """My custom extension that does stuff!."""
    
    def __init__(self, bot):
        self.bot = bot
        
    async def on_message(self, message):
        msgchan = message.channel
        if await main.command(message, "hi", True):
            await main.say(msgchan, "Hi!")
            
def setup(bot):
    bot.add_cog(myextension(bot))
```
This will let the bot say "Hi" when you do [p]hi
