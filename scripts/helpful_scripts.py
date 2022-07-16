from brownie import accounts, config, network, MockV3Aggregator
from web3 import Web3

DECIMALS = 8
STARTING_PRICE = 200000000000 #eth price as a mock

#forked env
FORKED_LOCAL_ENV = ["mainnet-fork-dev"]

#"development" means that it is a testnet blockchain (rinkeby, kovan, etc)
#"ganache-local" is a development but in the context that it is "local" blockchain.
BLOCKCHAIN_ENV = ["development","ganache-local"] #to help us "define" what a "local" blockchain is.

def get_account():
    if network.show_active() in BLOCKCHAIN_ENV or network.show_active() in FORKED_LOCAL_ENV:
        return accounts[0]
    else:
        return accounts.add(config['wallets']['from_key'])

def deploy_mock_aggregator():
    print(f"Active network is {network.show_active()}")
    print("Deploying Mock Aggregator...")

    if len(MockV3Aggregator) <= 0: #maybe we already deployed a mock aggregator, check, we just need 1 for our tests.
        #new mock aggregator not prev deployed        
        MockV3Aggregator.deploy(
            DECIMALS, STARTING_PRICE, {"from": get_account()}
        ) #the constructor (from the MockV3Aggregator.sol) requires 2 paramaters to be passed in.
    print("Mock aggregator deployed!")    