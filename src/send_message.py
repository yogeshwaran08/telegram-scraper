from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerChat
from configs.api_keys import api_keys,channel_config
from utils.nlp.nlp import get_links,extract_freelancer_links
from utils.db.mongo import upload_data
from utils.media.telegram import telegram_validater
from utils.media.github import github_validater
from utils.media.twitter import twitter_validater
from utils.media.freelancer import freelancer_validater
from utils.nlp.Prices import Prices
import time
from telethon.tl.custom import MessageButton
from telethon.tl.functions.contacts import AddContactRequest

# Replace with your own API credentials
api_id = api_keys["TELEGRAM_API"]["API_ID"]
api_hash = api_keys["TELEGRAM_API"]["API_HASH"]
session_name = "development_session"

# Replace with your own phone number and session file name
phone_number = '+917305127415'

# Initialize the Telegram client
client = TelegramClient(session_name, api_id, api_hash)

async def main():
    failed = 0
    await client.start(phone_number)

    # Replace 'chat' with the name or username of the chat you want to scrape
    chat = await client.get_input_entity(-1001113535556)

    # Retrieve the last 500 messages from the chat
    messages = await client.get_messages(chat, limit=2000)
    messages = client.iter_messages(chat, limit=1)
    
    async for message in messages:
        # Process each message as needed
        try:
            # print(message.reply_markup)
            if message.reply_markup and message.reply_markup.rows:
                for row in message.reply_markup.rows:
                    # print(row)
                    for button in row.buttons:
                        print(button.url)
                        if button.url:
                            print("Button URL:", button.url)
                            user_entity = await client.get_entity(button.url)
                            result = await client(AddContactRequest(user_entity))
        except Exception as e:
            print(e)
            failed += 1
            

    await client.disconnect()

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
