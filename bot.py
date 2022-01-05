import os

from discord.ext import commands

def main():
    client = commands.Bot(command_prefix="?")

    @client.event
    async def on_ready():
        print(f"{client.user.name} has connected to Discord.")

    @client.command()
    async def ping(ctx):
        await ctx.send("Pong")

    client.run("OTI3ODEzODk2NDUzMTIwMDMw.YdPsBg.UAQx5DiIh5uVxdKsVkuDHb0MC3M")

if __name__ == '__main__':
    main()
