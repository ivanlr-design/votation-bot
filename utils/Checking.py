import time
from discord.ext import commands
import discord

def Check(message, timeout=30):
    time.sleep(timeout)

    kick = False
    Count1 = 0
    Count2 = 0
    for reaction in message:
        if str(reaction.emoji) == "👍":
            Count1 += reaction.count
        elif str(reaction.emoji) == "👎":
            Count2 += reaction.count 

    if Count1 > Count2:
        return True
    else:
        return False
        