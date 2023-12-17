from __future__ import annotations
from datetime import timedelta, datetime, timezone
import logging
from typing import TYPE_CHECKING
import discord
from discord.ext import commands
from discord.ext.commands.errors import (
    NoPrivateMessage,
    NotOwner,
    ThreadNotFound,
    MissingRequiredArgument,
    BadArgument,
    UserInputError
)
if TYPE_CHECKING:
    from nixos_discord_bot import Bot

log = logging.getLogger(__name__)

class EventHandler(commands.Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx: commands.Context[Bot], error: commands.CommandError):
        ignored = (
            NotOwner,
            NoPrivateMessage,
            commands.CommandNotFound,
            commands.DisabledCommand,
        )
        if isinstance(error, ignored):
            return

        handlers = {
            MissingRequiredArgument: lambda: f"Missing `{error.param.name}` parameter", # type: ignore
            ThreadNotFound: lambda: f"Thread `{error.argument}` not found", # type: ignore
            BadArgument: lambda: "Bad argument",
            UserInputError: lambda: str(error),
        }

        for cls in error.__class__.__mro__: # type: ignore
            msg = handlers.get(cls)
            if msg is not None:
                return await ctx.send(msg())


        await ctx.send("\N{CHEERING MEGAPHONE} Something messed up, logged! \N{CHEERING MEGAPHONE}")
        log.error(f"{ctx.command.name} messed up (author: {ctx.author.id})", exc_info=error) # type: ignore


    @commands.Cog.listener()
    async def on_message_edit(self, before: discord.Message, after: discord.Message):
        # Add a time cap so people won't abuse this
        if datetime.now(timezone.utc) < after.created_at + timedelta(seconds=40):
            await self.bot.process_commands(after)






async def setup(bot: Bot):
    await bot.add_cog(EventHandler(bot))
