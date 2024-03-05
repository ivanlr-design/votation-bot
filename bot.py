from discord import app_commands
from utils.GetUsersInChannel import members
from discord.ext import commands
from utils import Checking
from utils.Log import Handler
from utils.Disconnect import Disconnect
from dotenv import load_dotenv, dotenv_values
import discord
import os
import time
import pymysql
import pymysql.cursors

# Load variables
load_dotenv(".env")

TOKEN = os.getenv("TOKEN")
MysqlUser = os.getenv("MYSQL_USER")
MysqlPass = os.getenv("MYSQL_PASSWORD")
Connection = os.getenv("MYSQL_CONNECTION")
Schema = os.getenv("SCHEMA")

def db_connection():
    try:
        connection = pymysql.connect(host=Connection, user=MysqlUser, password=MysqlPass, db=Schema, charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
        Handler.Success("Succesfully created connexion")
        return connection
    except Exception as e:
        Handler.Error(f"ERROR MAKING DB CONEXION : {str(e)}")

bot = commands.Bot(command_prefix="!",intents=discord.Intents.all())

@bot.event
async def on_ready():
    try:
        connection = db_connection()
        if not os.path.exists("Logs.txt"):
            with open("Logs.txt","w") as file:
                file.close()
        await bot.tree.sync()
    except Exception as e:
        Handler.Error(f"ERROR MAKING DB CONEXION : {str(e)}")

@bot.tree.command(name="dumplogs",description="dumps logs")
async def dumplogs(interaction: discord.Interaction):
    try:
        if str(interaction.user.name) != "ivanlr._1_45557":
            embed = discord.Embed(title=F"SIN ACCESO",description=f"El unico que tiene acceso a esta funcion es el propio developer, es una funcion para obtener los logs y poder fixear cosas :)")
            await interaction.response.send_message(embed=embed)
            return
        
        # Cargar el archivo
        with open("Logs.txt","rb") as file:
            archivo = discord.File(file)
        
        user = discord.utils.get(interaction.guild.members, name=str(interaction.user.name))
        if user:
            await user.send("LOG DUMP",file=archivo)
            Handler.Success(f"Succesfully sent logs to: {str(interaction.user.name)}")
            await interaction.response.send_message("sent")
    except Exception as e:
        Handler.Error(f"ERROR MAKING DB CONEXION : {str(e)}")

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
                    embed = discord.Embed(title="VOTE",description=f"Quieres darle F1 al usuario: {username} en el canal de voz: {voice.name} ?",color=discord.Color.orange())
                    msj = await channel.send(embed=embed)
                    await msj.add_reaction("👍")
                    await msj.add_reaction("👎")
                
                    time.sleep(5)
                    msg = await msj.channel.fetch_message(msj.id)

                    kick = Checking.Check(msg.reactions, 5)
                    if kick == True:
                        await msj.clear_reactions()
                        Handler.Success(F"USER : {username} was kicked from: {voice.name}")
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
        Handler.Error(f"ERROR MAKING DB CONEXION : {str(e)}")

bot.run(TOKEN)
