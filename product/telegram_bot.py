import requests
from telegram import Bot
import asyncio

def get_chat_id(bot_token):
    url = f'https://api.telegram.org/bot{bot_token}/getUpdates'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if data['result']:
            chat_id = data['result'][0]['message']['chat']['id']
            return chat_id
        else:
            print("No updates found. Make sure you've started a conversation with your bot.")
    else:
        print(f"Failed to fetch updates. Status code: {response.status_code}")

bot_token = '6991822427:AAGZYUkfrccur_aPfSujivqwV1NL6FtSU1o'
chat_id = get_chat_id(bot_token)

if chat_id:
    print(f"Your chat ID is: {chat_id}")



async def send_message(bot_token, chat_id, text):
    bot = Bot(token=bot_token)
    await bot.send_message(chat_id=chat_id, text=text)

async def main():
    await send_message('6991822427:AAGZYUkfrccur_aPfSujivqwV1NL6FtSU1o', '765001726', 'Hello, Telegram!')

if name == "main":
    # Run the event loop
    asyncio.run(main())


#pip install requests
# pip install python-telegram-bot