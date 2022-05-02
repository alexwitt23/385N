"""Interface to Uber's H3 geospatial indexing."""

import pathlib
from typing import List

from PIL import Image
import h3

_NO_LOCATION_HEXAGON = "000000000"


def calculate_images_hexagons(images: List[pathlib.Path]):
    image_hexagons, image_exifs = {}, {}
    for image_path in images:
        image = Image.open(image_path)
        image_exifs[image_path.name] = {key: value for key, value in image.getexif().items()}
        for key, value in image.getexif().items():
            if key == "GPSInfo":
                image_hexagons[image_path.name] = h3.geo_to_h3(value[0], value[1])
            else:
                image_hexagons[image_path.name] = _NO_LOCATION_HEXAGON
    
    return image_hexagons, image_exifs
