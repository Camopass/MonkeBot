# Monke Bot V 1.0 Alpha
import os

from discord.ext import commands
from util.GeToken import get_token

token = get_token()
bot = commands.Bot('?')


@bot.event
async def on_ready():
    print('------------')
    print('Bot is Ready')
    print('Client Name')
    print(bot.user.name)
    print('Client Name')
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
