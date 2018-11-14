import discord
from discord.ext import commands
import asyncio

bot = commands.Bot(command_prefix='#')

@bot.event
async def on_ready():
	print('Der Bot ist Online!')
	print(bot.user.name)
	
@bot.command()
async def Ip():
	await bot.say('Ip: Tropic.tk')
	await bot.say('Port: 25655')
	
@bot.command()
async def Author():
	await bot.say('OfficalGrasss')

bot.run('NTExMjMxMTkyNjg3ODM3MjA0.Dst4HQ.Ij-gWvUH3ngN62DQ9S-43a_acyU')
