# Creating Solidity Contract on ETH Blockchain

![contract](https://image.shutterstock.com/z/stock-photo-two-hands-handshake-polygonal-low-poly-hud-illustration-smart-contract-agreement-blockchain-and-1161295627.jpg)


## Created contracts will do several things:

* Pay your associate-level employees quickly and easily.

* Distribute profits to different tiers of employees.

* Distribute company shares for employees in a "deferred equity incentive plan" automatically.

## Files

* [`AssociateProfitSplitter.sol`](contracts/AssociateProfitSplitter.sol) — Level 1 contract.

* [`TieredProfitSplitter.sol`](contracts/TieredProfitSplitter.sol) — Level 2 contract.

* [`DeferredEquityPlan.sol`](contracts/DeferredEquityPlan.sol) — Level 3 contract.

* [`DeferredEquityPlanFastForward.sol`](contracts/DeferredEquityPlanFastForward.sol) — Level 3 test contract.

## Instructions

This assignment has three levels of difficulty, with each contract increasing in complexity and capability. 

* **Level One** is an `AssociateProfitSplitter` contract. This will accept ether into the contract, and divide it evenly among associate-level employees. This will allow the human resources department to pay employees quickly and efficiently.

* **Level Two** is a `TieredProfitSplitter` that will distribute different percentages of incoming ether to employees at different tiers/levels. For example, the CEO gets paid 60%, CTO 25%, and Bob gets 15%.

* **Level Three** is a `DeferredEquityPlan` that models traditional company stock plans. This contract will automatically manage 1000 shares, with an annual distribution of 250 shares over four years for a single employee.

### Projects

### Level One: The `AssociateProfitSplitter` Contract

The ETH will be distributed evenly into associate-level employees' wallet addresses.

![associatesplitter](Images/associatesplitter.gif)

### Level Two: The `TieredProfitSplitter` Contract

The ether will be distributed to different tiers of employees (CEO, CTO, and Bob) based on various percentages(60%, 25% and 15%).

![TieredProfitSplitter](Images/TieredProfitSplitter.gif)

### Level Three: The `DeferredEquityPlan` Contract

In this contract, we will be managing an employee's "deferred equity incentive plan," in which 1000 shares will be distributed over four years to the employee. We won't need to work with ether in this contract, but we will be storing and setting amounts that represent the number of distributed shares the employee owns, and enforcing the vetting periods automatically.

In addition, the fastforward function has been utilised to manipulate current time during testing.

![fastforwardDeferredEquityPlan](Images/fastforwardDeferredEquityPlan.gif)

### Deploy the contracts to a live Testnet

Live Test Net Ropsten and Contract Addresses:

* Associate Profit Spliter: 0x68BF27dBb630a3818E4d488C86AeB436F63E1989
* Tiered Profit Spliter: 0xDC83D8201964e45b74E504481Dc1306f99ab5d26 
* Deferred Equity Plan: 0x75f2bAC6Ecb37f9554cC481f3434E00D65b8B88e
* Deferred Equity Plan with Fastforward: 0x2f4fE65F61254ca3cE50Ca649795eE2Fd0dAe055

