
from brownie import accounts , config , network, MockV3Aggregator
from web3 import Web3

decimal = 18
amout = 2000

fork_local_environment = ["mainnet-fork"]
local_enviroment = ["development" , "ganache-local"]

def deploy_mock() :
    print(f"the network is {network.show_active()}")
    print(get_account())
    print("Deploying mocks")
    if len(MockV3Aggregator) <= 0:
        hello = MockV3Aggregator.deploy(18 ,Web3.toWei(amout , "ether") , {"from" : get_account()})
    
    #res = hello.get_res()
    #print(res)
    #print(f"mock address = {mock.address}")
    #print("deployed the mock")
def get_account():
    if network.show_active() in local_enviroment or network.show_active() in fork_local_environment:
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])

