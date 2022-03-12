import datetime
import praw
import time
import json
from psaw import PushshiftAPI
from pymongo import MongoClient
from dotenv import dotenv_values
from queries.Queries import Queries

# TWELVE_DAYS_INTERVAL = int(datetime.datetime.now().timestamp()) - int((datetime.datetime.now() - datetime.timedelta(days=12)).timestamp())
# ONE_DAY_INTERVAL = int(datetime.datetime.now().timestamp()) - int((datetime.datetime.now() - datetime.timedelta(days=1)).timestamp())
ONE_HOUR_INTERVAL = int(datetime.datetime.now().timestamp()) - int((datetime.datetime.now() - datetime.timedelta(hours=1)).timestamp())


def main():
    config = dotenv_values('.env')
    reddit = PushshiftAPI()
    praw_reddit = praw.Reddit("bot", user_agent="bot user agent")
    praw_reddit.config.store_json_result = True
    client = MongoClient(f"mongodb+srv://{config['MONGODB_USERNAME']}:{config['MONGODB_PASSWORD']}@prd.bfu3q.mongodb.net/test")
    db = client.prd
    collection = db.data

    start = time.time()

    ethical_submissions = Queries(reddit, praw=praw_reddit)\
        .query(subreddit="LifeProTips",
               epoch_delta=None,
               epoch_timeinterval=ONE_HOUR_INTERVAL,
               start_epoch=int(datetime.datetime(2022, 1, 1).timestamp()),
               limit=500000)

    unethical_submissions = Queries(reddit, praw=praw_reddit) \
        .query(subreddit="UnethicalLifeProTips",
               epoch_delta=None,
               epoch_timeinterval=ONE_HOUR_INTERVAL,
               start_epoch=int(datetime.datetime(2022, 1, 1).timestamp()),
               limit=500000)

    print(f"took {time.time() - start} seconds")

    collection.insert(json.loads(ethical_submissions.df.T.to_json()).values())
    collection.insert(json.loads(unethical_submissions.df.T.to_json()).values())


if __name__ == "__main__":
    main()
