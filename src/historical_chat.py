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

# Replace with your own API credentials
api_id = api_keys["TELEGRAM_API"]["API_ID"]
api_hash = api_keys["TELEGRAM_API"]["API_HASH"]
session_name = "development_session"

# Replace with your own phone number and session file name
phone_number = '+917305127415'

# Initialize the Telegram client
client = TelegramClient(session_name, api_id, api_hash)

async def main():
    total_messges = 2000
    success = 0
    failed = 0
    uploaded_to_database = 0
    parsed = 0
    start = time.time()
    await client.start(phone_number)

    # Replace 'chat' with the name or username of the chat you want to scrape
    chat = await client.get_input_entity(-1001273446931)

    # Retrieve the last 500 messages from the chat
    messages = await client.get_messages(chat, limit=2000)
    messages = client.iter_messages(chat, limit=2000)
    print("NoOfMsgScrapedParsed\tNoOfMsgUplodedToDB\tSuccess\tFailures\tTime\tTotal")
    
    async for message in messages:
        # Process each message as needed
        try:
            pe = Prices()
            price = pe.get_prices(message.text)
            # print(message.text)
            # print("price", price)
            lower_price = price[0][0]
            higher_price = price[0][1]
            currency = price[1]
            date = message.date
            post_url = extract_freelancer_links(message.text)[0]
            uname = get_links(message.text) 
            telegram_link = telegram_validater(uname)
            github_link = github_validater(uname)
            freelancer_link = freelancer_validater(uname)
            twitter_link = twitter_validater(uname)
            normalized_upper = pe.convert_currency(higher_price, currency, "USD")
            normalized_lower = pe.convert_currency(lower_price, currency, "USD")
            data = {
                'Message' : message.text,
                'Upper_price' : higher_price,
                "Nomalized_upper" : normalized_upper,
                "Normalized_lower" : normalized_lower,
                "Lower_price" : lower_price,
                "Currency" : currency,
                "Username" : uname,
                "Date" :  date.strftime("%Y-%m-%d %H:%M:%S"),
                "Github" : github_link,
                "Telegram" : telegram_link,
                "Freelancer" : freelancer_link,
                "Twitter" : twitter_link,
                "Post_url" : post_url               
            }
            upload_data(data=data)
            uploaded_to_database += 1
            success += 1
        except Exception as e:
            # print("[-] Error : ",e)
            failed += 1
        parsed += 1

        print(f"\t{parsed}\t\t\t{uploaded_to_database}\t\t{success}\t{failed}\t{total_messges}",end="\r")
    print(f"\n[+] Completed the MonstarGrasp in {start - time.time()}")
    print(f"{success} success")
    print(f"{failed} failed")
            

    await client.disconnect()

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
