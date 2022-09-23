from unittest.mock import Mock
from brownie import accounts , config , fund_mee , network , MockV3Aggregator
import os
from scripts.helpful_scripts import (deploy_mock, get_account,local_enviroment)

def deploy_fund_me():
    #account = accounts.add(config["wallets"]["from_key"])
    print(network.show_active())
    eth_usd_address = 0
    if network.show_active() not in local_enviroment:
        eth_usd_address = config["address"][network.show_active()]["ETH_USD"]
    else:
        deploy_mock()
        eth_usd_address = MockV3Aggregator[-1].address

    print(eth_usd_address)
    print(get_account())
    #print(len(MockV3Aggregator))
    fund_me = fund_mee.deploy(eth_usd_address , { "from" : get_account()} , 
    publish_source = config["address"][network.show_active()]["verify"])

    entrance_fee = fund_me.getEntranceFee()
    fund_me.fund({"from" : get_account() , "value" : entrance_fee})

    
def main():
    deploy_fund_me()