from asyncio import exceptions
from logging import exception
from scripts.fund_and_withdraw import get_account
from scripts.deploy import deploy_fund_me, BLOCKCHAIN_ENV
import pytest
from brownie import network, accounts, exceptions

def test_can_fund_and_withdraw():
    account = get_account()
    fund_me_contract = deploy_fund_me()
    entrance_fee = fund_me_contract.getEntranceFee() + 100
    tx = fund_me_contract.fund({"from": account, "value": entrance_fee})
    tx.wait(1)
    assert fund_me_contract.addressToAmountFunded(account.address) == entrance_fee

    tx2_withdraw = fund_me_contract.withdraw({"from":account})
    tx2_withdraw.wait(1)
    assert fund_me_contract.addressToAmountFunded(account.address) == 0

   
#test - only owner can wthdraw
def test_only_owner_can_withdraw(): 
    #to skip this test if we are not on a local network
    if network.show_active() not in BLOCKCHAIN_ENV:
        print(f"Your current active network is: {network.show_active()}")
        pytest.skip("Skipping test: test_only_owner_can_withdraw : this is only for local networks")
    
    #deploy test
    fund_me = deploy_fund_me()
    account = get_account()
    bad_actor = accounts.add()
    #fund_me.withdraw({"from":account}) # the owner, passes, good.
    with pytest.raises(exceptions.VirtualMachineError):
        fund_me.withdraw({"from":bad_actor})
    

 
        
    


    

