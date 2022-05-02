"""Various properties to calculate for a given image.
Return a quality measurement between 1 - 1000000
"""
import math
import pathlib

import cv2

from src import file_utils


def calculate_images_sharpness(image_folder: pathlib.Path):
    image_sharpnesses = {}
    for image_path in file_utils.find_all_images(image_folder):
        image = cv2.imread(str(image_path))
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        image_sharpnesses[image_path] = math.ceil(
            min(cv2.Laplacian(gray, cv2.CV_64F).var(), 100000))

    return image_sharpnesses

def average_sharpness(image_sharpnesses):
    return sum(image_sharpnesses) / len(image_sharpnesses)