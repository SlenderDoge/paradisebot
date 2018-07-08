import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import os


token = str(os.environ.get("BOT_TOKEN"))

welcome_channel_id = str(os.environ.get("WELCOME_CHANNEL_ID"))


Client = discord.Client()
bot = commands.Bot(command_prefix="!")


def channel_get(member_object, channel_type):
	server_object = member_object.server
	
	if channel_type == "welcome":
		welcome_channel_object = server_object.get_channel(welcome_channel_id)
		
		if welcome_channel_object == None:
			print("ERROR: Welcome Channel ID Invalid!")
			
		return welcome_channel_object

	else:
		print("ERROR: channel_get error, invalid channel_type!")


@bot.event
async def on_ready():
	await bot.wait_until_ready()
	print (bot.user.name + " is ready")
	print ("ID: " + bot.user.id)
	
	
	
@bot.event
async def on_member_join(member):
	
	server_object = member.server
	welcome_channel_object = channel_get(member, "welcome")
	
	await bot.send_message(welcome_channel_object, "Welcome to **{0}**, {1}!".format(server_object.name, member.mention))
	
@bot.event
async def on_member_remove(member):
	
	welcome_channel_object = channel_get(member, "welcome")
	
	await bot.send_message(welcome_channel_object, "Goodbye **{0}#{1}**".format(member.name, member.discriminator))


bot.run(token)
