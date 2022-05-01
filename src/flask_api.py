"""Flask API to calculate reward for given set of images."""

import b2
import flask
import h3
from flask import request
from web3 import Web3
from solcx import compile_source
import os, json

from src import b2_interface
from src import image_quality
from src import h3_interface


env_variables = json.load(open('.env.json'))

w3 = Web3(Web3.HTTPProvider(env_variables["RPC_PROVIDER"]))

# "ZEPPELIN_REMAPPING_PATH" path, needs to be changed to wherever you have downloaded openzeppelin, as solcx doesn't directly download it.
compiled_sol = compile_source(open("../contracts/Rewarder.sol").read(),
                            output_values=['abi', 'bin'],
                            import_remappings={'@openzeppelin/contracts/': env_variables["ZEPPELIN_REMAPPING_PATH"]}
                        )
contract_id, contract_interface = compiled_sol.popitem()
bytecode = contract_interface['bin']
abi = contract_interface['abi']

rewarder = w3.eth.contract(address=env_variables["ADDRESS_SMART_CONTRACT"], abi=abi) # 0x9ADEA578c48E4285E2d31eF7bd81c99Fb19dAA25

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



    ############### Need to change ###############
    latitude, longitude = 10.0, 10.0 # get_lat_long()
    hex_id = h3.geo_to_h3(latitude, longitude, H3_RESOLUTION)
    quality = 1000 # Quality is between 1 and 100000
    receiver_address = env_variables["ACCOUNT_ADDRESS"]
    H3_RESOLUTION = 10
    ############### Need to change ###############


    # Distribute reward
    assert 1 < quality < 100000
    nonce = w3.eth.get_transaction_count(env_variables["ACCOUNT_ADDRESS"])

    reward_txn = rewarder.functions.giveReward(receiver_address, quality, hex_id).buildTransaction({'chainId': 1,
                    'gas': 70000000,
                    'maxFeePerGas': w3.toWei('2', 'gwei'),
                    'maxPriorityFeePerGas': w3.toWei('1', 'gwei'),
                    'nonce': nonce,
                })

    private_key = env_variables["ACCOUNT_PRIVATE_KEY"]
    signed_txn = w3.eth.account.sign_transaction(reward_txn, private_key=private_key)

    w3.eth.send_raw_transaction(signed_txn.rawTransaction)

    return {"reward": 0}

if __name__ == "__main__":
    APP.run(debug=True)

