from discord.ext import commands
import discord


class Cog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    class Embed(discord.Embed):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            self.color = 0x198754
        
        @classmethod
        def error(cls, **kwargs):
            embed = cls(**kwargs)
            embed.color = 0xdc3545
            return embed