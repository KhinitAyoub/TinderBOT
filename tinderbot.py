#!/usr/bin/env python2\
# -*- coding: utf-8 -*-\
"""
Created on Wed May 20 18:48:58 2020

@author: khinitayoub
"""
from bot import tinderbot
from secrets import nbr_likes

if __name__ == "__main__":
    bot = tinderbot()
    bot.login(nbr_likes)


