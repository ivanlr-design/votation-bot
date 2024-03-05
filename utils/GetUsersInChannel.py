from discord.ext import commands
import discord

async def members(bot: commands.Bot, channelName : str):
    total_members = []
    for guild in bot.guilds:
        voice = discord.utils.get(guild.voice_channels, id=int(channelName))
        if voice:
            members = voice.members
            for member in members:
                user = discord.utils.get(guild.members, name=str(member.name))
                total_members.append(member.name)
    return total_members