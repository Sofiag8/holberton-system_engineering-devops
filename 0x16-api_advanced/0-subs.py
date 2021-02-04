#!/usr/bin/python3
""" Reddit API
Checking on JSON link for an overview of some response types
    - subreddit neeeded = passed as argument
"""
import requests


def number_of_subscribers(subreddit):
    """ Function that queries Reddit API

        Return:
             the number of subscribers (not active users, total subscribers)
             for a given subreddit. If an invalid subreddit is given,
             the function should return 0.
    """
    subreddit_url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'user-agent': 'reddit_url'}
    subreddit_req = requests.get(subreddit_url, headers=headers)
    if subreddit_req.status_code == 404:
        return 0
    data_dict = subreddit_req.json().get('data')
    subscribers = data_dict.get('subscribers')
    return subscribers
