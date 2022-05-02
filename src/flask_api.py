"""Flask API to calculate reward for given set of images."""
import pathlib
import flask
import h3
from flask import request
from web3 import Web3
from solcx import compile_source
import json

from src import b2_interface
from src import image_quality
from src import h3_interface
from src import file_utils


env_variables = json.load(open('.env.json'))

w3 = Web3(Web3.HTTPProvider(env_variables["RPC_PROVIDER"]))

# "ZEPPELIN_REMAPPING_PATH" path, needs to be changed to wherever you have downloaded openzeppelin, as solcx doesn't directly download it.
compiled_sol = compile_source(open("contracts/Rewarder.sol").read(),
                            output_values=['abi', 'bin'],
                            import_remappings={'@openzeppelin/contracts/': str(pathlib.Path.cwd() / env_variables["ZEPPELIN_REMAPPING_PATH"]) + "/"}
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

    all_images = file_utils.find_all_images(image_folder)
    image_names = [image.name for image in all_images]

    # Calculate image sharpness
    average_sharpness = image_quality.calculate_images_sharpness(image_folder)
    # # Find index of image given lat long
    image_hexagons, image_exifs = h3_interface.calculate_images_hexagons(all_images)

    receiver_address = env_variables["ACCOUNT_ADDRESS"]

    # Distribute reward
    nonce = w3.eth.get_transaction_count(env_variables["ACCOUNT_ADDRESS"])

    hex_id = "00000000000"
    for hex_id, quality in zip(image_hexagons.values(), average_sharpness.values()):
        reward_txn = rewarder.functions.giveReward(receiver_address,
                    quality,
                    hex_id).buildTransaction({
                        'gas': 1500000,
                        'gasPrice': w3.toWei('3', 'gwei'),
                        'from': env_variables["ACCOUNT_ADDRESS"],
                        'nonce': nonce,
                    })

        private_key = env_variables["ACCOUNT_PRIVATE_KEY"]
        signed_txn = w3.eth.account.sign_transaction(reward_txn, private_key=private_key)

        send = w3.eth.send_raw_transaction(signed_txn.rawTransaction)

    return json.dumps({
        "reward": 0,
        "transaction_id": send.hex(),
        "image_names": image_names,
        "image_hexagons": image_hexagons,
    })

if __name__ == "__main__":
    APP.run(debug=True)
