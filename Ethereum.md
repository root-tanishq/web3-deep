
# Ethereum Basics 
## What is Ethereum?

- Founded by Vitalik Buterin
- the core concept is to run programs on the blockchain
- kind of adding applications to the whole blockchain concept
- We can create decentralize applications
- Ethereum provides token which can help to run blockchain applications
- the coin is `ETHER`

## Ethereum nodes

### Types of node

- Full node ⇒ Locally stores the entire copy of blockchain for verification purposes
- Archive node ⇒ Stores everything kept in full nodes and built an archive of historical data, Requires terabyte of diskspace
- Light node ⇒Stores only the block header , depends on full node

## Ethereum Accounts

An ethereum accounts is an entity  with an ether (ETH) balance that can send or receive transactions of ethereum.

## Types of Ethereum Accounts
- Externally Owned Accounts (EOA) - A wallet owned by a person or a user , similar to a bank account of an human
- Contract Account (CA)
	- Controlled by contract code - SMART CONTRACT 

| Externally Owned Account | Contract Account                                                            |
| ------------------------ | --------------------------------------------------------------------------- |
| Private key is needed    | No private or public key is needed                                          |
| Controlled by Human      | Controlled by Contract Account                                              |
| No gas is associated     | Gas is associated                                                           |
| Has a unique address     | Has a unique address                                                        |
| Holds ETH balance        | Holds ETH balance and perform functionalities mention on the smart contract |

# Smart Contract
- Its an program which is runned on the ethereum blockchain 
- Coding language is solidity for interacting with etherum blockchain 
- Its a Turing complete language which means loops can also be written in solidity language

## Each node has the following:-
- Current state of all smart contracts.
- History of both transaction and smart contract.

# Decentralized Applications | DAPPS
- An application which runs in decentralized network
- It runs all the node of the blockchain
- Smart Contract + Front End = Dapp
- Examples of DAPPS- Preseach , LBRY , D.tube

| Centralized Application | Decentralized Application |
| ----------------------- | ------------------------- |
| Not Trustwothy          | Trustworthy               |
| Censorship              | No censorship             |
| You pay                 | They pay                  |
| Go down                 | Can never go down         |

# Ethereum Virtual Machine | EVM
- Its an virtual machine to run the etherum code so that the virtual machine and ethereum blockchain is not able to directly contact the host computer and its peripherals

# Ethereum Gas
- cost of running / interacting with the smart contract on the etherum blockchain . Its calculated according to the tasks performed by the smart contract
- Cost of gas according to the task performed are mentioned here :- https://ethereum.org/en/developers/docs/evm/opcodes/

## Points to note:-
- Any transaction that modifies the blockchain cost gas.
- The user that generated the transaction pays for the gas.

## Ethereum Gas price
- It is the amount the sender wants to pay per unit of gas to get the transaction mined. gasPrice is set by the sender.
- Gas price are denoted in gwei (1 gwei = 10^-9 ETH or 0.000000001 ETH)
- The higher the gas price the faster the transaction will be mined. It just like the transaction in bitcoin.

## Ethereum Gas limit
- Its the maximum gas the transaction can consume.
- set by the sender.

# Etherum Block / Demo

- All the ethereum live transactions can be seen here - https://etherscan.io/blocks

# Decentralized Autonomous Organization | DAO
- DAO (Decentralized Autonomous Organization) in Ethereum is a self-governing entity operating through smart contracts and governed by its participants.
- Its a smart contract

| DAO (Decentralized Autonomous Organization) | A traditional organization                                            |
| ------------------------------------------- | --------------------------------------------------------------------- |
| Fully democratized                          | Usually hierarchical                                                  |
| Voting required                             | Voting may or may not require.                                        |
| No trusted intermediary to count vote       | Outcome of voting must be handled or centrally controlled automation. |
| Service offered are handled automatically   | Requires human handling or centrally controlled automation            |
| All activity is transparent and full public | Activity is typically private, and limited to the public              |
# Hard Fork
- During a hard fork software implementing a protocol and its mining procedures is upgraded.
- Once a user upgrades their software, that version rejects all transactions from older software, effectively creating a new branch of the blockchain.
- on 20/07/2016 there was done a hard fork on ethereum blockchain due to The DAO Attack.
- Ethereum Classic -> Follows the classic old rules of smart contract .
- However those who retain the old software continue to process transactions.
- Ethereum -> New chain which changed the smart contract due to the loss of The DAO Attack.

# Soft Fork
- Soft fork are a change to the protocol, but the end product remains unchanged.
- A soft fork is a backward compatible upgrade, meaning that the upgraded nodes can still communicate with the non-upgradable ones.
- Old nodes (not upgraded nodes) could still validate blocks and transactions (the formatting didn't break the rules), but they just didn't wouldn't understand them.

# Inital Coin Offering | ICO
- An Initial Coin Offering (ICO) in the context of Ethereum refers to a fundraising method commonly used by blockchain-based projects to raise capital for their development. It involves the issuance of a new cryptocurrency or token by a project or company to investors in exchange for legal tender or other established cryptocurrencies, typically Ethereum (ETH).
- Token holders doesn't control the orgranization.
- Less legal work is required to acquire tokens.

# Ethereum 2.0 | Serenity | ETH 2.0
- Ethereum 2.0 represents a significant upgrade to the Ethereum network, transitioning from a proof-of-work to a proof-of-stake consensus mechanism. This shift promises increased scalability, security, and sustainability by implementing features like shard chains, which enable parallel transaction processing, and the Beacon Chain for managing validator staking and rewards.
### Major Upgrades
- Proof of Stake (POS)
- Sharding

## Proof of Stake
- validators are used to verify the work instead of miners.
- The more ether you pay the more chances of getting randomly selected you have.

| Proof of Work                                                    | Proof of Stake                                          |
| ---------------------------------------------------------------- | ------------------------------------------------------- |
| Miners                                                           | Validators                                              |
| High performing hardware required                                | Mobile or Laptop are enough                             |
| Lots of electricity required.                                    | Not much electricity is required.                       |
| The more hashing power you have the more blocks you can validate | The more ETH you stake the more blocks you can validate |
| Attack to happen 51% hashing power is required.                  | Attack to happen 51% of stake is required.              |
| Competition is there                                             | Random selection of validators                          |
## Sharding in Ethereum
-   Sharding in Ethereum involves partitioning the network into smaller groups of nodes to improve scalability by allowing parallel processing of transactions. This enhances the network's capacity to handle a higher throughput of transactions while maintaining decentralization.
### Advantages
- Transaction per second increases.
- Powerful and expensive computers will not be needed.
- More validators will join.
- Reduce in energy consumption.
