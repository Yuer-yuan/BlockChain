// Please paste your contract's solidity code here
// Note that writing a contract here WILL NOT deploy it and allow you to access it from your client
// You should write and develop your contract in Remix and then, before submitting, copy and paste it here
pragma solidity ^0.5.16;

contract SplitWise {
    // address of all users
    address[] users;

    // debt from [debtor][creditor]: debts[debtor][creditor]
    mapping(address => mapping(address => uint32)) debts; 

    // helper function: check if user is new. if new, add user to users
    function check_new_user(address user) internal {
        for(uint i = 0; i < users.length; i++) {
            if(users[i] == user) {
                return;
            }
        }
        users.push(user);
    }

    // helper function: completed add_iou function
    function __add_IOU(address debtor, address creditor, uint32 amount) public {
        check_new_user(debtor);
        check_new_user(creditor);
        debts[debtor][creditor] += amount;
    }

    // return the debt from debtor to creditor
    function lookup(address debtor, address creditor) public view returns(uint32 ret) {
        ret = debts[debtor][creditor];
    }

    // add iou of amount from debtor--msg.sender to creditor
    function add_IOU(address creditor, uint32 amount) public {
        __add_IOU(msg.sender, creditor, amount);
    }

    // get users
    function getUsers() public view returns (address[] memory ret){
        ret = new address[](users.length);
        for (uint i = 0; i < users.length; i++){
            ret[i] = users[i];
        }
    }
}