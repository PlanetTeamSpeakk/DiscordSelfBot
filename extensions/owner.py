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
        main.cmds['owner'] = {'download': {'help': 'Downloads a file from a url and puts it in data/downloads', 'usage': 'download <url>'},
                                'whitelist add': {'help': 'Adds a user to the whitelist, use ids for this.', 'usage': 'whitelist add <user_id>'},
                                'whitelist remove': {'help': 'Removes a user from the whitelist, use ids for this.', 'usage': 'whitelist remove <user_id>'},
                                'shutdown': {'help': 'Shuts down the bot.', 'usage': 'shutdown'},
                                'name': {'help': 'Sets the name of the owner of the bot, limited by Discord to twice per hour.', 'usage': 'name <name>'},
                                'setprefix': {'help': 'Sets the prefix of the bot.', 'usage': 'setprefix <prefix>'},
                                'setinvite': {'help': 'Sets the invite to send everybody for the spaminvite and spaminvitedm commands.', 'usage': 'setinvite <invite>'},
                                'spaminvite': {'help': 'Spams the invite in the channel the command was sent.', 'usage': 'spaminvite <times>'},
                                'spaminvitedm': {'help': 'Sends the invite to everyone in the server except for mods and admins.', 'usage': 'spaminvitedm <message>'},
                                'clearconsole': {'help': 'Clears the console.', 'usage': 'clearconsole'}}
        
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
                
            elif await main.command(message, "clearconsole", True):
                print("\n" * 696969)
                await main.say(msgchan, "Console cleared!")
                
            elif await main.command(message, "setinvite ", True):
                invite = message.content[len(main.prefix + "setinvite "):]
                main.settings['invite'] = invite
                main.save_settings()
                await main.say(msgchan, "Invite set!")
                
            elif await main.command(message, "spaminvite ", True):
                invite = settings['invite']
                if invite is "None":
                    await main.say(msgchan, "You haven't set an invite link, set one with {}setinvite <invite>".format(main.prefix))
                times = int(message.content[len(main.prefix + "spaminvite "):])
                time = 0
                while time < times:
                    time = time + 1
                    await main.say(msgchan, invite)
          
            elif await main.command(message, "spaminvitedm ", True):
                msg = " " + message.content[len(main.prefix + "spaminvitedm "):]
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
                                await self.bot.send_message(member, invite + msg)
                                sent = sent + 1
                                sent_list.append(member.id)
                                print("Sent an invite to {} people.".format(sent))
                                await asyncio.sleep(60) # There you go Nathan, happy now?
                    except:
                        pass
                    with open("sent_list.json", "w") as sent_list_json:
                        json.dump(sent_list, sent_list_json, indent=4, sort_keys=True, separators=(',', ' : '))
                        sent_list_json = None
        
    def save_extensions(self):
        with open("data/dsb/extensions.json", "w") as extensions_file:
            json.dump(self.extensions, extensions_file, indent=4, sort_keys=True, separators=(',', ' : '))
            extensions_file = None
            
def setup(bot):
    bot.add_cog(owner(bot))