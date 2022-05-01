"""Interface to Uber's H3 geospatial indexing."""

import pathlib

from PIL import Image
import h3

def calculate_images_hexagons(image_folder: pathlib.Path):
    image_sharpnesses = {}
    for image_path in image_folder.glob("*.jpg"):
        image = Image.open(image_path)
        print(image._getexif())
        for key, value in image.getexif():
            print(key, value)
