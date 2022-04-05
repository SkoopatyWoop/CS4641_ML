import datetime
import string
import sys
import re

import praw
import time
import nltk
from azure.cosmos.exceptions import CosmosResourceExistsError
import azure.cosmos.cosmos_client as cosmos_client
from azure.cosmos.partition_key import PartitionKey
from psaw import PushshiftAPI
from dotenv import dotenv_values
from queries.Queries import Queries

# TWELVE_DAYS_INTERVAL = int(datetime.datetime.now().timestamp()) - int((datetime.datetime.now() - datetime.timedelta(days=12)).timestamp())
# ONE_DAY_INTERVAL = int(datetime.datetime.now().timestamp()) - int((datetime.datetime.now() - datetime.timedelta(days=1)).timestamp())
ONE_HOUR_INTERVAL = int(datetime.datetime.now().timestamp()) - int(
    (datetime.datetime.now() - datetime.timedelta(hours=1)).timestamp())


def main(varargs):
    config = dotenv_values('.env')
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
    if "clean" in varargs:
        nltk.download('stopwords')
        items = container.read_all_items()
        for i, item in enumerate(items):
            if "deleted by user" in item["text"]:
                container.delete_item(item, partition_key=item["ethical_tag"])
                continue
            item["text"] = item["text"].lower()
            item["text"] = item["text"].replace("lpt request:", "")
            item["text"] = item["text"].replace("lpt request", "")
            item["text"] = item["text"].replace("ulpt request:", "")
            item["text"] = item["text"].replace("ulpt request", "")
            item["text"] = item["text"].replace("lpt:", "")
            item["text"] = item["text"].replace("ulpt:", "")
            item["text"] = item["text"].replace("lpt", "")
            item["text"] = item["text"].replace("ulpt", "")
            item["text"] = item["text"].replace("edit", "")
            item["text"] = item["text"].replace("/", " ")
            item["text"] = item["text"].replace("“", "\"")
            item["text"] = item["text"].replace("”", "\"")
            item["text"] = item["text"].replace("’", "'")
            item["text"] = ' '.join(word for word in item["text"].split() if word not in nltk.corpus.stopwords.words('english'))
            item["text"] = item["text"].replace("'", "")
            item["text"] = item["text"].replace("\"", "")
            item["text"] = item["text"].translate(str.maketrans('', '', string.punctuation))
            item["text"] = item["text"].strip()
            item["text"] = ''.join(char for char in item["text"] if not char.isdigit())
            item["text"] = re.sub(r'\s+', ' ', item["text"])
            item["text"] = ' '.join(word for word in item["text"].split() if len(word) > 1)
            if len(item["text"].split()) <= 6 or item["text"].split()[-1] == "deleted":
                container.delete_item(item, partition_key=item["ethical_tag"])
                continue
            print(item["text"])
            container.upsert_item(item)
    else:
        reddit = PushshiftAPI()
        praw_reddit = praw.Reddit("bot", user_agent="bot user agent")
        praw_reddit.config.store_json_result = True

        start = time.time()

        ethical_submissions = Queries(reddit, praw=praw_reddit) \
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
    main(sys.argv[1:])
