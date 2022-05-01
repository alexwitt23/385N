"""Flask API to calculate reward for given set of images."""

from web3 import Web3
import h3
from solcx import compile_source
import os, json

H3_RESOLUTION = 10

env_variables = json.load(open('../.env.json'))

w3 = Web3(Web3.HTTPProvider(env_variables["RPC_PROVIDER"]))
# Web3.toChecksumAddress(lower_case_address)
# "ZEPPELIN_REMAPPING_PATH" path, needs to be changed to wherever you have downloaded openzeppelin, as solcx doesn't directly download it.
compiled_sol = compile_source(open("../contracts/Rewarder.sol").read(),
                            output_values=['abi', 'bin'],
                            import_remappings={'@openzeppelin/contracts/': env_variables["ZEPPELIN_REMAPPING_PATH"]}
                        )
contract_id, contract_interface = compiled_sol.popitem()
bytecode = contract_interface['bin']
abi = contract_interface['abi']

rewarder = w3.eth.contract(address=env_variables["ADDRESS_SMART_CONTRACT"], abi=abi) # 0x9ADEA578c48E4285E2d31eF7bd81c99Fb19dAA25

def calculate_reward():
    ############### Need to change ###############
    latitude, longitude = 10.0, 10.0 # get_lat_long()
    hex_id = h3.geo_to_h3(latitude, longitude, H3_RESOLUTION)
    quality = 1000 # Quality is between 1 and 100000
    receiver_address = env_variables["ACCOUNT_ADDRESS"]
    ############### Need to change ###############


    # Distribute reward
    assert 1 < quality < 100000
    nonce = w3.eth.get_transaction_count(env_variables["ACCOUNT_ADDRESS"])

    reward_txn = rewarder.functions.giveReward(receiver_address,
                quality,
                hex_id).buildTransaction({
                    'gas': 1500000,
                    'gasPrice': w3.toWei('3', 'gwei'),
                    'from': env_variables["ACCOUNT_ADDRESS"],
                    'nonce': nonce,
                })
    print(nonce)
    private_key = env_variables["ACCOUNT_PRIVATE_KEY"]
    signed_txn = w3.eth.account.sign_transaction(reward_txn, private_key=private_key)
    print(signed_txn)
    send = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
    print(send)

    return {"reward": 0}

if __name__ == "__main__":
    calculate_reward()

