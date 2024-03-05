import datetime

def GetTime():
    now = datetime.datetime.now()

    return now.strftime("%d/%m/%Y %H:%M")