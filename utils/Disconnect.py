from discord.ext import commands
import discord

async def Disconnect(bot: commands.Bot, username : str):
    for guild in bot.guilds:
        user = discord.utils.get(guild.members, name=str(username))
        if user:
            await user.move_to(None)
