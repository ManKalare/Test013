import os
import re
import sys
import json
import time
import asyncio
import requests
import subprocess
import core as helper
from utils import progress_bar
#from vars import api_id, api_hash, bot_token
from aiohttp import ClientSession
from pyromod import listen
from subprocess import getstatusoutput
from os import environ
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import FloodWait
from pyrogram.errors.exceptions.bad_request_400 import StickerEmojiInvalid
from pyrogram.types.messages_and_media import message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


bot = Client("bot",
             bot_token= "6759014088:AAE8yMeNKRIeuahOcrs7LLWjS_7ijO-LoFs",
             api_id= 25038096,
             api_hash= "098112aae38be62db58363267a061b59")


@bot.on_message(filters.command(["start"]))
async def account_login(bot: Client, m: Message):
    editable = await m.reply_text("Hello, **Nikhil Jha**! 🌟\n\n I am your friendly bot 🤖, here to help you download links from your **.txt** file and upload them to Telegram. To get started, simply send me the /Homelander command and follow a few easy steps.")

@bot.on_message(filters.command("stop"))
async def restart_handler(_, m):
    await m.reply_text("**Stopped**🚫", True)
    os.execl(sys.executable, sys.executable, *sys.argv)

@bot.on_message(filters.command(["Homelander"]))
async def account_login(bot: Client, m: Message):
    editable = await m.reply_text('𝐓𝐨 𝐝𝐨𝐰𝐧𝐥𝐨𝐚𝐝 𝐚 𝐭𝐞𝐱𝐭 𝐟𝐢𝐥𝐞, 𝐬𝐞𝐧𝐝 𝐢𝐭 𝐡𝐞𝐫𝐞.⚡️')
    input: Message = await bot.listen(editable.chat.id)
    x = await input.download()
    await input.delete(True)
    path = f"./downloads/{m.chat.id}"

    try:
       with open(x, "r") as f:
           content = f.read()
       content = content.split("\n")
       links = []
       for i in content:
           links.append(i.split("://", 1))
       os.remove(x)
            # print(len(links)
    except:
           await m.reply_text("**Invalid file input.**")
           os.remove(x)
           return
    
    await editable.edit(f"**𝐓𝐨𝐭𝐚𝐥 𝐋𝐢𝐧𝐤𝐬 𝐟𝐨𝐮𝐧𝐝 𝐚𝐫𝐞🔗** **{len(links)}**\n\n**𝐒𝐞𝐧𝐝 𝐅𝐫𝐨𝐦 𝐖𝐡𝐞𝐫𝐞 𝐘𝐨𝐮 𝐖𝐚𝐧𝐭 𝐓𝐨 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝 𝐈𝐧𝐢𝐭𝐢𝐚𝐥 𝐈𝐬** **1**")
    input0: Message = await bot.listen(editable.chat.id)
    raw_text = input0.text
    await input0.delete(True)

    await editable.edit("**𝐍𝐨𝐰 𝐏𝐥𝐞𝐚𝐬𝐞 𝐒𝐞𝐧𝐝 𝐌𝐞 𝐘𝐨𝐮𝐫 𝐁𝐚𝐭𝐜𝐡 𝐍𝐚𝐦𝐞**")
    input1: Message = await bot.listen(editable.chat.id)
    raw_text0 = input1.text
    await input1.delete(True)

    await editable.edit("**𝐄𝐧𝐭𝐞𝐫 𝐑𝐞𝐬𝐨𝐥𝐮𝐭𝐢𝐨𝐧📸**\n\n144\n240\n360\n480\n720\n1080\n\n **𝐏𝐥𝐞𝐚𝐬𝐞 𝐂𝐡𝐨𝐨𝐬𝐞 𝐐𝐮𝐚𝐥𝐢𝐭𝐲**")
    input2: Message = await bot.listen(editable.chat.id)
    raw_text2 = input2.text
    await input2.delete(True)
    try:
        if raw_text2 == "144":
            res = "256x144"
        elif raw_text2 == "240":
            res = "426x240"
        elif raw_text2 == "360":
            res = "640x360"
        elif raw_text2 == "480":
            res = "854x480"
        elif raw_text2 == "720":
            res = "1280x720"
        elif raw_text2 == "1080":
            res = "1920x1080" 
        else: 
            res = "UN"
    except Exception:
            res = "UN"

    await editable.edit("𝐍𝐨𝐰 𝐄𝐧𝐭𝐞𝐫 𝐀 𝐍𝐚𝐦𝐞 𝐭𝐨 𝐚𝐝𝐝 𝐜𝐚𝐩𝐭𝐢𝐨𝐧 𝐨𝐧 𝐲𝐨𝐮𝐫 𝐮𝐩𝐥𝐨𝐚𝐝𝐞𝐝 𝐟𝐢𝐥𝐞")
    input3: Message = await bot.listen(editable.chat.id)
    raw_text3 = input3.text
    await input3.delete(True)
    highlighter  = f"️ ⁪⁬⁮⁮⁮"
    if raw_text3 == 'robin':
        MR = highlighter 
    else:
        MR = raw_text3

    await editable.edit("Now send the Thumb url/nEg » https://telegra.ph/file/289af3c1accf576e359b1.jpg \n Or if don't want thumbnail send = no")
    input6 = message = await bot.listen(editable.chat.id)
    raw_text6 = input6.text
    await input6.delete(True)
    await editable.delete()

    thumb = input6.text
    if thumb.startswith("http://") or thumb.startswith("https://"):
        getstatusoutput(f"wget '{thumb}' -O 'thumb.jpg'")
        thumb = "thumb.jpg"
    else:
        thumb == "no"

    if len(links) == 1:
        count = 1
    else:
        count = int(raw_text)

    try:
        for i in range(count - 1, len(links)):

            V = links[i][1].replace("file/d/","uc?export=download&id=").replace("www.youtube-nocookie.com/embed", "youtu.be").replace("?modestbranding=1", "").replace("/view?usp=sharing","") # .replace("mpd","m3u8")
            url = "https://" + V

            if "visionias" in url:
                async with ClientSession() as session:
                    async with session.get(url, headers={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'Accept-Language': 'en-US,en;q=0.9', 'Cache-Control': 'no-cache', 'Connection': 'keep-alive', 'Pragma': 'no-cache', 'Referer': 'http://www.visionias.in/', 'Sec-Fetch-Dest': 'iframe', 'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-Site': 'cross-site', 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (Linux; Android 12; RMX2121) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36', 'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform': '"Android"',}) as resp:
                        text = await resp.text()
                        url = re.search(r"(https://.*?playlist.m3u8.*?)\"", text).group(1)

            elif "tencdn.classplusapp" in url:
                headers = {'Host': 'api.classplusapp.com', 'x-access-token': 'eyJhbGciOiJIUzM4NCIsInR5cCI6IkpXVCJ9.eyJpZCI6MTI0NDQyMjIwLCJvcmdJZCI6MTMxNSwidHlwZSI6MSwibW9iaWxlIjoiOTE3NDA0MDM0NjQ3IiwibmFtZSI6Ikt1bmFsICIsImVtYWlsIjoia3VuYWxkYWxhbDAzMDlAZ21haWwuY29tIiwiaXNGaXJzdExvZ2luIjp0cnVlLCJkZWZhdWx0TGFuZ3VhZ2UiOiJFTiIsImNvdW50cnlDb2RlIjoiSU4iLCJpc0ludGVybmF0aW9uYWwiOjAsImlzRGl5Ijp0cnVlLCJsb2dpblZpYSI6Ik90cCIsImZpbmdlcnByaW50SWQiOiI4M2M4ZDczOTAwYzc0NjYzYzI2MGJkMzA1ZDYxOTM0MCIsImlhdCI6MTcxODg3Njg5MSwiZXhwIjoxNzE5NDgxNjkxfQ.tV2t5whgnQwrfWLibVIOHV5JN0iDdQwlqDtVDCT_i1zQy4lhF_G3a0zfz7e5S8re', 'user-agent': 'Mobile-Android', 'app-version': '1.4.37.1', 'api-version': '18', 'device-id': '5d0d17ac8b3c9f51', 'device-details': '2848b866799971ca_2848b8667a33216c_SDK-30', 'accept-encoding': 'gzip'}
                params = (('url', f'{url}'),)
                response = requests.get('https://api.classplusapp.com/cams/uploader/video/jw-signed-url', headers=headers, params=params)
                url = response.json()['url']	

            elif 'videos.classplusapp' in url:
                url = requests.get(f'https://api.classplusapp.com/cams/uploader/video/jw-signed-url?url={url}', headers={'x-access-token': 'eyJhbGciOiJIUzM4NCIsInR5cCI6IkpXVCJ9.eyJzb3VyY2UiOjUwLCJzb3VyY2VfYXBwIjoiY2xhc3NwbHVzIiwic2Vzc2lvbl9pZCI6ImNiMmNmNTgzLTgzZDgtNGIzYS04ODNiLTVmMzRmOTUyMzc0NyIsInZpc2l0b3JfaWQiOiI2ZGFhOWVlYi1kMmU4LTQyY2EtOGVjNi0xMzIyM2FjMGE1ODUiLCJjcmVhdGVkX2F0IjoxNzE5MTQxNzc2Mjk5LCJuYW1lIjoiQmFhbG5vaSBBY2FkZW15Iiwib3JnX2NvZGUiOiJibG4iLCJvcmdfaWQiOjEzMTUsInBob25lIjoiOTE3MDE0ODk4NjY4Iiwic291cmNlX3VzZXJfaWQiOiIxMjQ2NzM2MjQiLCJ1c2VyX3R5cGUiOjEsImNvdW50cnlfY29kZSI6IklOIiwiaXNfdXNlcmlkX2V2ZW4iOnRydWUsImlhdCI6MTcxOTE0MTc3NiwiZXhwIjoxNzIwNDM3Nzc2fQ.0b-fTtO_KojThBA7C-l_4N-LQC1Gd4P5sRTLpX8OK9AfcjY9SSDaUznQjN7pcOxi'}).json()['url']
            
            elif '/master.mpd' in url:
                id =  url.split("/")[-2]
                url =  "https://penpencilvod.pc.cdn.bitgravity.com/" + id + "/master.m3u8"

            name1 = links[i][0].replace("\t", "").replace(":", "").replace("/", "").replace("+", "").replace("#", "").replace("|", "").replace("@", "").replace("*", "").replace(".", "").replace("https", "").replace("http", "").strip()
            name = f'{str(count).zfill(3)}) {name1[:60]}'

            if "youtu" in url:
                ytf = f"b[height<={raw_text2}][ext=mp4]/bv[height<={raw_text2}][ext=mp4]+ba[ext=m4a]/b[ext=mp4]"
            else:
                ytf = f"b[height<={raw_text2}]/bv[height<={raw_text2}]+ba/b/bv+ba"

            if "jw-prod" in url:
                cmd = f'yt-dlp -o "{name}.mp4" "{url}"'
            else:
                cmd = f'yt-dlp -f "{ytf}" "{url}" -o "{name}.mp4"'

            try:  
                
                cc = f' **{str(count).zfill(3)}. {name1}** **({res}) Homelander.mkv\n** \n**Batch Name** : **{raw_text0}**\n\n**Downloaded by : {MR}** '
                cc1 = f' **{str(count).zfill(3)}.{name1}** **Homelander.pdf\n** \n**Batch Name** : **{raw_text0}**\n\n**Downloaded by : {MR}** '
                if "drive" in url:
                    try:
                        ka = await helper.download(url, name)
                        copy = await bot.send_document(chat_id=m.chat.id,document=ka, caption=cc1)
                        count+=1
                        os.remove(ka)
                        time.sleep(1)
                    except FloodWait as e:
                        await m.reply_text(str(e))
                        time.sleep(e.x)
                        continue
                
                elif ".pdf" in url:
                    try:
                        cmd = f'yt-dlp -o "{name}.pdf" "{url}"'
                        download_cmd = f"{cmd} -R 25 --fragment-retries 25"
                        os.system(download_cmd)
                        copy = await bot.send_document(chat_id=m.chat.id, document=f'{name}.pdf', caption=cc1)
                        count += 1
                        os.remove(f'{name}.pdf')
                    except FloodWait as e:
                        await m.reply_text(str(e))
                        time.sleep(e.x)
                        continue
                else:
                    Show = f"**⌛🅓𝒐𝒘𝒏𝒍𝒐𝒂𝒅𝒊𝒏𝒈⌛ »**\n\n**⚓️Name »** `{name}`\n\n🖼**Quality** » `{raw_text2}`\n\n**Bot Developed by Bʟᴀᴄᴋ⚡Ꭺᴅᴀᴍ️🤍**"
                    prog = await m.reply_text(Show)
                    res_file = await helper.download_video(url, cmd, name)
                    filename = res_file
                    await prog.delete(True)
                    await helper.send_vid(bot, m, cc, filename, thumb, name, prog)
                    count += 1
                    time.sleep(1)

            except Exception as e:
                await m.reply_text(
                    f"**Downloading Failed **\n\n**Error** » {str(e)}\n\n**Name** » {name}"
                )
                continue

    except Exception as e:
        await m.reply_text(e)
    await m.reply_text("**✰🅓ơɳɛ✰**")
    
bot.run()
