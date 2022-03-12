import pandas
from psaw import PushshiftAPI
from praw import Reddit
from typing import Optional


class Queries:

    def __init__(self, reddit: PushshiftAPI, praw: Reddit):
        """
        :param reddit: api wrapper
        """
        self.reddit = reddit
        self.praw = praw
        self.df = pandas.DataFrame()

    def query(self, subreddit: str, epoch_delta: Optional[int], epoch_timeinterval: int, start_epoch: int, limit: int):
        """
        :param subreddit: target subreddit to query
        :param epoch_delta: number of posts to take at a time i.e. limit
        :param epoch_timeinterval: timeskip interval to iterate with
        :param start_epoch: starting time
        :param limit: total limit on submissions
        """
        idx = 1
        while self.df.size < limit:
            submissions = [submission.d_ for submission in self.reddit.search_submissions(
                after=start_epoch - epoch_timeinterval * idx,
                before=start_epoch - epoch_timeinterval * (idx - 1),
                subreddit=subreddit,
                limit=100
            )]
            submissions = [submission for submission in self.praw.info([f"t3_{info['id']}" for info in submissions]) if submission.score > 4 ]
            valid_submissions = [{
                "num_awards": submission.total_awards_received,
                "num_reports": submission.num_reports if submission.num_reports is not None else 0,
                "score": submission.score,
                "ups": submission.ups,
                "upvote_ratio": submission.upvote_ratio,
                "text": f"{submission.title} {submission.selftext if submission.selftext != '[removed]' else ''}",
                "ethical_tag": subreddit == "LifeProTips"
            } for submission in submissions if submission.ups > 4 and submission.removed_by is None]
            search_df = pandas.DataFrame(valid_submissions)
            print(f"found {len(search_df)} matching submissions for -{idx} hours...")
            self.df = pandas.concat([self.df, search_df])
            idx += 1

        return self
