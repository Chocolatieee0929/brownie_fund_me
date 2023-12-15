from brownie import network, MockV3Aggregator, accounts, config
from web3 import Web3

FORKED_LOCAL_ENVIROMENTS = ["mainnet-fork", "mainnet-fork-dev"]
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local"]

DECIMALS = 18
STARTING_PRICE = 2000

def get_account():
    if (
        network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS
        or FORKED_LOCAL_ENVIROMENTS    
    ):
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])
    
def deploy_mocks(account):
    print(f"The active network is {network.show_active()}")
    print(f"Deploying Mock...")
    MockV3Aggregator.deploy(
        DECIMALS, Web3.toWei(STARTING_PRICE, "ether"), {"from":account}
    )
    print("Mocks Deployed!")