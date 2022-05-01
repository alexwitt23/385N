"""Various properties to calculate for a given image.
Return a quality measurement between 1 - 1000000
"""

import pathlib

import cv2


_IMG_EXTS = [".jpeg", ".jpg", ".png"]


def _find_all_images(image_folder: pathlib.Path):
    images = []
    for ext in _IMG_EXTS:
        images += list(image_folder.rglob(f"*{ext}"))
        images += list(image_folder.rglob(f"*{ext.upper()}"))

    return images


def calculate_images_sharpness(image_folder: pathlib.Path):
    image_sharpnesses = {}
    for image_path in _find_all_images(image_folder):
        image = cv2.imread(str(image_path))
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        image_sharpnesses[image_path] = cv2.Laplacian(gray, cv2.CV_64F).var()

    return image_sharpnesses
