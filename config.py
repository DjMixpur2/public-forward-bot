import os
import logging
class Config:                                                                   
    API_ID = int(os.environ.get("API_ID", "12850056"))
    API_HASH = os.environ.get("API_HASH", "15564ec4a1a2cbef87c99a9aa9e40b34")       
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8178732396:AAEd104z69Wv0xQel_fgdWONINLHbKRBRIg")
    BOT_SESSION = os.environ.get("BOT_SESSION", "forwardbot")
    OWNER_ID = os.environ.get("OWNER_ID", "")                             
    DATABASE_URI = os.environ.get("DATABASE_URI", "")  
    DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluste0")
    COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'Data')
    SESSION = os.environ.get("SESSION", "")   
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", ""))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", "")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
