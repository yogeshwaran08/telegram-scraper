from slack_sdk import WebClient
from src.configs.api_keys import api_keys,channel_config
slack_token = api_keys["SLACK_API"]
client = WebClient(token=slack_token)

channel_id =  channel_config["SLACK_CHANNEL"]["TRIGGER"]

def trigger_in_slack(channel_id, message, sender):
    message = f"Message received from {sender} with content {message}"
    response = client.chat_postMessage(channel=channel_config["SLACK_CHANNEL"][channel_id],text=message)
    if response['ok']:
        print(f"[+] Message sent successfully: {response}")
    else:
        print(f"[-] Failed to send message : {response['error']}")