import os
import logging
class Config:                                                                   
    API_ID = int(os.environ.get("API_ID", "12850056"))
    API_HASH = os.environ.get("API_HASH", "15564ec4a1a2cbef87c99a9aa9e40b34")       
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8178732396:AAEd104z69Wv0xQel_fgdWONINLHbKRBRIg")
    BOT_SESSION = os.environ.get("BOT_SESSION", "forwardbot")
    OWNER_ID = os.environ.get("OWNER_ID", "770434685")                             
    DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://Kdbhai:Kdbhai@cluster0.qxasr.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")  
    DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluste0")
    COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'Data')
    SESSION = os.environ.get("SESSION", "Forward")   
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1002260661088"))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", "MovieJungle_Bot")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
