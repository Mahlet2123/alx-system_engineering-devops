#!/usr/bin/python3
"""
Write a  recursive function that queries the Reddit API
and prints the titles of the first 10 hot posts
listed for a given subreddit.

If not a valid subreddit, print None.
"""


import requests


def recurse(subreddit, hot_list=[], after=None):
    """Prints top 10 posts"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Linux:0-subs:v1.0"}
    # Custom User-Agent header

    params = {'limit': 100}
    if isinstance(after, str):
        if after != "STOP":
            params['after'] = after
        else:
            return hot_list
    response = requests.get(url, headers=headers, params=params)
    posts = response.json().get('data', {}).get('children', {})
    if response.status_code != 200 or not posts:
        return None
    data = response.json().get('data', {})
    after = data.get('after', 'STOP')
    if not after:
        after = "STOP"
    hot_list = hot_list + [post.get('data', {}).get('title')
                           for post in data.get('children', [])]
    return recurse(subreddit, hot_list, after)
