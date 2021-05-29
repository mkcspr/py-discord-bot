import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands, tasks
import platform

client = Bot(description="soup bot", command_prefix="#", pm_help = True)

@client.event
async def on_ready():
	print('Use this link to invite {}:'.format(client.user.name))
	print('https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=8'.format(client.user.id))

client.run('ODQ3NjE5NTE2MjgzODc5NDM5.YLAtMA.ZeVIDBwERLzKGReF0W6K5C0uV4A')