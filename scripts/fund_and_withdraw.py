from threading import activeCount
from brownie import FundMe
from scripts.helpful_scripts import get_account

def fund():
    fund_me = FundMe[-1] #the most recently deployed contract
    account = get_account()
    entranceFee = fund_me.getEntranceFee()
    print(f"The current entrance fee is: {entranceFee}")
    print("Funding..")
    fund_me.fund({"from": account, "value": entranceFee})
    return fund_me

def withdraw():
    fund_me = FundMe[-1]
    account = get_account()
    print("Withdrawing..")
    fund_me.withdraw({"from": account})
    return fund_me

def main():
    fund()
    withdraw()