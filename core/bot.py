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
            await self.load_extension(f"cogs.{filename[:-2]}")

    async def on_ready(self) -> None:
        print("Start")

    async def close(self) -> None:
        await self.db.close()
        await super().close()

    async def is_owner(self, user: discord.User) -> bool:
        return await super().is_owner() or user.id in self.secret["owners"]
