
# README
- Good website to learn smart contract security - https://scsfg.io/hackers/signature-attacks/
---
# Blockchain
- A distributed ledger operated on via a decentralized network of nodes
- Some properties
	- Immutable
	- Untamperable
	- Used to make cryptocurrency, computing machines

## Bitcoin Cryptocurrency
- Satoshi Nakamoto and his bitcoin whitepaper
- Laid the foundation of cryptocurrency
- What crypto is:
	- A system of economic exchange not controlled by a centralized entity (banks)
	- Instead managed by thousands of decentralized nodes on a peer-to-peer decentralized basis
- Bitcoin is essentially a digital currency payment network

## Etherum
- Idealized in 2014 and its inception in 2015
- A decentralized computing infrastructure witha built in Turing Complete programming language (Solidity)
- Programs called "Smart Contracts"
- The "blocks" in blockchains store all changes performed in the computing infrastructure
- Foundation of Decentralized Applications

## The core components of blockchain
### Decentralized Network
- A blockchain implementation always involves decentralized network of nodes
- Two types:
	- Permissioned (Requirement of permission for participation)
	- Permissionless (Anyone can participate)
- All of the nodes have a copy of the blockchain
- When a new block is attached, the change is communicated across all these nodes.

### Cryptography
- One of the core ideas used by blockchain 
- Used for encryption, keys, hashing and so on
	- Digital signature are used for signing transactions, identity verification, to maintain integrity
	- Hashing is used to create the immutable chain of blocks.

### Immutable Ledger
- The database of blockchain 
- What it stores
	- Transactions made by the users on the network
- In case of bitcoin (Any change in the balance of the involved users is recoreded)
- In case of ethereum (Much more complex changes in the state of the blockchain are recorded)

### Consensus
- What let's users be able to do transactions between themselves without any intermediary controlling parties involved
- A set of rules and processess which the senders and receivers in the network, agree upon, to complete a certain transaction
- The transaction is attached to the block, and updated to all nodes on the decentralized network

### Smart Contracts
- Web3, divided into
	- Client (Frontend)
	- Smart Contract (Backend)
	- Blockchain

- Smart Contracts can
	- Read data on the blockchain
	- Write new data to the blockchain
---
## Practical Demo 
- https://andersbrownworth.com/blockchain/hash
	- Key Learning:-
	- Nonce and data need to be changed multiple times to achieve the hash in a block.
	- the prev hash of the previous block is linked and the current hash is used as a pervios hash in the next block making a chain that's why its called blockchain. 
	- Due to of this blockchain is considered tamper proof because if any data is changed the current hash will be changed which results in breaking the on-going blockchain. 
---
# Ethereum
- To understand ethereum better, we can divide it into parts.
	- The Blockchain
		- An integral part of ethereum, the same as any other blockchain
		- A General purpose programmable blockchain that runs a virtual machine capable of executing code
	- The nodes and the miners
		- `Nodes` 
			- Nodes hold a copy of the blockchain
			- When a new block is attached to the chain, it gets updated across all the nodes in the network.
		- `Miners`
			- Miners run ethereum nodes that validate, execute and combine transactions into blocks, that go onto the blockchain
			- Validation, a process involving miners spending computational power
			- 'Proof of Work'
			- Miners are rewarded for blocks attached
	- The smart contracts
		- What holds executable code on the blockchain
		- Can execute specific pieces of said code
		- Some properties
			- Smary contracts have their own balance of ether and storage to keep track of variables.
			- Enable developers to build amazing Decentralized Applications
			- Once deployed, is immutable, that is, the code can never be changed

---
# Smart Contracts
- Pieces of code written in solidity and other language (Rust, Go, Python etc...), programs that are stored on the blockchain and executed by EOAs or other smart contracts.
- Just as Javascript executes in a web browser, Solidity code is always executed on the Ethereum blockchain.

## Important Terms: Address
- Address
	- Last 20 bytes of the hash of a given public key
	- How accounts and smart contracts are represented on the blockchain
- Two Types of addresses
	- Externally Owned Accounts (EOAs)
	- Contract Accounts

## Important Terms: Bytecode
- Object code that is converted into binary machine code, which can be read by a machine
- Smart Contracts written in High Level Language, converted into bytecode that can be executed by the EVM
![](../attachments/Pasted%20image%2020231221152341.png)

## Important Terms: Gas Fees
- Gas Fees
	- Unit that measures the amount of computation required to do any transaction on the blockchain (Write something to blockchain data) 
	- Comensation for computation resources used for the transaction to be completed.
	- Paid in Ethereum's Native currency, Ether (ETH)
	- Gas denoted in `gwei` such that ---> 1 gwei = 0.0000000001 ETH

## Why gas fees?
- Prevent someone trying to overload the network and try DOS Attacks.
- Also compensation for computation resources, of all the miners that keep the network running.

## Interacting with smart contracts
- User initiates a transaction using a wallet
- The transaction is verified and approved
- It includes code that defines what type of transaction is to be executed
- The transaction is added as a block  to the blockchain
- Using 
	- Web3 js Library
	- Ethers js
	- Web3 py

## Metamask
- Its an crypto wallet which is used to connect with web3 application
- It stores crypto assets.
- https://metamask.io
- `Secret Recovery Phrase` -> its an 12 word phrase which is linked to your wallet and is used to recover or import the wallet

