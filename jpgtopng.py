import sys
import os

from PIL import Image # this is the Pillow 

#jpg to png converter

#grab first and second argument
# first argument is a folder containing the images
# second argument is a folder to store the images in

imageFolder = sys.argv[1]
outputFolder = sys.argv[2]

#check if out put folder already exists
if not os.path.exists(outputFolder):
    os.makedirs(outputFolder) #make new folder if not exist


# loop through the images folder
for file in os.listdir(imageFolder):
    img = Image.open(f'{imageFolder}{file}')

    #split the name of the file
    #returns a tuple, only want the first value
    splitName = os.path.splitext(file)[0]

    img.save(f'{outputFolder}{splitName}.png','png')
