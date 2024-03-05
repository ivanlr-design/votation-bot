from discord import app_commands
from utils.GetUsersInChannel import members
from discord.ext import commands
from utils import Checking
from utils.Disconnect import Disconnect
from dotenv import load_dotenv, dotenv_values
import discord
import os
import time
# test
load_dotenv(".env")

TOKEN = os.getenv("TOKEN")

bot = commands.Bot(command_prefix="!",intents=discord.Intents.all())

@bot.event
async def on_ready():
    await bot.tree.sync()

@bot.tree.command(name="vote",description="vote to KICK a user")
async def vote(interaction: discord.Interaction, iddelcanal: str, user: str):
    
    try:
        iddelcanal = int(iddelcanal)
        username = str(user)
        guild = interaction.guild
        user = discord.utils.get(guild.members, name=username)
        if user:
            voice = discord.utils.get(guild.voice_channels, id=int(iddelcanal))
            if voice:
                users = await members(bot,str(iddelcanal))
                found = False
                for user in users:
                    if user.lower() == username.lower():
                        found = True

                if found == False:
                    embed = discord.Embed(title="VOTE",description=f"No encontré el usuario: {username} en el canal de voz: {iddelcanal} dentro del servidor",color=discord.Color.red())
                    await interaction.response.send_message(embed=embed)
                    return 
                else:
                    await interaction.response.send_message("votacion en curso")
                    channel = bot.get_channel(interaction.channel_id)
                    embed = discord.Embed(title="VOTE",description=f"Quieres darle F1 al usuario: {username} en el canal de voz: {iddelcanal} ?",color=discord.Color.orange())
                    msj = await channel.send(embed=embed)
                    await msj.add_reaction("👍")
                    await msj.add_reaction("👎")
                
                    time.sleep(5)
                    msg = await msj.channel.fetch_message(msj.id)

                    kick = Checking.Check(msg.reactions, 5)
                    if kick == True:
                        await msj.clear_reactions()
                        embed = discord.Embed(title="DISCONNECT",description=f"```Al usuario : {username} le han dado F1 por subnormal```",color=discord.Color.green())
                        await msj.edit(embed=embed)
                        await Disconnect(bot, username)
                    else:
                        await msj.clear_reactions()
                        embed = discord.Embed(title="DISCONNECT",description=f"```Al usuario : {username} no le dieron F1 :)```",color=discord.Color.green())
                        await msj.edit(embed=embed)
                    
                    time.sleep(5)
                    await msj.delete()
            else:
                embed = discord.Embed(title="VOTE",description=f"No encontré el canal de voz: {iddelcanal} dentro del servidor",color=discord.Color.red())
                await interaction.response.send_message(embed=embed)
                return 
        else:
            embed = discord.Embed(title="VOTE",description=f"No encontramos al usuario: {username} dentro del servidor",color=discord.Color.red())
            await interaction.response.send_message(embed=embed)
            return 

    except Exception as e:
        print(e.with_traceback())

bot.run(TOKEN)
