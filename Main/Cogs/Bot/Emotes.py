import discord
import re

from discord.ext import commands
from util.Config import load_config


class Emotes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        super().__init__()
        self.config = load_config()

    @commands.Cog.listener()
    async def on_message(self, message):
        string = message.content
        match = re.match(':.+:', string)



def setup(bot):
    bot.add_cog(Emotes(bot))
