#!/usr/bin/python3

"""Importing request library to get data from Url"""
import requests


def number_of_subscribers(subreddit):
    """number_of_subscribers function
    that get date from reddit
    and returns number of subscribers"""

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        else:
            return 0
    except requests.RequestException:
        return 0


# Example usage:
print(number_of_subscribers("python"))