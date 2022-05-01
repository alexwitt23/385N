import h3
import random

H3_RESOLUTION = 9
test_latitude, test_longitude = 10.0, 10.0 # get_lat_long()

def get_hexid_from_image(path):
    return random.choice([h3.geo_to_h3(latitude, longitude, H3_RESOLUTION), "test"])