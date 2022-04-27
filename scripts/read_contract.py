from brownie import accounts, address_book


def read_contract_mapping():
    contract = address_book[-1]
    address = contract.getAddress(accounts[1])
    print(accounts[1])


def read_contract_array():
    contract = address_book[-1]
    print(contract.addresses(accounts[0]))


def main():
    read_contract_array()


if __name__ == "__main__":
    main()