# Decentralized Application `Dapps`
- Decentralized Applications are apps that are built on decentralized networks and are essentially a system that combines smart contracts (As Backend) and User Interface (As Frontend)

## Dapp Examples
- Decentralized Exchanges (Uniswap, Sushiswap)
- Decentralized Finances
- Games (CryptoKitties)
- Marketplace (Opensea)

## Decentralized Autonomous Organization `DAO`
### What's a DAO?
- Like any other organization, has participants, offers services
- Traditional Organizations
	- Decision are made by higher authorities like a board of directors or Executives
	- Centralized Entity makes decision for all members
- Decentralized Autonomous Organization
	- The members create the decision (Proposals) and other members vote on whether said decision should be taken or not
	- Members themselves are involved in decision making

### Advantages of DAO
- More power to the people (True Democracy)
- Autonomy (Independent of any other orgs, Governments etc.)
- Everyone is involved in running the organization

## Decentralized Exchanges
- Blockchain based applications
- Enable large scale trading of crypto assets between users
- Different types of Decentralized Exchanges
	- Order Book DEX
	- AMM  DEX

### Order Book  DEX
- The `traditional` assets trading method
- Uses an Order Book that keeps track of `buy orders` and  `sell orders`
- When a buyer uploads a buy order, the order book organizes suitable sell orders that match the buyers price.
- On Chain and Off Chain Order Books

### Automated Market Makers
- AMM stands for `Automated Market Maker`
- The goal : remove the middleman between crypto asset exchange
- Achieved using smart contracts
- Aggregates a pool of assets that is to be exchanged, eg ETH/SOL
- Uses Algorithm to determine an exchange price based on the assets that are available in the liquidity pools

## Exchanging Crpyto assets
- User A has some ETH
- They want to trade their ETH for some Token
- User goes to the exchange
- Exchange gives the user the amount of Token that can be exchanged according to the ETH/Token Pair's Liquidity Pool
- User A accepts, signs a transaction to trade.
- User A now has Token for the ETH he traded.

---
## Test network for dapps
- You can use test networks to interact with smart contracts with no real money value present for this in metamask extension go to Advance => show test network
- ropsten faucet 
- upon sending ether or making any transaction some gas fees is charged for the miners who are minning

---
# The core concept of mining in crypto transactions
- so there any mutliple ledgers and minining means finding the perfect hash which matches the blockchain to continue
- and then that hash is put on to the records of all the decentralized copies of the cryptonetwork
- and the person who is minning actually gets paid with the gas fees of the transaction

---
# Etherscan
## What's etherscan?
- Blockchain is a public ledger
- Anyone can view all transactions at any point of time
- Using etherscan
- It's a tool to view all the transactions on blockchain

## Etherscan.io
- A Block explorer and analysis tool
- Lets you view any and all transactions on the blockchain
- Available for both the mainnet and testnet => net means networks

## Etherscan for testnet
- ropsten.etherscan.io
- rinkeby.etherscan.io
- goerli.etherscan.io

---
# Remix IDE
- remix.etherium.org

---
# Solidity programming language
## How to start
```
contract MyContract {
	// Your smart contract
}
```

## Primitive Datatypes
- int : integer (signed integer)
- uint : unsigned integer => `it does not store any negative values`
- bool : Boolean (True or False)
- address : Ethereum address

### Address
```
contract MyContract {
	// 20 byte value that holds Ethereum Address
	address public myAddress; // public keyword is a visibility modifier
}
```

![](../attachments/Pasted%20image%2020231225131559.png)

- Visibility Modifier
	- public `any contract can access the variable` , private `the contract itself is able to access variable` , internal `functions internally can access this variable` , external `the variable can only be accessed externally`

### Variables
- Three types of variables
	- `Local Variables`
		- Declared inside a function
		- Not stored on the blockchain
	- `State Variables`
		- Declared outside a function
		- Stored on the blockchain
	- `Global Variables`
		- Global variables provide information about the blockchain
		- Some examples of global variables
			- `msg.sender` : address of the called of the function
			- `msg.value` : Ether sent by the caller
			- `msg.data` : Any data sent in the call
			- `block.timestamp` : Current block timestamp

> Example
```sol
Contract myContract {
// Stored on the blockchain
uint num;
string myString;
function myFunction() public {
	// Not stored on the blockchain
	uint num2;
	}
}
```

#### Playing with Global Variables
```sol
...
function newFunction() public returns (address) {
	address myAddress = msg.sender;
	return myAddress;
}
...
```

## Read and Write Operation
- Reading variables is for free without any fees
- To write a state variable, you have to send transactions with gas fees

```sol
contract Storage {
	uint256 number;

	function get() public view returns (uint256) {
		return number;
	}

	function set(uint256 num) public {
		number = num;
	}
}
```

## Functions
- Functions are sets of reusable code that can be called anywhere in the program
- Used to avoid writing the same code again and again
- Syntax
```sol
function function-name(argument) scope returns(return-values) {
	//code
}
```

### Example
```sol
function addNumber(uint a,uint b) public returns(uint) {
	uint c = a + b;
	return c;
}
```
---
### Global Variables in Solidity
```sol
pragma solidity ^0.6.0;

contract MyContract {
	uint public number1;

	function myFunction() public {
		uint num;
	}

	function newFunction() public returns (uint, address) {
		uint num1 = 12;
		uint num2 = 13;
		number1 = num1 + num2;
		address myAddress = msg.sender;
		returns(number1,myAddress);
	}
}
```