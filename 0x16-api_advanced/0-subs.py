#!/usr/bin/python3
"""
Write a function that queries the Reddit API and
returns the number of subscribers (not active users,
total subscribers) for a given subreddit.

If an invalid subreddit is given, the function should return 0.
"""


import requests


def number_of_subscribers(subreddit):
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Linux:0-subs:v1.0"}
    # Custom User-Agent header

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data["data"]["subscribers"]
    else:
        return 0
