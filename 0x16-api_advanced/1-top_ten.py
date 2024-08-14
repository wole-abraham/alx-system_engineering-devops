#!/usr/bin/python3
"""
    top ten post for a givnen sub reddit

"""

import requests
from sys import argv


def top_ten(subreddit):
    """
    Queries the Reddit API to print the titles of the first 10 hot posts
    listed for a given subreddit. If the subreddit is invalid, prints None.

    :param subreddit: The name of the subreddit.
    """

    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
    headers = {
        "User-Agent": "python:subreddit.hot.posts:v1.0 (by /u/yourusername)"
        }

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            posts = response.json().get('data', {}).get('children', [])
            if not posts:
                print(None)
                return
            for post in posts:
                print(post.get('data', {}).get('title'))
        else:
            print(None)
    except requests.RequestException:
        print(None)


if __name__ == "__main__":

    top_ten(argv[1])
