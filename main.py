# Main
from core import Develop

import discord
try:
    from uvloop import install
except ImportError:
    pass
else:
    install()


intents = discord.Intents.all()
intents.typing = False # Disable typing events
bot = Develop(command_prefix="$", intents=intents)


if __name__ == "__main__":
    bot.run(bot.secret["token"])
