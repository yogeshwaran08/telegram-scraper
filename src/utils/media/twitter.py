import tweepy
from ...configs import api_keys

auth = tweepy.OAuthHandler(api_keys.twitter_bot["consumer_key"], api_keys.twitter_bot["consumer_secret"])
auth.set_access_token(api_keys.twitter_bot["access_token"], api_keys.twitter_bot["access_token_secret"])

api = tweepy.API(auth)


        
def twitter_validater(username):
    try:
        _ = api.get_user(screen_name=username)
        return f"https://twitter.com/{username}"
    except:
        return None
