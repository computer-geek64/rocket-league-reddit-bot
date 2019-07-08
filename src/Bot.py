#!/usr/bin/python3
# Bot.py
# Ashish D'Souza (computer_geek64)
# July 7th, 2019

import os
import sys
import git
import praw
from time import sleep
from datetime import datetime


subreddit = "RocketLeagueExchange"
submission = "bkz2do"

#os.chdir(os.path.dirname(sys.argv[0]))

#absolute_filepath = os.path.abspath(__file__)
#git.Repo(absolute_filepath[:absolute_filepath.index("rocket-league-reddit-bot") + 24]).remotes.origin.fetch()
#if sum(1 for c in git.Repo(absolute_filepath[:absolute_filepath.index("rocket-league-reddit-bot") + 24]).iter_commits("master..origin/master")):
#    git.Repo(absolute_filepath[:absolute_filepath.index("rocket-league-reddit-bot") + 24]).remotes.origin.pull()
#    sys.exit(0)

reddit = praw.Reddit("bot")

while True:
    with open("settings.txt", "r") as file:
        settings = file.readlines()

    delay = int(settings[0][settings[0].index(":") + 1:].strip())
    paragraph = "".join(settings[1:])

    posts = reddit.redditor(str(reddit.user.me())).new()
    for post in posts:
        if post.subreddit == subreddit:
            break
    if (datetime.now().timestamp() - post.created_utc) / 60 < 15:
        sleep(60)
        continue

    #reddit.submission("bkz2do").reply(paragraph)
    #reddit.submission("bxap66").reply(paragraph)
    reddit.submission(submission).reply(paragraph)
    sleep(delay * 60)
