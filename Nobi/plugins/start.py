from Nobi import Nobi, BOT_USERNAME
from Config import Config
from telethon import events, Button

PM_START_TEXT = """
ʜᴇʏᴀ! {}

• ɪ'ᴍ ᴀ ꜱɪᴍᴘʟᴇ ᴛᴇʟᴇɢʀᴀᴍ ᴍᴜꜱɪᴄ ʙᴏᴛ.
• ɪ ᴄᴀɴ ᴘʟᴀʏ ꜱᴏɴɢꜱ ɪɴ ʏᴏᴜʀ ᴠᴏɪᴄᴇ.
• ᴛʜɪꜱ ʙᴏᴛ ʙᴀꜱᴇᴅ ᴏɴ ᴛᴇʟᴇᴛʜᴏɴ. ꜱᴏ ɪᴛ'ꜱ ᴘʀᴏᴠɪᴅᴇ ᴍᴏʀᴇ ꜱᴛᴀʙɪʟɪᴛʏ ꜰʀᴏᴍ ᴏᴛʜᴇʀ ʙᴏᴛꜱ!
• ɪ ᴄᴀɴ ᴅᴏ ᴏᴛʜᴇʀ ᴛʜɪɴɢꜱ ʟɪᴋᴇ ᴘɪɴꜱ ᴇᴛᴄꜱ.

➻ **ᴄʟɪᴄᴋ ᴏɴ ʜᴇʟᴘ ʙᴜᴛᴛᴏɴ ꜰᴏʀ ᴍᴏʀᴇ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ**.
"""

@Nobi.on(events.NewMessage(pattern="^[/!?]start$"))
async def start(event):
    if Config.MANAGEMENT_MODE == "ENABLE":
        return
    if event.is_private:
       await event.client.send_file(event.chat_id,
             Config.START_IMG,
             caption=PM_START_TEXT.format(event.sender.first_name), 
             buttons=[
        [Button.url("✨ 𝑨𝒅𝒅 𝑴𝒆 ✨", f"https://telegram.me/{BOT_USERNAME}?startgroup=true"), Button.inline("🥀 𝑯𝒆𝒍𝒑 🥀", data="help") , Button.url("💞 𝑴𝒚 𝑴𝒂𝒔𝒕𝒆𝒓 💞", "https://telegram.me/Radhe_krishna_hare_hare"), Button.url("🏫 𝑶𝒇𝒇𝒊𝒄𝒆 🏫", "https://telegram.me/The_nobita_support") , Button.url("🆂🆄🅿🅿🅾🆁🆃 🅲🅷🅰🆃", "https://telegram.me/INDIAN_CHATING_CLUB")]])
       return

    if event.is_group:
       await event.reply("**ʜᴇʏ! ɪ'ᴍ ꜱᴛɪʟʟ ᴀʟɪᴠᴇ ✅**")
       return



@Nobi.on(events.callbackquery.CallbackQuery(data="start"))
async def _(event):
    if Config.MANAGEMENT_MODE == "ENABLE":
        return
    if event.is_private:
       await event.edit(PM_START_TEXT.format(event.sender.first_name), buttons=[
        [Button.url("✨ ᴀᴅᴅ ᴍᴇ", f"https://telegram.me/{BOT_USERNAME}/startgroup=true"), Button.inline("🥀 ʜᴇʟᴘ", data="help")]])
       return
