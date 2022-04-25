from brownie import my_first_contract, accounts

def deploy_contract(): 
    contract = my_first_contract.deploy({"from": accounts[0]})
    return contract

def main():
    deploy_contract()

if __name__ == "__main__":
    main()