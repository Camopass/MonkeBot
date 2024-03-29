# Monke Bot V 1.01 Alpha
import os
import discord

from discord.ext import commands
from util.GetToken import get_token

token = get_token()
intents = discord.Intents.all()
bot = commands.Bot('?', intents=intents)


@bot.event
async def on_ready():
    print('------------')
    print('Bot is Ready')
    print('Client Name')
    print(bot.user.name)
    print('Client ID')
    print(bot.user.id)
    print('------------')


@bot.command()
async def test(ctx, foo: str = 'Bot is active.'):
    await ctx.send(foo)


for category in os.listdir('Main/Cogs'):
    for cog in os.listdir(f'Main/Cogs/{category}'):
        if cog.endswith('.py'):
            bot.load_extension(f'Cogs.{category}.{cog[:-3]}')
            print(f'Loaded {cog}')

bot.run(token)
