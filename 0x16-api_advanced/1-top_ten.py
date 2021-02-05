#!/usr/bin/python3
""" Function that queries Reddit API """
import requests


def top_ten(subreddit):
    """ this function prints the titles od the first 10 host posts
        listed for a given subreddit
    """
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    headers = {'User_agent': 'someramdonstring'}
    subreddit_req = requests.get(url, headers=headers).json()
    if 'error' in subreddit_req:
        print("None")
        return 0
    data_dict = subreddit_req.get('data')
    children_dict = data_dict.get('children')
    for titles in children_dict:
        print(titles.get('data').get('title'))
