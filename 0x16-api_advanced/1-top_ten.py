#!/usr/bin/python3
"""
Write a function that queries the Reddit API
and prints the titles of the first 10 hot posts
listed for a given subreddit.

If not a valid subreddit, print None.
"""


import requests
import json


def top_ten(subreddit):
    """Prints top 10 posts"""
    url = "https://www.reddit.com/r/{}/top.json".format(subreddit)
    headers = {"User-Agent": "Linux:0-subs:v1.0"}
    # Custom User-Agent header

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        #print(json.dumps(data, indent=4))
        top_list = data["data"]["children"]
        for i in top_list[0:10]:
            print(i["data"]["title"])
    else:
        print("None")
