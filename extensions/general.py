import discord
import json
import asyncio
import __main__ as main
import datetime
import random
import aiohttp
from subprocess import check_output
try:
    from pyfiglet import figlet_format
    error = False
except:
    try:
        print("Pyfiglet is not installed, installing it now...")
        check_output("pip3 install pyfiglet", shell=True)
        from pyfiglet import figlet_format
        error = False
        print("Succesfully install pyfiglet.")
    except:
        print("Pyfiglet did not succesfully install, cannot load extension.")
        error = True

class general:
    """You probably don't really need these."""
    
    def __init__(self, bot):
        self.bot = bot
        
    async def on_message(self, message):
        msgchan = message.channel
        if await main.command(message, "help", True):
            cmd = message.content[len(main.prefix + "help "):]
            help_cmds = ""
            if cmd == "":
                for cmda in main.cmds.keys():
                    if len(cmda + main.cmds[cmda]['help']) > 75:
                        help_cmds += "- `{}`: {}...\n".format(cmda, main.cmds[cmda]['help'][:75])
                    else:
                        help_cmds += "- `{}`: {}\n".format(cmda, main.cmds[cmda]['help'])
                    if len(help_cmds) > 1750:
                        await main.say(msgchan, help_cmds)
                        help_cmds = ""
                await main.say(msgchan, help_cmds)
                help_cmds = ""
                await main.say(msgchan, "TL;DR click here <https://github.com/PlanetTeamSpeakk/DiscordSelfBot#commands>\nTo get information of a specific command type {}help <command>".format(main.prefix))
            else:
                try:
                    await main.say(msgchan, "`{}`:\n{}\n\nUsage:\n`{}`".format(cmd, main.cmds[cmd]['help'], main.prefix + main.cmds[cmd]['usage']))
                except KeyError:
                    await main.say(msgchan, "The command you entered ({}) could not be found.".format(cmd))
                
        if await main.command(message, "uptime", True):
            await main.say(msgchan, "The bot has been up for **{}**.".format(datetime.datetime.now() - main.started))
            
        elif await main.command(message, "penis", True):
            user = message.content[len(main.prefix + "penis "):]
            if user is "":
                user = message.author
            else:
                user = discord.utils.get(message.server.members, name=user)
            random.seed(user.id)
            psize = "8" + "="*random.randint(0, 30) + "D"
            await main.say(msgchan, "{} penis size: {}".format(user.mention, psize))
            
        elif await main.command(message, "ascii ", True):
            text = message.content[len(main.prefix + "ascii "):]
            msg = str(figlet_format(text, font='cybermedium'))
            if msg[0] == " ":
                msg = "." + msg[1:]
            error = figlet_format('LOL, that\'s a bit too long.',
                                  font='cybermedium')
            if len(msg) > 2000:
                msg = error
            await main.say(msgchan, "```fix\n{}```".format(msg))
            
        elif await main.command(message, "boobs", True):
            author = message.author
            try:
                rdm = random.randint(0, 10219)      
                search = ("http://api.oboobs.ru/boobs/{}".format(rdm))
                async with aiohttp.get(search) as r:
                    result = await r.json()
                    boob = random.choice(result)
                    boob = "http://media.oboobs.ru/{}".format(boob["preview"])
            except Exception as e:
                await main.say(msgchan, "{} ` Error getting results.`".format(author.mention))
                return
            await main.say(msgchan, "{}".format(boob))
            
        elif await main.command(message, "ass", True):
            author = message.author
            try:
                rdm = random.randint(0, 10219)      
                search = ("http://api.obutts.ru/boobs/{}".format(rdm))
                async with aiohttp.get(search) as r:
                    result = await r.json()
                    butt = random.choice(result)
                    butt = "http://media.obutts.ru/{}".format(boob["preview"])
            except Exception as e:
                await main.say(msgchan, "{} ` Error getting results.`".format(author.mention))
                return
            await main.say(msgchan, "{}".format(butt))
            
        elif await main.command(message, "lenny", False):
            if main.is_owner(message.author):
                await self.bot.edit_message(message, "( ͡° ͜ʖ ͡°)")
            else:
                await main.say(msgchan, "( ͡° ͜ʖ ͡°)")
          
        elif await main.command(message, "shrug", True):
            await main.say(msgchan, "¯\_(ツ)_/¯")
            
        elif await main.command(message, "greentext ", False):
            text = message.content[len(main.prefix + "greentext "):]
            if main.is_owner(message.author):
                await self.bot.edit_message(message, "```css\n{}```".format(text))
            else:
                await main.say(msgchan, "```css\n{}```".format(text))
                
        elif await main.command(message, "orangetext ", False):
            text = message.content[len(main.prefix + "orangetext "):]
            if main.is_owner(message.author):
                await self.bot.edit_message(message, "```fix\n{}```".format(text))
            else:
                await main.say(msgchan, "```fix\n{}```".format(text))
                
        elif await main.command(message, "bluetext ", False):
            text = message.content[len(main.prefix + "bluetext "):].replace(" ", ".")
            if main.is_owner(message.author):
                await self.bot.edit_message(message, "```html\n<{}>```".format(text))
            else:
                await main.say(msgchan, "```html\n<{}>```".format(text))
        
        elif await main.command(message, "lmgtfy ", True):
            to_google = message.content[len(main.prefix + "lmgtfy "):]
            await main.say(msgchan, "http://lmgtfy.com/?q={}".format(to_google.replace(" ", "+")))
            
        elif await main.command(message, "triggered", True):
            await main.say(msgchan, "http://i.imgur.com/zSddfUe.gif")
                
        for person in message.mentions:
            if message.author.id != self.bot.user.id:
                if main.mentionmsg != "None":
                    if person.id == self.bot.user.id:
                        if main.mentionmode == "legit":
                            await asyncio.sleep(2)
                            await bot.send_typing(message.channel)
                            await asyncio.sleep(2)
                            await main.say(msgchan, mentionmsg)
                        elif main.mentionmode == "fast":
                            await main.say(msgchan, mentionmsg)
            
def setup(bot):
    if error:
        raise RuntimeError("A library could not be installed, extension can't be loaded.")
    bot.add_cog(general(bot))