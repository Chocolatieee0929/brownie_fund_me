from brownie import FundMe, MockV3Aggregator, network, config
from scripts.helpful_scripts import (
    get_account, 
    deploy_mocks,
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,FORKED_LOCAL_ENVIROMENTS,
)


def deploy_fund_me():
    account = get_account()
    print(account)
    # pass the price feed address to thid contract
    if (
        network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS
        and FORKED_LOCAL_ENVIROMENTS 
    ):
        price_feed_address = config["networks"]["sepolia"][
            "eth_usd_price_feed"
        ]
    else:
        # 如果是私链就需要考虑 
        if len(MockV3Aggregator) <= 0:
            deploy_mocks(account)
        price_feed_address = MockV3Aggregator[-1].address

    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify")
    )
    print(f"Contract deployed to {fund_me.address}")
    return fund_me


def main():
    print(f"The active network is {network.show_active()}")
    deploy_fund_me()