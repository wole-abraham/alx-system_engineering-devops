#!/usr/bin/python3

"""
    python script queries the reddit api

"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'after': after} if after else {}

    try:
        response = requests.get(url, headers=headers,
                                params=params, allow_redirects=False)
        # Check if the response is successful
        if response.status_code != 200:
            return None

        data = response.json().get('data')

        if not data:
            return None

        # Extend the list with titles of hot articles
        hot_list.extend([post['data']['title'] for post in data['children']])

        # Check if there's a next page (pagination)
        after = data.get('after')
        if after:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    except requests.exceptions.RequestException:
        return None
