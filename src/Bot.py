#!/usr/bin/python3
# Bot.py
# Ashish D'Souza (computer_geek64)
# June 5th, 2019

import os
import git
import praw
from time import sleep


os.chdir(os.path.dirname(__file__))

git.Repo(__file__[:__file__.index("rocket-league-reddit-bot") + 24]).remotes.origin.pull()

reddit = praw.Reddit("bot")
unauthenticated_reddit = praw.Reddit("unauthenticated_bot")

while True:
    with open("settings.txt", "r") as file:
        settings = file.readlines()

    delay = int(settings[0][settings[0].index(":") + 1:].strip())
    paragraph = "".join(settings[1:])

    print(unauthenticated_reddit.redditor(str(reddit.user.me())).submissions.new().next().author)

    exit(0)

    reddit.submission("bkz2do").reply(paragraph)
    sleep(delay * 60)
