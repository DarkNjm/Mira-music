import asyncio

from pyrogram import Client, __version__ as ver


API_ID = input("\nأدخل API ID الخاص بك :\n > ")
API_HASH = input("\nأدخل API HASH الخاص بك :\n > ")

print("\n\nأدخل رقم الهاتف المرتبط بحسابك على تيليجرام عندما يُطلب منك.\n\n")

fallen = Client("Fallen", api_id=API_ID, api_hash=API_HASH, in_memory=True)


async def main():
    await fallen.start()
    sess = await fallen.export_session_string()
    txt = f"إليك سلسلة الجلسة الخاصة بك باستخدام Pyrogram {ver}\n\n<code>{sess}</code>\n\nلا تشاركها مع أي شخص.\nلا تنسى الانضمام إلى @FallenAssociation"
    ok = await fallen.send_message("me", txt)
    print(f"إليك سلسلة الجلسة الخاصة بك باستخدام Pyrogram {ver}\n{sess}\nانقر مرتين لنسخها.") 


asyncio.run(main())
