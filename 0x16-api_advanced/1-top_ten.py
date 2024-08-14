#!/usr/bin/python3
"""
    top ten post for a givnen sub reddit

"""

import requests
from sys import argv


def top_ten(subreddit):
    """
    Queries the Reddit API to print the titles of the first 10 hot posts

    """

    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {
        "User-Agent": "python:subreddit.hot.posts:v1.0 (by /u/yourusername)"
        }
    params = {'limit': 9}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False,
                                params=params)
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
