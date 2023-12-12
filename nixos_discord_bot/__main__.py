import sys
import os
import logging

import discord
from discord.ext import commands
from discord.ext.commands import Context
from discord import Embed


def main() -> int:
    intents = discord.Intents.default()
    intents.message_content = True

    logger = logging.getLogger("bot")
    info = logger.info
    discord.utils.setup_logging(level=logging.INFO, root=True)

    bot = commands.Bot(command_prefix="$", intents=intents)

    async def fail(ctx: Context, description: str):
        info(f"Failed: {description}")
        await ctx.send(
            embed=Embed(
                title="Error",
                description=description
            )
        )

    @bot.command(help="Move a conversation to another channel")
    async def move(ctx: Context):
        if target_ref := ctx.message.reference:
            if len(ctx.message.channel_mentions) == 1:
                target_channel = ctx.message.channel_mentions[0]
                target_message = await ctx.fetch_message(target_ref.message_id)

                embed=Embed(
                    description=f"""
                        {target_message.content}

                        Original message: {target_message.jump_url}
                    """,
                )
                if avatar := target_message.author.avatar:
                    embed.set_author(name=target_message.author.display_name, icon_url=avatar.url)
                await target_channel.send(embed=embed)

                await ctx.channel.send(embed=Embed(
                    title="Moving conversation",
                    description=f"Please continue in {target_channel.mention}"
                ))
            else:
                await fail(ctx, "Please mention a channel to move the message to.")
        else:
            await fail(ctx, "Pleas mention a message to move.")

    @bot.event
    async def on_ready():
        info("Ready")


    if "DISCORD_TOKEN" in os.environ:
        token = os.environ["DISCORD_TOKEN"]
    elif "CREDENTIALS_DIRECTORY" in os.environ:
        with open(f'{os.environ["CREDENTIALS_DIRECTORY"]}/discord_token', "r") as f:
            token = f.readlines()[0].strip()
    else:
        logger.error("No token found in DISCORD_TOKEN or systemd credential discord_token")
        sys.exit(1)

    info(f"Starting client")
    bot.run(token)

    return 0

if __name__ == "__main__":
    sys.exit(main())

