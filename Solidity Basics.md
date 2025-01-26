# Solidity Basics
- extension for files is `.sol`
---
![Solidity compilation process](https://www.youtube.com/watch?v=opHjPETCh68&list=PLgPmWS2dQHW9u6IXZq5t5GMQTpW7JL33i&index=5)

![](../attachments/Pasted%20image%2020240118223558.png)
- Without `ABI` you can't communicate functions of  `.sol` files
### Smart Contract Comilation some important keypoints
- Contract bytecode is public in readable form
- Contract doesn't have to be public 
- Bytecode is immutable
- ABI acts as a bridge between applications and smart contract
- ABI and bytecode cannot be generated without source code.
---
![Mainnet VS Testnet](https://www.youtube.com/watch?v=ux91QP1Yuy4&list=PLgPmWS2dQHW9u6IXZq5t5GMQTpW7JL33i&index=5)

# Mainnet v/s Testnet

| Mainnet | Testnet |
| ---- | ---- |
| Used for actual transactions with value | Used for testing smart contracts and decentralized applications |
| Mainnet's network ID is 1 | Testnet have network IDs of 3,4, and 42 |
| Example - Ethereum Mainnet | Example - Rinkeby Test network |

---
![What is Metamask?](https://www.youtube.com/watch?v=ts3mIcfnD9s&list=PLgPmWS2dQHW9u6IXZq5t5GMQTpW7JL33i&index=6)

# What is Metamask?
- Store Ether
- Send Ether
- Receive Ether
- Run Dapps
- Swap Tokens

---
![What is Rinkeby Faucet](https://www.youtube.com/watch?v=f9AbCK6PwmM&list=PLgPmWS2dQHW9u6IXZq5t5GMQTpW7JL33i&index=7)

# What is Rinkeby Faucet?
- ETH on testnets has no real valuel; therefore we get testnet ETH from faucets. Example- Rinkeby faucet, Ropsten faucet etc.
- https://faucet.rinkeby.io

--- 
![Contract Deployment Environment](https://www.youtube.com/watch?v=hi1BjWLFrSM&list=PLgPmWS2dQHW9u6IXZq5t5GMQTpW7JL33i&index=8)

# Contract Deployment Environment
## Javascript Virtual Machine
- Transaction will be executed in a sandbox
- Own memory blockchain
- Ideal for testing

## Injected Web3
- Deploy a contract or run a transaction on Ethereum main or test net.

## Web3 Provider
- Connect to a remote node and Ethereum client

---