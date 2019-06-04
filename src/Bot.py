#!/usr/bin/python3
# Bot.py
# Ashish D'Souza (computer_geek64)
# June 4th, 2019

import praw
from time import sleep


reddit = praw.Reddit("bot")

while True:
  with open("settings.txt", "r") as file:
    settings = file.readlines()
  
  delay = int(settings[0][settings[0].index(":") + 1:].strip())
  paragraph = "".join(settings[1:])
  
  reddit.submission("bkz2do").reply(paragraph)
  sleep(delay * 60)
