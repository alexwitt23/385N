"""Flask API to calculate reward for given set of images."""

import b2
import flask
from flask import request

from src import b2_interface
from src import image_quality
from src import h3_interface

APP = flask.Flask(__name__)


@APP.route("/calculate-reward")
def calculate_reward() -> str:
    # Parse archive
    archive_name = request.args.get("archive", default=None, type=str)

    # Download images from b2
    image_folder = b2_interface.download_archive(archive_name)

    # Calculate image sharpness
    # average_sharpness = image_quality.calculate_images_sharpness(image_folder / "color")

    # Find index of image given lat long
    h3_interface.calculate_images_hexagons(image_folder / "color")

    # Calculate reward
    ...
    # Return reward
    ...
    return {"reward": 0}


if __name__ == "__main__":
    APP.run(debug=True)
