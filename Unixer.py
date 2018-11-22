import discord
from discord.ext import commands
import asyncio
import json
import os 
token = ""

extensions = []

bot = commands.Bot(command_prefix = "./unix ")
bot.remove_command("help")
def split_list(a_list):
	half = len(a_list)//2
	return a_list[:half], a_list[half:]

async def create_data(users, targid):
	if not targid in users:
		users[targid] = {}
		users[targid]["directory"] = "/"
		embed = discord.Embed(
			title = "Unixer Admin Console - User Created",
			description = "User has been created.",
			colour = discord.Colour(696969)
		)
		embed.set_footer(text="Unixer is made by pepsipu#3655 / Check out pepsipu.com.")
		embed.set_author(name="Unixer", icon_url="https://cdn.discordapp.com/attachments/515039814010142740/515058115620896768/icon_hires.png")

		await bot.say(embed=embed)
	else:
		embed = discord.Embed(
			title = "Unixer Admin Console - User Already Exists",
			description = "User already exits.",
			colour = discord.Colour(696969)
		)

		embed.set_footer(text="Unixer is made by pepsipu#3655 / Check out pepsipu.com.")
		embed.set_author(name="Unixer", icon_url="https://cdn.discordapp.com/attachments/515039814010142740/515058115620896768/icon_hires.png")

		await bot.say(embed=embed)

async def unauthorized():
	embed = discord.Embed(
			title = "Unixer Admin Console - Unauthorized",
			description = "You are unauthorized to perform this command.",
			colour = discord.Colour(696969)
		)
	embed.set_footer(text="Unixer is made by pepsipu#3655 / Check out pepsipu.com.")
	embed.set_author(name="Unixer", icon_url="https://cdn.discordapp.com/attachments/515039814010142740/515058115620896768/icon_hires.png")

	await bot.say(embed=embed)


@bot.event
async def on_ready():
	await bot.change_presence(game=discord.Game(name="./unix help"))
	print("Ready")
@bot.command(pass_context=True)
async def help(ctx):
	embed = discord.Embed(
			title = "Unixer - Terminal From Discord",
			description = "Talking to your computer has never been easier. By running Unixer on your computer, you can control it from anywhere. From your phone, laptop, anything that runs Discord. It is incredibly secure and near impossible to get authorized access, as it's built by a security researcher.",
			colour = discord.Colour(696969)
		)
	embed.set_footer(text="Unixer is made by pepsipu#3655 / Check out pepsipu.com.")
	embed.set_author(name="Unixer", icon_url="https://cdn.discordapp.com/attachments/515039814010142740/515058115620896768/icon_hires.png")
	embed.add_field(name="cmd <commands>", value="Main command. Run this to give input and get output.", inline=False)
	embed.add_field(name="makeuser <userid>", value="Create a user to be authorized to use Unixer.", inline=False)
	embed.add_field(name="removeuser <userid>", value="Removes a user from the database.", inline=False)
	embed.add_field(name="listusers", value="Lists users in the database.")
	await bot.say(embed=embed)
