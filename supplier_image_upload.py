#!/usr/bin/env python3

# import requwsts to conenct to the internet
import requests
import os

# upload the image in directory to web

url = "http://localhost/upload/"
lisdir = os.listdir("./supplier-data/images/")
for image_file in lisdir:
    # for all image_files ending with .jpeg extension in the given directory
    if image_file.endswith(".jpeg"):
        # open the image file in read bianry mode to post into the web
        with open("./supplier-data/images/"+image_file, 'rb') as opened:
            # store the output in r to get the status code of the response
            r = requests.post(url, files={'file': opened})
            # we can print(r.status code for our reference 200 range is for success, 400 client 
            # error 500 server problem)