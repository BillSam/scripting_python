import tweepy
import time

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
user = api.me()


# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)


def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(1000)


search = 'python'
numbersofTweets = 2

for tweet in tweepy.Cursor(api.search, search).items(numbersofTweets):
    try:
        tweet.favoite()
        print('I liked that tweet')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break

# generous bot
# for follower in limit_handler(tweepy.Cursor(api.followers).items()):
#     if follower.name == 'sample':
#         follower.follow()
#         break
