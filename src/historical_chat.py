from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerChat
from Configs.api_keys import api_keys,channel_config
from utils.nlp.nlp import get_prices,get_links
from utils.db.mongo import upload_data
from utils.media.telegram import telegram_validater
from utils.media.github import github_validater
from utils.media.twitter import twitter_validater
from utils.media.freelancer import freelancer_validater


# Replace with your own API credentials
api_id = api_keys["TELEGRAM_API"]["API_ID"]
api_hash = api_keys["TELEGRAM_API"]["API_HASH"]
session_name = "development_session"

# Replace with your own phone number and session file name
phone_number = 'YOUR_PHONE_NUMBER'

# Initialize the Telegram client
client = TelegramClient(session_name, api_id, api_hash)

async def main():
    await client.start(phone_number)

    # Replace 'chat' with the name or username of the chat you want to scrape
    chat = await client.get_input_entity(-1001273446931)

    # Retrieve the last 500 messages from the chat
    messages = await client.get_messages(chat, limit=2000)
    messages = client.iter_messages(chat, limit=2000)
    
    async for message in messages:
        # Process each message as needed
        try:
            price = get_prices(message.text)
            # print(message.text)
            print("price", price)
            lower_price = price[1]
            higher_price = price[0]
            date = message.date
            uname = get_links(message.text)
            telegram_link = telegram_validater(uname)
            github_link = github_validater(uname)
            freelancer_link = freelancer_validater(uname)
            twitter_link = twitter_validater(uname)
            data = {
                'message' : message.text,
                "sender_id" : -1001273446931,
                'upper_price_limit' : lower_price,
                "lower_price_limit" : higher_price,
                "username" : get_links(message.text),
                "date" :  date.strftime("%Y-%m-%d %H:%M:%S"),
                "Github" : github_link,
                "Telegram" : telegram_link,
                "Freelancer" : freelancer_link,
                "Twitter" : twitter_link,
            }
            upload_data(data=data)
        except:
            print("non sandard")
            

    await client.disconnect()

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
