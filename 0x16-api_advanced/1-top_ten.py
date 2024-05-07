#!/usr/bin/python3
"""
Python function queires the Reddit API and prints the
title of the first 10 hot posts listed for a given subreddit
"""

import requests


def top_ten(subreddit):
    """
    Args:
    Subreddit: name of subreddit
    Return: Print None if not a valid reddit
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'Custom User Agent'}
    # Set a custom User-Agent to avoid Too Many Requests error
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        for post in posts:
            print(post['data']['title'])
    else:
        print("None")
