from typing import Union
import discord
import os
import sys
import logging
from discord.ext import commands
from discord.ext.commands.errors import ChannelNotFound
from nixos_discord_bot import Bot


log = logging.getLogger(__name__)
discord.utils.setup_logging()


if "DISCORD_TOKEN" in os.environ:
    token = os.environ["DISCORD_TOKEN"]
elif "CREDENTIALS_DIRECTORY" in os.environ:
    with open(f'{os.environ["CREDENTIALS_DIRECTORY"]}/discord_token', "r") as f:
        token = f.readlines()[0].strip()
else:
    log.error("No token found in DISCORD_TOKEN or systemd credential discord_token")
    sys.exit(1)

bot = Bot()
bot.run(token)
