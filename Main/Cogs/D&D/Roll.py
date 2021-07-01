import discord
import random
import re

from discord.ext import commands
from util.Config import load_config


class Roll(commands.Cog):
    def __init__(self, bot):
        super().__init__()
        self.bot = bot
        self.config = load_config()

    @commands.command()
    async def roll(self, ctx, *, roll: str = None):
        if roll is None:
            e = discord.Embed(title=self.config.cosmetics.text.fail,
                              description='You have to include the dice roll.',
                              color=self.config.cosmetics.color.fail
            )
            return await ctx.send(embed=e)
        res = []
        dice = re.split(r' +?\+ *', roll)
        print(dice)
        for die in dice:
            try:
                if die.startswith('d'):
                    d = die[-1:]
                    res.append(random.randint(1, int(d)))
                else:
                    d = die.split('d')
                    for i in range(int(d[0])):
                        res.append(random.randint(1, int(d[1])))
            except ValueError:
                return await ctx.send(embed=discord.Embed(
                    title=self.config.cosmetics.text.fail,
                    description='Could not understand that value.',
                    color=self.config.cosmetics.color.fail
                ))

        total = sum(res)
        res = [str(i) for i in res]
        res = ', '.join(res)

        e = discord.Embed(
            title=f'Roll: **{roll}**',
            description=f'`{total}`: {res}',
            color=self.config.cosmetics.color.success
        )
        await ctx.send(embed=e)


def setup(bot):
    bot.add_cog(Roll(bot))
