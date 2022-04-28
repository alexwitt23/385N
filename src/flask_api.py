"""Flask API to calculate reward for given set of images."""

import b2
import flask
from flask import request
from web3 import Web3
from solcx import compile_source
import os

from src import b2_interface
from src import image_quality
from src import h3_interface

w3 = Web3(Web3.HTTPProvider('https://polygon-mumbai.infura.io/v3/'))

# The following hardcoded path, needs to be changed to
# wherever you have downloaded openzeppelin, as solcx doesn't directly download
compiled_sol = compile_source(open("contracts/Rewarder.sol").read(),
                            output_values=['abi', 'bin'],
                            import_remappings={'@openzeppelin/contracts/': '/Users/ayushk4/.solcx/openzeppelin-contracts-4.5.0/contracts/'}
                        )
contract_id, contract_interface = compiled_sol.popitem()
bytecode = contract_interface['bin']
abi = contract_interface['abi']

rewarder = w3.eth.contract(address=os.environ["ADDRESS_SMART_CONTRACT"], abi=abi) # 0x9ADEA578c48E4285E2d31eF7bd81c99Fb19dAA25
nonce = w3.eth.get_transaction_count(os.environ["ACCOUNT_ADDRESS"])

reward_txn = rewarder.functions.owner().buildTransaction({'chainId': 1,
                'gas': 700000,
                'maxFeePerGas': w3.toWei('2', 'gwei'),
                'maxPriorityFeePerGas': w3.toWei('1', 'gwei'),
                'nonce': nonce,
            })

private_key = os.environ["ACCOUNT_PRIVATE_KEY"]
signed_txn = w3.eth.account.sign_transaction(unicorn_txn, private_key=private_key)

w3.eth.send_raw_transaction(signed_txn.rawTransaction)

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

