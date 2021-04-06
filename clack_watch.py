# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 12:57:23 2021

@author: alanj
"""
import time 
import requests #for retreiving coronavirus data from web
from plyer import notification #for getting notification on your PC
from bs4 import BeautifulSoup
import re

while True:
    # set the url as clack,
    url = "https://www.elitekeyboards.com/shop"
    # set the headers like we are a browser,
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    # download the homepage
    response = requests.get(url, headers=headers)
    # parse the downloaded homepage and grab all text, then,
    soup = BeautifulSoup(response.text, "html.parser")
    time.sleep(5)
    
    # if the number of times the word "clack factory" occurs on the page is != 3,
    if len(soup.find_all("h3", string=re.compile("Clack Factory"))) == 3:
        # wait 60 seconds,
        print("#clacks = ", len(soup.find_all("h3", string=re.compile("Clack Factory"))))
        time.sleep(15)
        # continue with the script,
        continue
        
    # but if the word "clack factory" occurs any other number of times,
    else:
        # make notification
        notification.notify(
            title = "New Clack Skull in store!",
            message = "Go get it idjit",
            app_icon = "clack.ico",
            timeout = 10
        )
        break
