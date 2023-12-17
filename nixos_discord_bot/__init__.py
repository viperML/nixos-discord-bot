import discord
from discord.ext import commands

class Bot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(
            command_prefix=commands.when_mentioned_or("$"),
            help_command=commands.MinimalHelpCommand(),
            allowed_mentions=discord.AllowedMentions(
                everyone=False,
                roles=False,
                users=False,
                replied_user=True,
            ),
            intents=intents,
            description="official unofficial nixos discord bot",
        )

    async def setup_hook(self):
        extensions = [
            "nixos_discord_bot.exts.handler",
            "nixos_discord_bot.exts.meta",
        ]

        for ext in extensions:
            await self.load_extension(ext)

        # Optional, used for debugging
        try:
            await self.load_extension("jishaku")
        except commands.ExtensionNotFound:
            pass


