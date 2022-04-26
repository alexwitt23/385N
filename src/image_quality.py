"""Various properties to calculate for a given image."""

import pathlib

import cv2


def calculate_images_sharpness(image_folder: pathlib.Path):
    image_sharpnesses = {}
    for image_path in image_folder.glob("*.jpg"):
        image = cv2.imread(str(image_path))
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        image_sharpnesses[image_path] = cv2.Laplacian(gray, cv2.CV_64F).var()

    return image_sharpnesses
