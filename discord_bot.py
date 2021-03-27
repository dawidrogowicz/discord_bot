import discord
import TenGiphPy
import os
from discord.ext import commands

BOT_TOKEN=os.getenv('BOT_TOKEN')
TENOR_TOKEN=os.getenv('TENOR_TOKEN')

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='UwU ',intents=intents)
tenor = TenGiphPy.Tenor(token=TENOR_TOKEN)

@bot.event
async def on_ready():
    print('bot ready')

@bot.command()
async def health(ctx):
    await ctx.send(f"I'm great {ctx.message.author.mention} thank youwu! (⁄ ⁄•⁄ω⁄•⁄ ⁄)")
    await ctx.send(tenor.random('anime happy hug'))

@bot.event
async def on_member_join(member):
    for channel in member.guild.text_channels:
        if channel.name == 'welcome':
            await channel.send(f'Welcome {member.mention}! UwU')
            await channel.send(tenor.random('anime welcome'))

bot.run(BOT_TOKEN)
