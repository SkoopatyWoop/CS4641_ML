import datetime
import praw
import time
from azure.cosmos.exceptions import CosmosResourceExistsError
import azure.cosmos.cosmos_client as cosmos_client
from azure.cosmos.partition_key import PartitionKey
from psaw import PushshiftAPI
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
    client = cosmos_client.CosmosClient(
        config['AZURE_SQL_HOST'],
        {
            'masterKey': config['AZURE_SQL_MASTER_KEY']
        },
        user_agent="CosmosDBPythonQuickstart",
        user_agent_overwrite=True
    )
    db = client.create_database_if_not_exists(id=config['AZURE_SQL_DATABASE_ID'])
    print('Database with id \'{0}\' initialized'.format(config['AZURE_SQL_DATABASE_ID']))
    container = db.create_container_if_not_exists(
        id=config['AZURE_SQL_CONTAINER_ID'],
        partition_key=PartitionKey(path='/ethical_tag'),
        offer_throughput=1000
    )
    print('Container with id \'{0}\' initialized'.format(config['AZURE_SQL_CONTAINER_ID']))

    start = time.time()

    ethical_submissions = Queries(reddit, praw=praw_reddit)\
        .query(subreddit="LifeProTips",
               epoch_delta=None,
               epoch_timeinterval=ONE_HOUR_INTERVAL,
               start_epoch=int(datetime.datetime(2022, 1, 1).timestamp()),
               limit=10)

    unethical_submissions = Queries(reddit, praw=praw_reddit) \
        .query(subreddit="UnethicalLifeProTips",
               epoch_delta=None,
               epoch_timeinterval=ONE_HOUR_INTERVAL,
               start_epoch=int(datetime.datetime(2022, 1, 1).timestamp()),
               limit=10)

    print(f"took {time.time() - start} seconds")

    for document in ethical_submissions.submissions:
        try:
            container.create_item(document)
        except CosmosResourceExistsError:
            pass

    for document in unethical_submissions.submissions:
        try:
            container.create_item(document)
        except CosmosResourceExistsError:
            pass


if __name__ == "__main__":
    main()
