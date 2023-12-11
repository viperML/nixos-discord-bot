import sys
import os
import logging

import discord
from discord import app_commands
from discord.interactions import Interaction


def main() -> int:
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)
    command_tree = app_commands.CommandTree(client)
    discord.utils.setup_logging(level=logging.INFO, root=True)

    logger = logging.getLogger("client")
    info = logger.info

    @command_tree.command(name="move", description="Move a conversation")
    async def move(
        interaction: Interaction,
        channel: discord.TextChannel,
    ):

        await interaction.response.defer()
        message = await interaction.original_response()

        if ref := message.reference:
            await interaction.followup.send("Moving message")
        else:
            await interaction.followup.send("Please reply to a message to move it")


        pass

    @client.event
    async def on_ready():
        await command_tree.sync()
        info("Ready")



    token = os.environ["DISCORD_TOKEN"]
    info(f"Starting client (Token: {token})")
    client.run(token)

    return 0

if __name__ == "__main__":
    sys.exit(main())

