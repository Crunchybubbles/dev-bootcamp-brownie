pragma solidity ^0.6.7;

contract vault {
     constructor() public {owner = payable(msg.sender);}
    address payable owner;

  function isowner() public view returns (bool) {
    address addrinq;
    addrinq = msg.sender;
    return owner == addrinq;
  }


}
