#!/usr/bin/env python3

import os
import requests
# if we want to convert non json like object into json format import json
import json

# store the text file names in the list called dir_list
dir_list = os.listdir("./supplier-data/descriptions/")

# iterate through the directory and store the information in dictinalry and post this information to web
for text_file in dir_list:
    with open("./supplier-data/description/" + text_file) as file:
        # initialize the dictionary to store the text in json format
        dic = {}

        # read the file as whole by splitting lines because it is not large
        reader = file.readlines()

        # first line of the text file is the name of the item
        # we need to get rid of new line characters so, use strip()
        dic["name"] = reader[0].strip()
        # 2nd line contains the weight in lbs(i.e 200 lbs) so we nee only no in int format
        dic["weight"] = int(reader[1].strip()[:3])
        dic["description"] = reader[2].strip()

        # we need to store the image name corresponding to this text file and the image is not stored in current directory so, we need to explicitly tell the image file name (i.e file is "001.txt" for this corresponding image file is "001.jpeg")
        dic["image_name"] = text_file[:3] + ".jpeg"


        # post this data to web and store the response in variable for debugging and send data in json format
        response = requests.post("http://<IP address of the current machine>/fruits", json = dic)
