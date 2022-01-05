import discord
from discord.ext import commands
import os



def main():
    client = commands.Bot(command_prefix="?")

    @client.event
    async def on_ready():
        print(f"{client.user.name} has connected to Discord.")

    @client.command()
    async def ping(ctx):
        await ctx.send("Pong")

    client.run("MySecret")

if __name__ == '__main__':
    main()
