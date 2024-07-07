from pyrogram import Client, filters
from pyrogram.types import Message

from config import BANNED_USERS
from StoneXMusic.core.call import Stone
from StoneXMusic.utils.database import set_loop
from StoneXMusic.utils.decorators import AdminRightsCheck
from StoneXMusic.utils.inline import close_markup


@Client.on_message(
    filters.command(
        ["end", "stop", "cend", "cstop"],
        prefixes=["/", "!", "%", ",", "", ".", "@", "#"],
    )
    & filters.group
    & ~BANNED_USERS
)
@AdminRightsCheck
async def stop_music(cli, message: Message, _, chat_id):
    if not len(message.command) == 1:
        return
    await Stone.stop_stream(chat_id)
    await set_loop(chat_id, 0)
    await message.reply_text(
        _["admin_5"].format(message.from_user.mention), reply_markup=close_markup(_)
    )
