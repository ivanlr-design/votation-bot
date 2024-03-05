import os
import datetime

def GetTime():
    now = datetime.datetime.now()

    return now.strftime("%d/%m/%Y %H:%M")

def Success(log : str):
    if os.path.exists("Logs.txt"):
        with open("Logs.txt","a") as file:
            file.write(f"[SUCCESS] ({GetTime()}): {log}\n")
    else:
        return

def Info(log : str):
    if os.path.exists("Logs.txt"):
        with open("Logs.txt","a") as file:
            file.write(f"[INFO] ({GetTime()}): {log}\n")
    else:
        return

def Error(log : str):
    if os.path.exists("Logs.txt"):
        with open("Logs.txt","a") as file:
            file.write(f"[ERROR] ({GetTime()}): {log}\n")
    else:
        return