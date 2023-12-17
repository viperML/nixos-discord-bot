import logging
import os
import sys

from nixos_discord_bot import Bot

log = logging.getLogger(__name__)

def run() -> int:
    if "DISCORD_TOKEN" in os.environ:
        token = os.environ["DISCORD_TOKEN"]
    elif "CREDENTIALS_DIRECTORY" in os.environ:
        with open(f'{os.environ["CREDENTIALS_DIRECTORY"]}/discord_token', "r") as f:
            token = f.readlines()[0].strip()
    else:
        log.error("No token found in DISCORD_TOKEN or systemd credential discord_token")
        return 1
    bot = Bot()
    bot.run(token, root_logger=True)
    return 0

if __name__ == '__main__':
    sys.exit(run())
