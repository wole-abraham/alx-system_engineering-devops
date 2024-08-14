#!/usr/bin/python3
"""
    python script returns the number of subscribers
    for a given subreddit
"""

import requests
from sys import argv


def number_of_subscribers(subreddit):

    """
    Queries the Reddit API to return the number of
    subscribers for a given subreddit.
    If an invalid subreddit is given, returns 0.

    :param subreddit: The name of the subreddit.
    :return: The number of subscribers or 0 if the subreddit is invalid.
    """
    base_url = requests.get(f'https://www.reddit.com/r/{subreddit}/about.json',
                            allow_redirects=False)
    if base_url.status_code == 200:
        subs = base_url.json()['data']['subscribers']
        return subs
    else:
        return 0


if __name__ == "__main__":

    print(number_of_subscribers(argv[1]))
