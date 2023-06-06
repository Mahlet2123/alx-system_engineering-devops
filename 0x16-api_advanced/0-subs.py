#!/usr/bin/python3
"""
Write a function that queries the Reddit API and
returns the number of subscribers (not active users,
total subscribers) for a given subreddit.

If an invalid subreddit is given, the function should return 0.
"""


import requests


def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "My API Client"}
    # Custom User-Agent header

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data["data"]["subscribers"]
    else:
        return 0
