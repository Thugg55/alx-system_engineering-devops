#!/usr/bin/python3
"""
recursive function that queries the Reddit API and returns a list
contatining the tiltles of all hot articles for a given subreddit
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """function must be recursive"""
    if len(hot_list) >= 1000:
        return hot_list

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    if after:
        url += f"&after={after}"

    headers = {'User-Agent': 'Custom User Agent'}
    # Set a custom User-Agent to avoid Too Many Requests error
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        after = data['data']['after']

        for post in posts:
            hot_list.append(post['data']['title'])

        if after:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    else:
        return None
