import pandas
from psaw import PushshiftAPI


class Queries:

    def __init__(self, reddit: PushshiftAPI):
        """
        :param reddit: api wrapper
        """
        self.reddit = reddit
        self.df = pandas.DataFrame()

    def query(self, subreddit: str, epoch_delta: int, epoch_timeinterval: int, start_epoch: int, limit: int):
        """
        :param subreddit: target subreddit to query
        :param epoch_delta: number of posts to take at a time i.e. limit
        :param epoch_timeinterval: timeskip interval to iterate with
        :param start_epoch: starting time
        :param limit: total limit on submissions
        """
        idx = 0
        while self.df.size < limit:
            self.df = pandas.concat([self.df, pandas.DataFrame([submission.d_ for submission in self.reddit.search_submissions(
                after=start_epoch - epoch_timeinterval * idx,
                subreddit=subreddit,
                limit=epoch_delta
            )])])

        return self
