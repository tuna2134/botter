from discord.ext import commands
import discord
from orjson import loads
from aiosqlite import connect

from os import listdir

from typing import TypedDict, List


class Secret(TypedDict):
    token: str
    owners: List[int]

class Develop(commands.Bot):
    with open("secret.json", "r") as f:
        secret: Secret = loads(f.read())

    async def setup_hook(self) -> None:
        await self.load_extension("jishaku")
        self.db = await connect("main.db")
        for filename in listdir("cogs"):
            if filename.startswith("_"):
                continue
            await self.load_extension(f"cogs.{filename[:-3]}")

    async def on_ready(self) -> None:
        print("Start")

    async def close(self) -> None:
        await super().close()
        try:
            await self.db.close()
        except AttributeError:
            pass

    async def is_owner(self, user: discord.User | discord.Member) -> bool:
        return await super().is_owner(user) or user.id in self.secret["owners"]
