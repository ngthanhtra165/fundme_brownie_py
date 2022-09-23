from brownie import fund_mee
from scripts.helpful_scripts import get_account
from web3 import  Web3

def fund():

    #fund_me = fund_mee[-1]
    #print(fund_mee)
    #get account
    account = get_account()

    #entrance_fee = fund_me.getEntranceFee()
    #fund_me.fund({"from" : account , "value" : entrance_fee})


    # a = fund_me.get_balance()

    print(account)

def withdraw():
    fund_me = fund_mee[-1]

    #get account
    
    

def main():
    fund()