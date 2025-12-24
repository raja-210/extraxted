#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8459755418:AAGgfaQmHE2tkuc")
    API_ID = int(os.environ.get("API_ID", "23276426"))
    API_HASH = os.environ.get("API_HASH", "b13350fcfc")
    AUTH_USERS = "52983"

