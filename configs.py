from os import path, getenv
#en api id y hash no tocar 
class Config:
    API_ID = int(getenv('API_ID','21187534')) # Coloque el API ID del Telegram Cuenta
    API_HASH = getenv('API_HASH','50a7a5d0da3b6ca49da582c84732a8ef') # Coloque el API HASH del Telegram Cuenta
    BOT_TOKEN = getenv('BOT_TOKEN','5799910541:AAH3ZlLlfNu64rixpRaEf5xmvh0AslY5TH0') #Coloque el TOKEN DEL BOT de @BotFather
 #En las comillas tiene que ir tu token del bot 

config = Config()
