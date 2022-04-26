from brownie import accounts, my_first_contract

def write_to_contract():
    contract = my_first_contract[-1]
    name = contract.setName("Shin", {"from": accounts[0]})
    print(name)

def main():
    write_to_contract()

if __name__ == "__main__":
    main()