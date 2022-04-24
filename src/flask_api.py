"""Flask API to calculate reward for given set of images."""

import flask

app = flask.Flask(__name__)

@app.route("/calculate-reward")
def hello_world() -> str:
    # Download images from b2
    ...
    # Calculate image sharpness
    ...
    # Find index of image given lat long
    ...
    # Calculate reward
    ...
    # Return reward
    ...

if __name__ == "__main__":
    app.run(debug=True)