@bot.command(pass_context=True)
async def cmd(ctx, *args):
	with open("Users.json", "r") as f:
		users = json.load(f)
	if ctx.message.author.id in users:
		directory = users[ctx.message.author.id]["directory"]
		cmd = "{}".format("  ".join(args))
		output  = os.popen("cd {} ; {} ; pwd".format(directory, cmd)).readlines()
		pretty = " "
		for item in output:
			pretty += "{} ".format(item)
		prettyl = list(pretty)
		del prettyl[-1]
		pretty = "".join(str(x) for x in prettyl)
		prettys = pretty.split()
		users[ctx.message.author.id]["directory"] = prettys[-1]
		directory = prettys[-1]
		pretty = pretty.replace(directory,"")
		if cmd == "pwd":
			pretty = directory
		if len(pretty) < 1000:
			embed = discord.Embed(
				title = "Unixer Admin Console - Command Run",
				description = "Command output is below.",
				colour = discord.Colour(696969)
			)
			
			embed.add_field(name="Command Output", value="Output:\n {}".format(pretty), inline=False)
			embed.add_field(name="Directory Saved", value="{}".format(directory), inline=False)
			embed.set_footer(text="Unixer is made by pepsipu#3655 / Check out pepsipu.com.")
			embed.set_author(name="Unixer", icon_url="https://cdn.discordapp.com/attachments/515039814010142740/515058115620896768/icon_hires.png")

			await bot.say(embed=embed)
			with open("Users.json", "w") as f:
				users = json.dump(users, f)
		else:
			prettylong = pretty.split("\n")
			print(len(prettylong))
			p1, p2 = split_list(prettylong)
			p2s = "\n".join(str(x) for x in p2)
			p1s = "\n".join(str(x) for x in p1)
			if len(p1s) < 1000:
				embed = discord.Embed(
					title = "Unixer Admin Console - Command Run",
					description = "Command output is below.",
					colour = discord.Colour(696969)
				)
				
				embed.add_field(name="Command Output", value="Output:\n {}".format(p1s), inline=False)
				embed.add_field(name="Command Output", value="Output:\n {}".format(p2s), inline=False)
				embed.add_field(name="Directory Saved", value="{}".format(directory), inline=False)
				embed.set_footer(text="Unixer is made by pepsipu#3655 / Check out pepsipu.com.")
				embed.set_author(name="Unixer", icon_url="https://cdn.discordapp.com/attachments/515039814010142740/515058115620896768/icon_hires.png")
				await bot.say(embed=embed)
			else:
				p11, p12 = split_list(p1)
				p21, p22 = split_list(p2)
				p11s = "\n".join(str(x) for x in p11)
				p12s = "\n".join(str(x) for x in p12)
				p21s = "\n".join(str(x) for x in p21)
				p22s = "\n".join(str(x) for x in p22)
				if len(p11s) < 1000:
					sume = len(p22s)
					print(sume)
					embed = discord.Embed(
						title = "Unixer Admin Console - Command Run",
						description = "Command output is below.",
						colour = discord.Colour(696969)
					)
					embed.add_field(name="Command Output", value="Output:\n {}".format(p11s), inline=False)
					embed.add_field(name="Command Output", value="Output:\n {}".format(p12s), inline=False)
					embed.add_field(name="Directory Saved", value="{}".format(directory), inline=False)
					embed.set_footer(text="Unixer is made by pepsipu#3655 / Check out pepsipu.com.")
					embed.set_author(name="Unixer", icon_url="https://cdn.discordapp.com/attachments/515039814010142740/515058115620896768/icon_hires.png")
					await bot.say(embed=embed)
					embed = discord.Embed(
						title = "Unixer Admin Console - Command Run",
						description = "Command output is below.",
						colour = discord.Colour(696969)
					)
					embed.add_field(name="Command Output", value="Output:\n {}".format(p21s), inline=False)
					embed.add_field(name="Command Output", value="Output:\n {}".format(p22s), inline=False)
					embed.add_field(name="Directory Saved", value="{}".format(directory), inline=False)
					embed.set_footer(text="Unixer is made by pepsipu#3655 / Check out pepsipu.com.")
					embed.set_author(name="Unixer", icon_url="https://cdn.discordapp.com/attachments/515039814010142740/515058115620896768/icon_hires.png")
					await bot.say(embed=embed)
				else:
					embed = discord.Embed(
						title = "Unixer Admin Console - Command Output Too Big",
						description = "Command output is too big to be displayed. Your location is {}".format(directory),
						colour = discord.Colour(696969)
					)
					embed.set_footer(text="Unixer is made by pepsipu#3655 / Check out pepsipu.com.")
					embed.set_author(name="Unixer", icon_url="https://cdn.discordapp.com/attachments/515039814010142740/515058115620896768/icon_hires.png")
					await bot.say(embed=embed)



	else:
		await unauthorized()
	
@bot.command(pass_context=True)
async def makeuser(ctx, targid):
	with open("Users.json", "r") as f:
		users = json.load(f)
	if ctx.message.author.id in users:
		await create_data(users, targid)
		with open("Users.json", "w") as f:
			users = json.dump(users, f)
	else:
		await unauthorized()

@bot.command(pass_context=True)
async def removeuser(ctx, targid):
	with open("Users.json", "r") as f:
		users = json.load(f)
	if ctx.message.author.id in users:
		if targid in users:
			del users[targid]
			with open("Users.json", "w") as f:
				users = json.dump(users, f)
			embed = discord.Embed(
				title = "Unixer Admin Console - User Removed",
				description = "User has been removed.",
				colour = discord.Colour(696969)
			)
			embed.set_footer(text="Unixer is made by pepsipu#3655 / Check out pepsipu.com.")
			embed.set_author(name="Unixer", icon_url="https://cdn.discordapp.com/attachments/515039814010142740/515058115620896768/icon_hires.png")
			await bot.say(embed=embed)
		else:
			embed = discord.Embed(
				title = "Unixer Admin Console - User Does Not Exit",
				description = "Requested user to be deleted does not exist.",
				colour = discord.Colour(696969)
			)
			embed.set_footer(text="Unixer is made by pepsipu#3655 / Check out pepsipu.com.")
			embed.set_author(name="Unixer", icon_url="https://cdn.discordapp.com/attachments/515039814010142740/515058115620896768/icon_hires.png")
			await bot.say(embed=embed)
	else:
		await unauthorized()

@bot.command(pass_context=True)
async def listusers(ctx):
	with open("Users.json", "r") as f:
		users = json.load(f)
	if ctx.message.author.id in users:
		userid = ""
		for ids in users:
			userid += "[{}]\n".format(ids)
		print(userid)
		embed = discord.Embed(
			title = "Unixer Admin Console - User List",
			description = "User List:\n {}".format(userid),
			colour = discord.Colour(696969)
		)
		embed.set_footer(text="Unixer is made by pepsipu#3655 / Check out pepsipu.com.")
		embed.set_author(name="Unixer", icon_url="https://cdn.discordapp.com/attachments/515039814010142740/515058115620896768/icon_hires.png")
		await bot.say(embed=embed)
	else:
		await unauthorized()




if __name__ == "__main__":
	for extension in extensions:
		try:
			bot.load_extension(extension)
		except Exception as problem:
			print("Cannot load {}. [{}]".format(extension, problem))
	bot.run(token)

