
import asyncio
import importlib

from pyrogram import idle

import config
from config import BANNED_USERS
from StoneXMusic import LOGGER, app, userbot
from StoneXMusic.core.call import Stone
from StoneXMusic.misc import sudo
from StoneXMusic.plugins import ALL_MODULES
from StoneXMusic.plugins.tools.clone import restart_bots
from StoneXMusic.utils.database import get_banned_users, get_gbanned


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error(
            "ᴀssɪsᴛᴀɴᴛ ᴄʟɪᴇɴᴛ ᴠᴀʀɪᴀʙʟᴇs ɴᴏᴛ ᴅᴇғɪɴᴇᴅ, ᴇxɪᴛɪɴɢ..."
        )

    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            if user_id not in BANNED_USERS:
                BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("StoneXMusic.plugins" + all_module)
    LOGGER("StoneXMusic.plugins").info("sᴜᴄᴄᴇssғᴜʟʟʏ ɪᴍᴘᴏʀᴛᴇᴅ ᴍᴏᴅᴜʟᴇs...")

    await userbot.start()

    await Stone.start()
    await Stone.decorators()
    await restart_bots()
    LOGGER("StoneXMusic").info("\x43\x68\x61\x6D\x70\x75\x20\x42\x6F\x74\x20\x68\x61\x73\x20\x62\x65\x65\x6E\x20\x73\x75\x63\x63\x65\x73\x73\x66\x75\x6C\x6C\x79\x20\x73\x74\x61\x72\x74\x65\x64\x2E\x0A\x0A\x40\x54\x68\x65\x43\x68\x61\x6D\x70\x75\x20")
    await idle()

    await app.stop()
    await userbot.stop()

    LOGGER("StoneXMusic").info(
        " sᴛᴏᴘᴘɪɴɢ Stone ᴍᴜsɪᴄ ʙᴏᴛ..."
    )


if __name__ == "__main__":

    asyncio.get_event_loop().run_until_complete(init())
