from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ Creator : <a href='tg://user?id={OWNER_ID}'>moon</a>\n○ Language : <code>Python3</code>\n○ Library : <a href='https://t.me/+nDTaoJGRKJcxYmZl'>Library</a>\n○ movie channel : <a href='https://t.me/Hindi_Dub_Netflix_Movies'>Click here</a>\n○ Channel : @Hindi_Dub_Animes_Official</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("❗❗𝐂𝐋𝐎𝐒𝐄❗❗", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
