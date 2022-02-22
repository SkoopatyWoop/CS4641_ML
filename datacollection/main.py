import praw


def main():
    reddit = praw.Reddit("bot", user_agent="bot user agent")
    print(list(reddit.subreddit("memes").hot(limit=10)))


if __name__ == "__main__":
    main()
