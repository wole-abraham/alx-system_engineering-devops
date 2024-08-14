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
    headers = {'User-Agent': "python:subreddit.subscriber.counter:v1.0\
(by /u/Responsible-Bonus-58)"}
    base_url = requests.get(f'https://www.reddit.com/r/{subreddit}/about.json',
                            allow_redirects=False, headers=headers)
    if base_url.status_code == 200:
        subs = base_url.json().get('data').get('subscribers')
        return subs
    else:
        return 0
