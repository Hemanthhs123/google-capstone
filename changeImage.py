#!/usr/bin/env python3

# import Image from PIL to modify images
from PIL import Image
import os

# store the files in the images directory
image_list = os.listdir('./supplier_image_upload.py/images/')

# iterate through the images in the folder and modify image
for image in image_list:
    # if image is .tiff image i.e. it endswith .tiff extension then continue
    if image.endswith(".tiff"):
        # open the image using Image module
        with Image.open('./supplier-data/images/' + image) as im:
            # resize the image to 600, 400 size with RGB (RGB is the way that image has to be converted before saving in to .jpeg file)
            new_im = im.resize((600, 400)).convert('RGB')

            # save the newly generated image in .jpeg extension in the same folder
            new_im.save('./supplier-data/images/'+ image.split(".")[0] + '.jpeg') 
