# Owner
from discord.ext import commands

from core import Develop, Cog

from typing import List


class Owner(Cog):
    def __init__(self, bot: Develop):
        self.bot = bot
        self.db = bot.db
        bot.secret["owners"] = [
            813028035980034059,
            947837418139189259,
            739702692393517076
        ]
    
    async def cog_load(self) -> None:
        await self.db.execute("CREATE TABLE IF NOT EXISTS owners (UserId BIGINT PRIMARY KEY)")
        await self.db.commit()

    @commands.command(description="ownerに変えます。")
    async def owner(self, ctx):
        if ctx.author.id not in self.bot.secret["owner"]:
            raise commands.NotOwner("オーナー権限がありません。")
        cursor = await self.db.execute("SELECT UserId FROM owners WHERE UserId = ?", (ctx.author.id,))
        if await cursor.fetchone() is None:
            await self.db.execute("INSERT INTO owners (UserId) VALUES (?)", (ctx.author.id,))
            await ctx.reply(embed=Cog.Embed(
                title="Owner", description="オーナー権限を付与しました。"
            ))
        else:
            await self.db.execute("DELETE FROM owners WHERE UserId = ?", (ctx.author.id,))
            await ctx.reply(embed=Cog.Embed(
                title="Owner", description="オーナー権限を剥奪しました。"
            ))
        await self.db.commit()

async def setup(bot: Develop) -> None:
    await bot.add_cog(Owner(bot))