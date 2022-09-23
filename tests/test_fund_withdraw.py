
from threading import activeCount
from scripts.helpful_scripts import get_account , local_enviroment
from scripts.deploy import deploy_fund_me
from brownie import network,accounts , exceptions
import pytest

def test_can_fund_withdraw():
    account = get_account()
    
    fund_me = deploy_fund_me()
    #get_fee
    entrance_fee = fund_me.getEntranceFee()

    ha = fund_me.fund({"from" : account ,"value" : entrance_fee})
    ha.wait(1)

    assert fund_me.addressToAmountFunded(account.address) == entrance_fee

    tx2 = fund_me.withdraw({"from": account})
    tx2.wait(1)

    assert fund_me.addressToAmountFunded(account.address) == 0


def test_only_local():
    if network.show_active() not in local_enviroment:
        pytest.skip("only for local")
    
    account = get_account()
    fund_me = deploy_fund_me()

    bad_actor = accounts.add()

    with pytest.raises(exceptions.VirtualMachineError):
        fund_me.withdraw({"from" : bad_actor})



