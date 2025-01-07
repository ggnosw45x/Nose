from pyrogram import Client, filters
from pyrogram.types import (
    Message,
    InlineKeyboardButton,
    InlineKeyboardMarkup
) 

@Client.on_callback_query(filters.regex("exit"))
async def exit(client, message):
    await message.edit_message_text("<b> Has cerrado el menu espero vuelvas pronto <3</b>",reply_markup=InlineKeyboardMarkup(
        [
            [
        
InlineKeyboardButton("Home",callback_data="home"),
                
            ]
            
        ]

    )
    
 )