from os import path

from pyrogram import Client
from pyrogram.types import Message, Voice

from callsmusic import callsmusic, queues

import converter
from downloaders import youtube

from config import BOT_NAME as bn, DURATION_LIMIT
from helpers.filters import command, other_filters
from helpers.decorators import errors
from helpers.errors import DurationLimitError
from helpers.gets import get_url, get_file_name
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

@Client.on_message(command("aud") & other_filters)
@errors
async def play(_, message: Message):

    lel = await message.reply("๐ **๐๐๐๐๐๐๐๐๐๐**")
    sender_id = message.from_user.id
    sender_name = message.from_user.first_name

    keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="๐ฅ[เคฆเฅเคธเฅ ฮฯดแดแอฒแช]๐ฅ",
                        url="https://t.me/DesiNobita")
                   
                ]
            ]
        )

    audio = (message.reply_to_message.audio or message.reply_to_message.voice) if message.reply_to_message else None
    url = get_url(message)

    if audio:
        if round(audio.duration / 60) > DURATION_LIMIT:
            raise DurationLimitError(
                f"โ {DURATION_LIMIT} mere land se bada video..๐ฎ mai nhi play karta ja..๐"
            )

        file_name = get_file_name(audio)
        file_path = await converter.convert(
            (await message.reply_to_message.download(file_name))
            if not path.isfile(path.join("downloads", file_name)) else file_name
        )
    elif url:
        file_path = await converter.convert(youtube.download(url))
    else:
        return await lel.edit_text("โ Abey Kya Play Karu Teri GF Ki Recordings ? ๐")

    if message.chat.id in callsmusic.pytgcalls.active_calls:
        position = await queues.put(message.chat.id, file=file_path)
        await lel.edit(f"#โฃ **Queued** at position {position}!")
    else:
        callsmusic.pytgcalls.join_group_call(message.chat.id, file_path)
        await message.reply_photo(
        photo="https://telegra.ph/file/dda3be3c41d3d7d2f3799.jpg",
        reply_markup=keyboard,
        caption="โถ๏ธ **Playing** here the song requested by๐ฅ{}!".format(
        message.from_user.mention()
        ),
    )
        return await lel.delete()
