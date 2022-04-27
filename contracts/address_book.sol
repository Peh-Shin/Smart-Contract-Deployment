pragma solidity ^0.8.6;

contract address_book{
    mapping (address => address[]) private _addresses;   

    mapping (address(address))

    function storeAddress(string memory _name) public{
        accounts.push(msg.sender);
        addresses[msg.sender] = _name;
    }
    function getAddress(address account) public view returns (string memory){
        return addresses[account];
    }
}