from brownie import accounts, address_book


def write_to_contract():
    contract = address_book[-1]
    name = contract.storeAddress("Shin", {"from": accounts[1]})
    print(f"{name} transaction was successful!")


def main():
    write_to_contract()


if __name__ == "__main__":
    main()
