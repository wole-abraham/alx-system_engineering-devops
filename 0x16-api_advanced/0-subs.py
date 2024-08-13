#!/usr/bin/python3
"""
    python script returns the number of subscribers
    for a given subreddit
"""

import requests
from sys import argv


def number_of_subscribers(subreddit):

    """
        base_url:
        subs
    """

    base_url = requests.get(f'https://reddit.com/r/{subreddit}/about.json')
    try:
        subs = base_url.json()['data']['subscribers']
    except KeyError:
        subs = 0
    return subs


if __name__ == "__main__":

    print(number_of_subscribers(argv[1]))
