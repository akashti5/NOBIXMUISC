from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(filters.command("help") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Contact me in PM to get help of possible commands ⁉️**""",
      reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                text="Help",
                                url="t.me/Music_op_bot?start=ghelp_{}".format(
                                    context.bot.username, module,
                                ),
                            ),
                        ],
                    ],
                ),
            )
