#!/usr/bin/python3
"""
recursive function that queries the Reddit API, parses the 
title of all hot articles, and prints a sorted count of given keywords
"""
import requests
from collections import Counter


def count_words(subreddit, word_list, after=None, word_count=None):
    """function count words"""
    if word_count is None:
        word_count = Counter()

    if len(word_count) == 0:
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
                title = post['data']['title'].lower()
                for word in word_list:
                    if ' ' + word.lower() + ' ' in title or title.startswith(word.lower() + ' ') or title.endswith(' ' + word.lower()):
                        word_count[word.lower()] += 1

            if after:
                return count_words(subreddit, word_list, after, word_count)
            else:
                return word_count
        else:
            return None
    else:
        sorted_counts = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_counts:
            print(f"{word}: {count}")

# Example usage:
count_words("python", ["python", "java", "javascript"])

