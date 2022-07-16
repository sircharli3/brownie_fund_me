from brownie import FundMe, network, config, MockV3Aggregator
from scripts.helpful_scripts import deploy_mock_aggregator, get_account, BLOCKCHAIN_ENV

def deploy_fund_me():
    account = get_account()
    #print(account)
    # pass price feed address to the FundMe contract (the constructor indicates this..)
    # if we are on a persistent network, like rinkeby, use the associated addr, else deploy mocks!
    if network.show_active() not in BLOCKCHAIN_ENV:
        priceFeed_addr = config["networks"][network.show_active()]["eth_usd_price_feed"]
    else:
        deploy_mock_aggregator()
        priceFeed_addr = MockV3Aggregator[-1].address #"use th emost recently deployed mock agreggator"        

    fund_me = FundMe.deploy(
        priceFeed_addr,
        {"from": account},
        publish_source=config["networks"][network.show_active()]['verify'] #T/F - publish means that etherscan.io will verify its legit contract
    ) 
    #print(f"Contract deployed to : {fund_me}")
    return fund_me

def main():
    deploy_fund_me()