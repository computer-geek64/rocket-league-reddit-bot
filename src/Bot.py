#!/usr/bin/python3
# Bot.py
# Ashish D'Souza (computer_geek64)
# June 5th, 2019

import os
import git
import praw
from time import sleep
from datetime import datetime


os.chdir(os.path.dirname(__file__))

git.Repo(__file__[:__file__.index("rocket-league-reddit-bot") + 24]).remotes.origin.pull()

reddit = praw.Reddit("bot")

while True:
    with open("settings.txt", "r") as file:
        settings = file.readlines()

    delay = int(settings[0][settings[0].index(":") + 1:].strip())
    paragraph = "".join(settings[1:])

    posts = reddit.redditor(str(reddit.user.me())).new()
    for post in posts:
        if post.subreddit != "BotTesting69":
            continue
        break
    if (datetime.now().timestamp() - post.created_utc) / 60 < 10:
        sleep(60)
        continue

    #reddit.submission("bkz2do").reply(paragraph)
    reddit.submission("bxap66").reply(paragraph)
    sleep(delay * 60)
