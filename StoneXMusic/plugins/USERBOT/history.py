import asyncio
import random

from pyrogram import Client, filters
from pyrogram.raw.functions.messages import DeleteHistory
from pyrogram.types import Message

from StoneXMusic.core.userbot import assistants
from StoneXMusic.utils.database import get_client


@Client.on_message(filters.command(["sg", "History"], prefixes=["."]))
async def sg(client: Client, message: Message):

    if len(message.text.split()) < 2 and not message.reply_to_message:
        return await message.reply("sg username/id/reply")
    if message.reply_to_message:
        args = message.reply_to_message.from_user.id
    else:
        args = message.text.split()[1:]
        if not args:
            return await message.reply(
                "ᴘʟᴇᴀsᴇ ᴘʀᴏᴠɪᴅᴇ ᴀ ᴜsᴇʀɴᴀᴍᴇ, ɪᴅ, ᴏʀ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ."
            )
        args = args[0]
    lol = await message.reply("<code>ᴘʀᴏᴄᴇssɪɴɢ...</code>")
    if args:
        try:
            user = await client.get_users(f"{args}")
        except Exception:
            return await lol.edit("<code>ᴘʟᴇᴀsᴇ sᴘᴇᴄɪғʏ ᴀ ᴠᴀʟɪᴅ ᴜsᴇʀ!</code>")
    sgbot = ["sangmata_bot", "sangmata_beta_bot"]
    sg = random.choice(sgbot)
    Stone = random.choice(assistants)
    ubot = await get_client(Stone)

    try:
        a = await ubot.send_message(sg, f"{user.id}")
        await a.delete()
    except Exception as e:
        return await lol.edit(str(e))
    await asyncio.sleep(1)

    async for stalk in ubot.search_messages(a.chat.id):
        if stalk.text is None:
            continue
        if not stalk:
            await message.reply("@Ywr_stone")
        elif stalk:
            await message.reply(f"{stalk.text}")
            break

    try:
        user_info = await ubot.resolve_peer(sg)
        await ubot.send(DeleteHistory(peer=user_info, max_id=0, revoke=True))
    except Exception:
        pass

    await lol.delete()
