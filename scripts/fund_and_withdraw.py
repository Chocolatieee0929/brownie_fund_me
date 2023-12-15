from brownie import FundMe
from scripts.helpful_scripts import get_account
from scripts.deploy import deploy_fund_me
from brownie.exceptions import VirtualMachineError


def fund():
    deploy_fund_me()
    fund_me = FundMe[-1]
    account = get_account()
    try:
        entrance_fee = fund_me.getEntranceFee() + 100
    except VirtualMachineError as e:
        print(f"Revert reason: {e}")
    print("Funding....")
    fund_me.fund({"from":account, "value": entrance_fee})


def withdraw():
    account = get_account()
    for fund_me in FundMe:    
        fund_me.withdraw({"from":account})


def main():
    fund()
    withdraw()