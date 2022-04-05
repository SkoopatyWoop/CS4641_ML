import datetime
from psaw import PushshiftAPI
from queries.Queries import Queries

TWELVE_DAYS_INTERVAL = int(datetime.datetime.now().timestamp()) - int((datetime.datetime.now() - datetime.timedelta(days=12)).timestamp())


def main():
    # prw = praw.Reddit("bot", user_agent="bot user agent")
    reddit = PushshiftAPI()

    ethical_submissions = Queries(reddit)\
        .query(subreddit="LifeProTips",
               epoch_delta=1000,
               epoch_timeinWterval=TWELVE_DAYS_INTERVAL,
               start_epoch=int(datetime.datetime(2022, 1, 1).timestamp()),
               limit=1000)

    unethical_submissions = Queries(reddit) \
        .query(subreddit="UnethicalLifeProTips",
               epoch_delta=1000,
               epoch_timeinterval=TWELVE_DAYS_INTERVAL,
               start_epoch=int(datetime.datetime(2022, 1, 1).timestamp()),
               limit=1000)


if __name__ == "__main__":
    main()
