from telethon.sync import TelegramClient, events
from utils.targets import test_send_message, test_message
from utils.db.mongo import upload_data
from configs.api_keys import api_keys,channel_config
from utils.trigger.slack import trigger_in_slack
from utils.nlp.nlp import get_prices,get_links

#telegram conf
api_id = api_keys["TELEGRAM_API"]["API_ID"]
api_hash = api_keys["TELEGRAM_API"]["API_HASH"]
session_name = "development_session"
target_id = channel_config["TELEGRAM_CHAT"]["target_id"]

#driver code
with TelegramClient(session_name, api_id, api_hash) as client:
   client.send_message(test_send_message, test_message)
   
   @client.on(events.NewMessage())
   async def handler(event):
      if (event.sender_id in target_id):
         # await event.reply(test_message)
         # print(event)
         # print(f"[+] Received {event.message.text} from {event.sender_id}")
         price = get_prices(event.message.text)[0]
         lower_price = price[0].strip()
         higher_price = price[1].strip()
         data = {
            'message' : event.message.text,
            "sender_id" : event.sender_id,
            'upper_price_limit' : lower_price,
            "lower_price_limit" : higher_price,
            "username" : get_links(event.message.text),
         }
         upload_data(data=data)
         # trigger_in_slack("TRIGGER", message=event.message.text, sender=event.sender_id)
         
   client.run_until_disconnected()
