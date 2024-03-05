from discord.ext import commands
import discord

def clear(bot : commands.Bot, channel_id):
    for guild in bot.guilds:
        voice = discord.utils.get(guild.voice_channels, id=int(channel_id))
        if voice:
            members = voice.members
            for member in members:
                user = discord.utils.get(guild.members, name=str(member.name))
                user.move_to(None)
    