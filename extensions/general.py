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
        main.cmds['general'] = {'boobs': {'help': 'Shows some boobs.', 'usage': 'boobs'},
                                'ass': {'help': 'Shows some ass.', 'usage': 'ass'},
                                'say': {'help': 'Let\'s the bot say something.', 'usage': 'say <message>'},
                                'lenny': {'help': 'Prints out a lenny face.', 'usage': 'lenny'},
                                'shrug': {'help': 'Shrugs.', 'usage': 'shrug'},
                                'greentext': {'help': 'Makes your text green.', 'usage': 'greentext <text>'},
                                'orangetext': {'help': 'Makes your text orange.', 'usage': 'orangetext <text>'},
                                'bluetext': {'help': 'Makes your text blue. Looks pretty shitty tbh.', 'usage': 'bluetext <text>'},
                                'lmgtfy': {'help': 'Makes a lmgtfy (let me google that for you) link.', 'usage': 'lmgtfy <search_quarries>'},
                                'triggered': {'help': 'The h3h3 triggered meme gif.', 'usage': 'triggered'},
                                'uptime': {'help': 'Shows the bots uptime.', 'usage': 'uptime'},
                                'ascii': {'help': 'Converts text to ascii (figlet)', 'usage': 'ascii <text>'},
                                'penis': {'help': 'Detects a users penis length, this is 100% accurate.', 'usage': 'penis <user_name>'}}
        
    async def on_message(self, message):
        msgchan = message.channel
        if await main.command(message, "uptime", True):
            uptime = datetime.datetime.utcnow() - main.started
            await main.say(msgchan, "The bot has been up for **{} hour(s), {} minute(s) and {} second(s)**.".format(uptime.seconds//3600, (uptime.seconds//60)%60, uptime.seconds%60))
            
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
                
        elif await main.command(message, "say ", True):
            await main.say(msgchan, message.content[len(prefix + "say "):])
            
def setup(bot):
    if error:
        raise RuntimeError("A library could not be installed, extension can't be loaded.")
    bot.add_cog(general(bot))