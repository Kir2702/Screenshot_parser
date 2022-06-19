# -*- coding: utf-8 -*-
import os
import time
import string
import random
import _thread
import requests

# Discription
print("###############################################################################\n"
      "#                               !!! Attention !!!                             #\n"
      "# This script can pull a totally random screenshot.                           #\n"
      "# The author is not responsible for the content obtained with this parser.    #\n"
      "# The content find by this parser is freely available at https://i.imgur.com/ #\n"
      "###############################################################################\n\n"
      "This script eats a lot of traffic, if you are not sure about\n"
      "in capacity of your Internet connection is recommended to\n"
      "choose no more than 3 threads.\n")

# Set the number of threads
tread_amount = None
while True:
    tread_amount = int(input("Please specify the number of threads to run the parser (from 1 to 30): "))
    if tread_amount >= 1 and tread_amount <= 30:
        break
    else:
        print("Incorrect value")

# Check if there is a directory, create it if there is no directory
try:
    os.mkdir("screenshot")
except:
    None

# Getting a valid url and saving a screenshot
variants = (string.ascii_lowercase + string.ascii_letters + string.digits + string.digits)
def urls_generator(thread):
    while True:
        url = "https://i.imgur.com/"
        length = random.choice((5, 6))
        if length == 5:
            for i in range(5):
                url += random.choice(variants)
        if length == 6:
            for i in range(6):
                url += random.choice(variants)
        url += ".jpg"
        filename = url.rsplit("/", 1)[-1]
        r = requests.get(url, timeout=10)
        img = r.content
        if str(img)[2:17] != "<!doctype html>" and len(r.content) != 503:
            with open("screenshot/" + filename, "wb") as f:
                f.write(img)
            print("[DONE]__" + filename)
        else:
            None
            #print("[FAIL]__" + filename)

# Thread generation
for thread in range(1, tread_amount + 1):
    thread = str(thread)
    try:
        _thread.start_new_thread(urls_generator, (thread,))
    except:
        print("Error when creating a thread " + thread)
print("Successfully launched " + thread + " thread.")
while True:
    time.sleep(0.5)