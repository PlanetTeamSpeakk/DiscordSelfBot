import discord
from discord.ext import commands
import json
import os
import __main__ as main
import asyncio
import aiohttp
import random

class owner:
    """Owner only commands."""
    
    def __init__(self, bot):
        self.bot = bot
        if not os.path.exists("extensions"):
            os.makedirs("extensions")
        if not os.path.exists("data/dsb/extensions.json"):
            with open("data/dsb/extensions.json", "w") as extensions:
                json.dump({'general': True, 'useful': True, 'owner': True, 'serverinfo': True, 'copypastas': True}, extensions, indent=4, sort_keys=True, separators=(',', ' : '))
                extensions = None
        with open("data/dsb/extensions.json", "r") as extensions:
            self.extensions = json.load(extensions)
            extensions = None
        
    async def on_message(self, message):
        msgchan = message.channel
        if main.is_owner(message.author):
            if await main.command(message, "load ", True):
                extension = message.content[len(main.prefix + "load "):]
                if extension == "":
                    await main.say(msgchan, "I can't load an empty string.")
                    return
                else:
                    try:
                        self.bot.load_extension("extensions." + extension)
                        self.extensions[extension] = True
                        self.save_extensions()
                        await main.say(msgchan, "Extension loaded.")
                    except Exception as e:
                        print(e)
                        await main.say(msgchan, "Loading gave an error, check your console for more information.")
                        
            elif await main.command(message, "unload ", True):
                extension = message.content[len(main.prefix + "unload "):]
                if extension == "":
                    await main.say(msgchan, "I can't unload an empty string.")
                elif extension not in self.bot.cogs.keys():
                    await main.say(msgchan, "That extension is not loaded.")
                elif extension == "owner":
                    await main.say(msgchan, "Can't unload the owner extension, you can reload it though :P.")
                else:
                    try:
                        self.bot.unload_extension("extensions." + extension)
                        self.extensions[extension] = False
                        self.save_extensions()
                        await main.say(msgchan, "Extension unloaded.")
                    except Exception as e:
                        print(e)
                        await main.say(msgchan, "An error occured while unloaded the cog, check your console for more information.")
                
            elif await main.command(message, "reload ", True):
                extension = message.content[len(main.prefix + "reload "):]
                if extension == "":
                    await main.say(msgchan, "I can't reload an empty string.")
                elif extension not in self.bot.cogs.keys():
                    await main.say(msgchan, "That extension is not loaded.")
                else:
                    try:
                        self.bot.unload_extension("extensions." + extension)
                        self.bot.load_extension("extensions." + extension)
                        await main.say(msgchan, "Extension reloaded.")
                    except Exception as e:
                        print(e)
                        await main.say(msgchan, "An error occured while reloading the extension, check your console for more information.")
                
            elif await main.command(message, "extensions", True):
                await main.say(msgchan, ", ".join(self.bot.cogs.keys()) + ".")
                
            elif await main.command(message, "whitelist add ", True):
                id = message.content[len(main.prefix + "whitelist add "):]
                main.settings['whitelist'].append(id)
                with open("data/dsb/settings.json", "w") as settings_file:
                    json.dump(main.settings, settings_file, indent=4, sort_keys=True, separators=(',', ' : '))
                await main.say(msgchan, "Added user to whitelist!")
                
            elif await main.command(message, "whitelist remove ", True):
                id = message.content[len(main.prefix + "whitelist remove "):]
                main.settings['whitelist'].remove(id)
                with open("data/dsb/settings.json", "w") as settings_file:
                    json.dump(main.settings, settings_file, indent=4, sort_keys=True, separators=(',', ' : '))
                await main.say(msgchan, "Removed user from the whitelist!")
                    
            elif await main.command(message, "shutdown", True):
                sys.exit("Bot got shutdown.")
                
            elif await main.command(message, "name ", True):
                name = message.content[len(main.prefix + "name "):]
                await self.bot.edit_profile(settings['password'], username=name)
                await main.say(msgchan, "Name set!")
                
            elif await main.command(message, "setprefix ", True):
                new_prefix = message.content[len(main.prefix + "setprefix "):]
                main.settings['prefix'] = new_prefix
                main.save_settings()
                await main.say(msgchan, "Prefix set! Restart the bot for the changes to take affect.")
                
            elif await main.command(message, "download ", True):
                url = message.content[len(main.prefix + "download "):]
                downloadmsg = await self.bot.send_message(msgchan, "What's the file suffix?")
                await asyncio.sleep(0.2)
                suffix = await self.bot.wait_for_message(timeout=15, author=message.author)
                await self.bot.edit_message(downloadmsg, "Downloading...")
                if not "http://" in url:
                    if not "https://" in url:
                        if not "." in url:
                            await main.say(msgchan, "The given url is not in the correct format.\nA correct format would be `http://dank.website/file.suffix`.")
                        else:
                            pass
                    else:
                        pass
                else:
                    pass
                if not os.path.exists("data/downloads"):
                    os.makedirs("data/downloads")
                async with aiohttp.get(url) as r:
                    file = await r.content.read()
                fileloc = "data/downloads/download{}.{}".format(random.randint(1000, 9999), suffix.content.lower())
                with open(fileloc, 'wb') as f:
                    f.write(file)
                await self.bot.edit_message(downloadmsg, "File downloaded, look in the root folder.")
                
            elif await main.command(message, "mentionmsg ", True):
                new_mentionmsg = message.content[len(main.prefix + "mentionmsg "):]
                main.settings['mentionmsg'] = new_mentionmsg
                main.save_settings()
                await main.say(msgchan, "Mention message set!")
                    
            elif await main.command(message, "mentionmode ", True):
                mentionmodes = ['legit', 'fast']
                new_mentionmode = message.content[len(main.prefix + "mentionmode "):]
                if not new_mentionmode in mentionmodes:
                    await main.say(msgchan, "That's not a correct mentionmode, you can choose from `legit` or `fast`.")
                    return
                main.settings['mentionmode'] = new_mentionmode
                main.save_settings()
                await main.say(msgchan, "Mentionmode set!")
        
    def save_extensions(self):
        with open("data/dsb/extensions.json", "w") as extensions_file:
            json.dump(self.extensions, extensions_file, indent=4, sort_keys=True, separators=(',', ' : '))
            extensions_file = None
            
def setup(bot):
    bot.add_cog(owner(bot))