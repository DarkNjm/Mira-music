# MIT License
#
# Copyright (c) 2023 AnonymousX1025
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import asyncio
import importlib
import os

from pyrogram import idle

from FallenMusic import (
    ASS_ID,  # معرف المساعد
    ASS_NAME,  # اسم المساعد
    ASS_USERNAME,  # اسم المستخدم للمساعد
    BOT_ID,  # معرف البوت
    BOT_NAME,  # اسم البوت
    BOT_USERNAME,  # اسم المستخدم للبوت
    LOGGER,  # المسجل
    SUNAME,  # اسم المستخدم
    app,  # التطبيق
    app2,  # التطبيق 2
    pytgcalls,  # المكالمات الصوتية
)
from FallenMusic.Modules import ALL_MODULES  # جميع الوحدات


async def fallen_startup():
    LOGGER.info("[•] جاري تحميل الوحدات...")
    for module in ALL_MODULES:
        importlib.import_module("FallenMusic.Modules." + module)
    LOGGER.info(f"[•] تم تحميل {len(ALL_MODULES)} وحدة.")

    LOGGER.info("[•] جاري تحديث المجلدات...")
    if "downloads" not in os.listdir():
        os.mkdir("downloads")
    if "cache" not in os.listdir():
        os.mkdir("cache")
    LOGGER.info("[•] تم تحديث المجلدات.")

    try:
        await app.send_message(
            SUNAME,
            f"✯ بوت فالين ميوزيك ✯\n\n𖢵 المعرف : `{BOT_ID}`\n𖢵 الاسم : {BOT_NAME}\n𖢵 اسم المستخدم : @{BOT_USERNAME}",
        )
    except:
        LOGGER.error(
            f"{BOT_NAME} فشل في إرسال الرسالة إلى @{SUNAME}, يرجى التحقق."
        )

    try:
        await app2.send_message(
            SUNAME,
            f"✯ ميرا ميوزيك ✯\n\n𖢵 المعرف : `{ASS_ID}`\n𖢵 الاسم : {ASS_NAME}\n𖢵 اسم المستخدم : @{ASS_USERNAME}",
        )
    except:
        LOGGER.error(
            f"{ASS_NAME} فشل في إرسال الرسالة إلى @{SUNAME}, يرجى التحقق."
        )

    await app2.send_message(BOT_USERNAME, "/start")

    LOGGER.info(f"[•] بدأ البوت باسم {BOT_NAME}.")
    LOGGER.info(f"[•] بدأ المساعد باسم {ASS_NAME}.")

    LOGGER.info(
        "[•] \x53\x74\x61\x72\x74\x69\x6e\x67\x20\x50\x79\x54\x67\x43\x61\x6c\x6c\x73\x20\x43\x6c\x69\x65\x6e\x74\x2e\x2e\x2e"
    )
    await pytgcalls.start()
    await idle()


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(fallen_startup())
    LOGGER.error("تم ايقاف بوت ميرا ميوزك.")
