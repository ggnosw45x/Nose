from os import path, getenv
#en api id y hash no tocar 
class Config:
    API_ID = int(getenv('API_ID','16650069')) # Coloque el API ID del Telegram Cuenta
    API_HASH = getenv('API_HASH','a4373bc737d0c78881d48dd62eed7268') # Coloque el API HASH del Telegram Cuenta
    BOT_TOKEN = getenv('BOT_TOKEN','7807495947:AAGvrDQJ0WpnjXLFPhkDsdOB6ql2m7rN0hc') #Coloque el TOKEN DEL BOT de @BotFather
 #En las comillas tiene que ir tu token del bot 

config = Config()
