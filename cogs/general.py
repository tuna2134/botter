from core import Develop, Cog

from discord.ext import commands

import traceback


class General(Cog):
    def __init__(self, bot: Develop):
        self.bot = bot

    @commands.command(description="botの速さを表示します。")
    async def ping(self, ctx):
        await ctx.reply(embed=Cog.Embed(
            title="Ping", description=f"{round(self.bot.latency * 1000, 2)}ms"
        ))

    @Cog.listener("on_command_error")
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            embed = Cog.Embed.error(
                title="Error", description="コマンドが見つかりませんでした。"
            )
        elif isinstance(error, commands.NotOwner):
            embed = Cog.Embed.error(
                title="Error", description="オーナー権限がありません。"
            )
        else:
            traceback.print_exc(error)
            embed = Cog.Embed.error(
                title="Error", description=(
                    "予期せぬエラーが発生しました。\n"
                    f"```py\n{traceback.format_exc(error)}\n```"
                )
            )
        await ctx.reply(embed=embed)


async def setup(bot: Develop) -> None:
    await bot.add_cog(General(bot))
