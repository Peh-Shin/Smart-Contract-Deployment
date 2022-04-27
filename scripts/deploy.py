from brownie import address_book, accounts

def deploy_contract(): 
    contract = address_book.deploy({"from": accounts[0]})
    return contract

def main():
    deploy_contract()

if __name__ == "__main__":
    main()