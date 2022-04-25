pragma solidity ^0.8.6;

contract my_first_contract{
    
    // Setting visibility to private here as don't want getter functions to be created for the public variables
    // The variables should only be accessed through the functions itself 
    uint private age;
    string private name;

    function setName(string memory _name) public{
        name = _name;
    }
    
    function setAge(uint _age) public{
        require(_age > 0, "Age must be a positive number");
        age = _age;
    }

    function getName() public view returns (string memory){
        return name;
    }

    function getAge() public view returns (uint){
        return age;
    }
}