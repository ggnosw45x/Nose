from configss._def_main_ import *


@Client.on_message(filters.command(["me", "yo", "myacc", "plan", "my"], [".", "/", "$", "-", "_", "|"]))
async def start(client, m: Message):
    rank = get_user_rank(m.from_user.id)
    await m.reply(f"""<b>┏━━━━━━━━━━━━━━━━━━━━━━━━━━
┣ ━━━━━ • 𝗧𝗨 𝗜𝗡𝗙𝗢 • ━━━━━━━
┣ • 𝙄𝙙 ➨{m.from_user.id}</code>
┣ • 𝙐𝙨𝙚𝙧 ➨@{m.from_user.username} </code>
┣ • 𝗥𝙖𝙣𝗴𝙤 ➨{rank}</b>
┗━━━━━━━━━━━━━━━━━━━━━━━━━
     """,
    reply_markup=InlineKeyboardMarkup(
        [
            [
        
                InlineKeyboardButton("𝘾𝙈𝘿𝙎", callback_data="home"),
                InlineKeyboardButton("𝙀𝙓𝙄𝙏", callback_data="exit"),
        ],
        [        
                InlineKeyboardButton("𝙍𝙀𝙁𝙀𝙍𝙀𝙉𝘾𝙄𝘼", url="t.me/referencias_pain_chk_bot"),
            ]
            
        ]

    )
    
 )

