#!/usr/bin/python3
"""
Python function that queries the Reddit API and returns the
number of subcribers
"""
import requests

def number_of_subscribers(subreddit):
        url = f"https://www.reddit.com/r/{subreddit}/about.json"
        headers = {'User-Agent': 'Custom User Agent'}
        # Set a custom User-Agent to avoid Too Many Requests error
        response = requests.get(url, headers=headers)
                    
        if response.status_code == 200:
            data = response.json()
            subscribers = data['data']['subscribers']
            return subscribers
         else:
            return 0

