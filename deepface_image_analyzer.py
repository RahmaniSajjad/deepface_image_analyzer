"""
The code uses the DeepFace library to analyze the gender, age, and dominant emotion of a person in an image.
It first loads an image using OpenCV and then passes it to the analyze function of the DeepFace library.
The actions parameter specifies the types of analysis to perform on the image.

The code then prints whether the person in the image is a man or a woman and their estimated age.
It also prints the dominant emotion expressed by the person in the image.
The time.sleep function is used to add delays between each printed message for better readability.
"""

import time  # import time module to pause for a moment before printing results
import cv2  # import OpenCV module for image processing
from deepface import DeepFace  # import DeepFace module for facial analysis

# set the path of the image you want to analyze
img_path = "pic.png"

# read the image using OpenCV and store it in a variable
img = cv2.imread(img_path)

# analyze the image using DeepFace and store the results in a variable
analyze = DeepFace.analyze(img, actions=("gender", "age", "emotion"))

# print "Man or Woman?" to the console and pause for 2 seconds
print("Man or Woman?")
time.sleep(2)

# if the gender is male, print "Man" to the console and pause for 1 second
# then print "How Old Does He Look?" to the console and pause for 2 seconds
# then print the estimated age to the console and pause for 1 second
# then print "How Does He Feel?" to the console and pause for 2 seconds
# then print the dominant emotion to the console
if analyze["gender"] == "Man":
    print(analyze["gender"])
    time.sleep(1)
    print("How Old Does He Look?")
    time.sleep(2)
    print(analyze["age"])
    time.sleep(1)
    print("How Does He Feel?")
    time.sleep(2)
    print(analyze['dominant_emotion'])

# if the gender is female, print "Woman" to the console and pause for 1 second
# then print "How Old Does She Look?" to the console and pause for 2 seconds
# then print the estimated age to the console and pause for 1 second
# then print "How Does She Feel?" to the console and pause for 2 seconds
# then print the dominant emotion to the console
else:
    print(analyze["gender"])
    time.sleep(1)
    print("How Old Does She Look?")
    time.sleep(2)
    print(analyze["age"])
    time.sleep(1)
    print("How Does She Feel?")
    time.sleep(2)
    print(analyze['dominant_emotion'])
