import cv2
import imutils
import os
import argparse
from tqdm import trange

#GOAL: To create a program where it checks a directory of images and sees if each image has a certain color
#if it does it stays and if it dosnt its removed.

'''
directory - The file with all the images that should be filtered (and the file should have only images)
color - The BGR
Percentage - How much percentage of the image should be the color. If an image dosnt have this much percent of that color its removed
For example, if you set Percentage to 90, if the 90% of the image isnt that color, its removed
'''
arg_obj = argparse.ArgumentParser()
arg_obj.add_argument("directory", type=str, help="Directory of images")
arg_obj.add_argument("color", type=str, help="BGR Of Color. Format the text like \"B G R\"")
arg_obj.add_argument("percentage", type=int, help="How much percent of the image should be the color before its filtered out")
arg = arg_obj.parse_args()


DIRECTORY = arg.directory
COLOR = tuple(arg.color.split(" "))
PERCENTAGE = arg.percentage

def check_image(image_location, percentage_marker, color):
    im = cv2.imread(image_location)
    dimentions = im.shape

    is_color, total = 0, 0
    for height in range(dimentions[0]):
        for width in range(dimentions[1]):
            if tuple(im[height, width]) == color:
                is_color += 1
            total += 1

    return round(is_color / total) >= percentage_marker

os.chdir(DIRECTORY)
images = os.listdir()

for index in trange(len(images), desc="Checking Image"):
    if not check_image(images[index], PERCENTAGE, COLOR): os.remove(images[index])
