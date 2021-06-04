from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(filters.command("help") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**𝐂𝐎𝐍𝐓𝐀𝐂𝐓 𝐌𝐄 𝐈𝐍 𝐏𝐌 𝐓𝐎 𝐆𝐄𝐓 𝐇𝐄𝐋𝐏 𝐎𝐅 𝐏𝐎𝐒𝐒𝐈𝐁𝐋𝐄 𝐂𝐎𝐌𝐌𝐀𝐍𝐃𝐒 ⁉️**""",
      reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                text="Help",
                                url="t.me/NoBi_vC_PlAyEr_RoBoT?start=ghelp_{}".format(
                                    context.bot.username, module,
                                ),
                            ),
                        ],
                    ],
                ),
            )
