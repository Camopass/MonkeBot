import discord
import typing

from discord.ext import commands


async def webhook_send(channel: discord.TextChannel, message: str, *, avatar_url: str, name: str):
    webhooks = await channel.webhooks()
    if len(webhooks) != 0:
        for webhook in webhooks:
            if webhook.token is not None:
                return await webhook.send(content=message, username=name, avatar_url=avatar_url)
    web = await channel.create_webhook(name="Monke Bot Webhook Sender")
    await web.send(content=message, username=name, avatar_url=avatar_url)


def name(user: typing.Union[discord.Member, discord.User]):
    return user.name if user.nick is None else user.nick


async def get_raw_count(bot, payload):
    try:
        message = await bot.get_channel(payload.channel_id).fetch_message(payload.message_id)
    except discord.errors.NotFound:
        return 0
    for reaction in message.reactions:
        if str(reaction.emoji) == str(payload.emoji):
            return reaction.count
    return 0


async def to_string(c):
    digit = f'{ord(c):x}'
    return f'\\U{digit:>08}'


async def convert_emoji(ctx, emoji):
    try:
        emoji = await commands.EmojiConverter().convert(ctx, emoji)
    except commands.BadArgument:
        emoji = await to_string(emoji)
    finally:
        return str(emoji)


async def get_non_bot_members(guild):
    members = 0
    for member in guild.members:
        if not member.bot:
            members += 1
    return members
