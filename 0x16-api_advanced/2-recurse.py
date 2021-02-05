#!/usr/bin/python3
""" Function that queries Reddit API """
import requests


def recurse(subreddit, hot_list=[], count=''):
    """ this function returns a list containing
    the titles of all hot articles for a given subreddit
    """
    url = 'https://www.reddit.com/r/{}/hot.json?afer={}'.format(subreddit,
                                                                count)
    headers = {'User-Agent': 'app,os,vendorandversion'}
    subreddit_req = requests.get(url, headers=headers).json()
    if 'error' not in subreddit_req:
        for titles in subreddit_req['data']['children']:
            hot_list.append(titles['data']['title'])
        count = subreddit_req['data']['after']
        if count is not None:  # nothing more in the listing
            recurse(subreddit, hot_list, count)
        return hot_list
    else:
        return None
