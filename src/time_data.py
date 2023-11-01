import asyncio
from telethon.sync import TelegramClient
from datetime import datetime, timedelta
import pytz
from Configs.api_keys import api_keys,channel_config


async def retrieve_messages():
    api_id = api_keys["TELEGRAM_API"]["API_ID"]
    api_hash = api_keys["TELEGRAM_API"]["API_HASH"]
    session_name = "development_session"

    async with TelegramClient(session_name, api_id, api_hash) as client:
        await client.start()

        chat_username = -1001273446931
        date_from = datetime.now() - timedelta(days=30)
        
        # Make sure both datetime objects are in the same time zone
        date_from = date_from.replace(tzinfo=pytz.utc)  # Set the time zone to UTC

        entity = await client.get_entity(chat_username)
        messages = client.iter_messages(entity, limit=100)
        lst = []
        mst = []
        async for message in messages:
            # print(message.date)
            lst.append(message)
            if message.date > date_from:
                print(message.date)
                
                # print(f"From:  - Message: {message.text}")
                mst.append(message)
        print(len(lst), len(mst))

if __name__ == "__main__":
    asyncio.run(retrieve_messages())
