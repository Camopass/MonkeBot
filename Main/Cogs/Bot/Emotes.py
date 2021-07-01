import discord
import re

from discord.ext import commands
from util.Config import load_config
from util.Discord import webhook_send


class Emotes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        super().__init__()
        self.config = load_config()
        self.re = re.compile(r':[A-z|0-9|\-|_]+?:(?!\d{18})')

    def get_emotes(self, member: discord.Member):
        emotes = []
        for guild in self.bot.guilds:
            if member in guild.members:
                emotes += guild.emojis
        return emotes

    @commands.Cog.listener()
    async def on_message(self, message):
        string = message.content

        def replace_emotes(match: re.Match):

            name = match.group()[1:-1]
            for emote in self.get_emotes(message.author):
                if emote.name == name and emote not in message.guild.emojis:
                    return str(emote)
            return match.group()

        match = self.re.sub(replace_emotes, string)
        if match != string:
            author = message.author
            await webhook_send(message.channel, match, avatar_url=author.avatar_url, name=author.name if author.nick is None else author.nick)
            await message.delete()


def setup(bot):
    bot.add_cog(Emotes(bot))
