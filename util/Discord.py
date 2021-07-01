import discord


async def webhook_send(channel: discord.TextChannel, message: str, *, avatar_url: str, name: str):
    webhooks = await channel.webhooks()
    if len(webhooks) != 0:
        for webhook in webhooks:
            if webhook.token is not None:
                return await webhook.send(content=message, username=name, avatar_url=avatar_url)
    web = await channel.create_webhook(name="Monke Bot Webhook Sender")
    await web.send(content=message, username=name, avatar_url=avatar_url)
