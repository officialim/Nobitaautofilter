import asyncio
import time
import math
import os
import psutil
from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram.errors.exceptions.bad_request_400 import MessageTooLong, PeerIdInvalid
from info import ADMINS, LOG_CHANNEL, SUPPORT_CHAT, MELCOW_NEW_USERS, CHNL_LNK, GRP_LNK, NEWGRP
from database.users_chats_db import db
from database.ia_filterdb import Media
from utils import get_size, temp, get_settings
from Script import script
from pyrogram.errors import ChatAdminRequired

"""-----------------------------------------https://t.me/GetTGLink/4179 --------------------------------------"""
BOT_START_TIME = time.time()

@Client.on_message(filters.new_chat_members & filters.group)
async def save_group(bot, message):
    r_j_check = [u.id for u in message.new_chat_members]
    if temp.ME in r_j_check:
        if not await db.get_chat(message.chat.id):
            total=await bot.get_chat_members_count(message.chat.id)
            r_j = message.from_user.mention if message.from_user else "Anonymous" 
            await bot.send_message(LOG_CHANNEL, script.LOG_TEXT_G.format(a=message.chat.title, b=message.chat.id, c=message.chat.username, d=total, e=r_j, f=temp.B_LINK))       
            await db.add_chat(message.chat.id, message.chat.title)
        if message.chat.id in temp.BANNED_CHATS:
            # Inspired from a boat of a banana tree
            buttons = [[
                InlineKeyboardButton('Sᴜᴘᴘᴏʀᴛ', url=f'https://t.me/{SUPPORT_CHAT}')
            ]]
            reply_markup=InlineKeyboardMarkup(buttons)
            k = await message.reply(
                text='<b>🚫 CHAT NOT ALLOWED 🚫\n\nMʏ Aᴅᴍɪɴs Hᴀs Rᴇsᴛʀɪᴄᴛᴇᴅ Mᴇ Fʀᴏᴍ Wᴏʀᴋɪɴɢ Hᴇʀᴇ ! Iғ Yᴏᴜ Wᴀɴᴛ Tᴏ Kɴᴏᴡ Mᴏʀᴇ Aʙᴏᴜᴛ Iᴛ Cᴏɴᴛᴀᴄᴛ Sᴜᴘᴘᴏʀᴛ..</b>',
                reply_markup=reply_markup,
            )

            try:
                await k.pin()
            except:
                pass
            await bot.leave_chat(message.chat.id)
            return
        buttons = [[
                    InlineKeyboardButton('ᴜᴘᴅᴀᴛᴇs', url=CHNL_LNK),
                    InlineKeyboardButton('ʀᴇᴘᴏʀᴛ ʜᴇʀᴇ', url=f"https://t.me/Aks_support01_bot")
                  ]]
        reply_markup=InlineKeyboardMarkup(buttons)
        await message.reply_photo(
            photo=NEWGRP,
            caption=f"ᴛʜᴀɴᴋs ᴛᴏ ᴀᴅᴅ ᴍᴇ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ. {message.chat.title} ❣️\n\nɪs ᴀɴʏ ᴅᴏᴜʙᴛs ᴀʙᴏᴜᴛ ᴜsɪɴɢ ᴍᴇ ᴄʟɪᴄᴋ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴ 👇",
            reply_markup=reply_markup)
    else:
        settings = await get_settings(message.chat.id)
        if settings["welcome"]:
            for u in message.new_chat_members:
                buttons = [[
                InlineKeyboardButton("❌ ʀᴇᴀᴅ ɢʀᴏᴜᴘ ʀᴜʟᴇs ⁉️", url="http://t.me/MissRose_bot?start=rules_-1001500645086")
            ]]
                if (temp.MELCOW).get('welcome') is not None:
                    try:
                        await (temp.MELCOW['welcome']).delete()
                    except:
                        pass
                temp.MELCOW['welcome'] = await message.reply_photo(
                photo="https://telegra.ph/file/5cad86087b1bcd176f370.jpg",
                caption=f"🔖 ʜᴇʟʟᴏ ᴍʏ ғʀɪᴇɴᴅ {u.mention},\nᴡᴇʟᴄᴏᴍᴇ ᴛᴏ {message.chat.title} !\n\n ʀᴇᴀᴅ ɢʀᴏᴜᴘ ʀᴜʟᴇs ᴛᴏ ᴋɴᴏᴡ ᴍᴏʀᴇ...",
