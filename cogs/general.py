from core import Develop

from discord.ext import commands


class General(commands.Cog):
    def __init__(self, bot: Develop):
        self.bot = bot

    @commands.command(description="botの速さを表示します。")
    async def ping(self, ctx):
        await ctx.reply(embed=Cog.Embed(
            title="Ping", description=f"{round(self.bot.latency * 1000, 2)}ms"
        ))


async def setup(bot: Develop) -> None:
    await bot.add_cog(General(bot))
