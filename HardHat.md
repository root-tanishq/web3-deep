# HardHat 
- Hardhat is a robust development framework tailored for Ethereum smart contract development, equipped with comprehensive testing, debugging, and deployment features, facilitating efficient and streamlined blockchain development workflows for Solidity projects.
- In simple words:- It runs a local blockchain and provide some other utility along with it.
- Its more efficient then truffle
- migration is easy in hardhat rather than truffle
- RESOURCE - https://www.youtube.com/watch?v=6SYsy1ZlOPo&t=1496s
- RESOURCE - https://ethereum-waffle.readthedocs.io/en/latest/
# 0: Installation and ready to go setup
- requires nodejs and npm `sudo apt install nodejs npm -y`
```
$ mkdir <Project Name>; cd <Project Name>
$ npm init --yes
$ npm install --save-dev hardhat @nomicfoundation/hardhat-toolbox
$ npm install chai
```

## Initializing the project with hardhat
```
tanishq@pwnbox:~/Documents/WEB3/Learning-hardhat$ npx hardhat init
888    888                      888 888               888
888    888                      888 888               888
888    888                      888 888               888
8888888888  8888b.  888d888 .d88888 88888b.   8888b.  888888
888    888     "88b 888P"  d88" 888 888 "88b     "88b 888
888    888 .d888888 888    888  888 888  888 .d888888 888
888    888 888  888 888    Y88b 888 888  888 888  888 Y88b.
888    888 "Y888888 888     "Y88888 888  888 "Y888888  "Y888

Welcome to Hardhat v2.22.1

✔ What do you want to do? · Create a JavaScript project
✔ Hardhat project root: · /home/tanishq/Documents/WEB3/Learning-hardhat
✔ Do you want to add a .gitignore? (Y/n) · n

Project created

See the README.md file for some example tasks you can run

Give Hardhat a star on Github if you're enjoying it!

     https://github.com/NomicFoundation/hardhat

```

## Running node of the local blockchain of hardhat
- `npx hardhat node` 
```
Documents/WEB3/Learning-hardhat is 📦 v1.0.0 via  v20.11.1 
❯ npx hardhat node
Started HTTP and WebSocket JSON-RPC server at http://127.0.0.1:8545/

Accounts
========

WARNING: These accounts, and their private keys, are publicly known.
Any funds sent to them on Mainnet or any other live network WILL BE LOST.

Account #0: 0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266 (10000 ETH)
Private Key: 0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80

Account #1: 0x70997970C51812dc3A010C7d01b50e0d17dc79C8 (10000 ETH)
Private Key: 0x59c6995e998f97a5a0044966f0945389dc9e86dae88c7a8412f4603b6b78690d
...

WARNING: These accounts, and their private keys, are publicly known.
Any funds sent to them on Mainnet or any other live network WILL BE LOST.
```

---
# 1: Creating and testing an hardhat project, Invoking tokens
- `contracts/Wallet.sol`
```sol
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

contract Wallet {
    address public owner;
    string public name="Test Token";
    string public symbol="TT";
    mapping(address=>uint) public balances;
    uint public totalSupply=10000;

    constructor() {
        balances[msg.sender] = totalSupply;
        owner = msg.sender;
    }

    function transfer(address _to, uint _amt) public {
        require(balances[msg.sender] > _amt, "not enough amount");
        balances[msg.sender] -= _amt;
        balances[_to] += _amt;
    }

    function balanceOf(address _addr) public view returns (uint) {
        return balances[_addr];
    }

    

}
```
- for compiling the project `npx hardhat compile`
- OUTPUT OF THE UPPER COMMAND
```
tanishq@pwnbox:~/Documents/WEB3/Learning-hardhat$ npx hardhat compile
Downloading compiler 0.8.24
Compiled 2 Solidity files successfully (evm target: paris).
```
- `test/Wallet.js`
```js
const { expect } = require("chai");
const { ethers } = require("hardhat");

describe("Wallet Contract",function() { // describing the working of this function
    it("Wallet contract a simple contract with collecting and transfering money",async function() { // Test case1
        const [owner] = await ethers.getSigners(); // getting all the signer account from blockchain
        console.log("Signers Object:- ", owner);
        const wallet = await ethers.getContractFactory("Wallet"); // fetching the contract from contracts 

        const WalletContract = await wallet.deploy(); // deploying the contract
        const ownersBalance = await WalletContract.balanceOf(owner.address); // fetching the balance of owner using balanceOf function from Wallet.sol
        console.log("Owners Address ", owner.address);
        expect(await WalletContract.totalSupply()).to.equal(ownersBalance); // running an check that the owner have all the tokens of Wallet.sol
    });
});
```
- For test running the project `npx hardhat test`
- OUTPUT OF THE UPPER COMMAND
```
tanishq@pwnbox:~/Documents/WEB3/Learning-hardhat$ npx hardhat test


  Lock
    Deployment
      ✔ Should set the right unlockTime (691ms)
      ✔ Should set the right owner
      ✔ Should receive and store the funds to lock
      ✔ Should fail if the unlockTime is not in the future
    Withdrawals
      Validations
        ✔ Should revert with the right error if called too soon
        ✔ Should revert with the right error if called from another account
        ✔ Shouldn't fail if the unlockTime has arrived and the owner calls it
      Events
        ✔ Should emit an event on withdrawals
      Transfers
        ✔ Should transfer the funds to the owner

  Wallet Contract
Signers Object:-  HardhatEthersSigner {
  _gasLimit: 30000000,
  address: '0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266',
  provider: HardhatEthersProvider {
    _hardhatProvider: LazyInitializationProviderAdapter {
      _providerFactory: [AsyncFunction (anonymous)],
      _emitter: [EventEmitter],
      _initializingPromise: [Promise],
      provider: [BackwardsCompatibilityProviderAdapter]
    },
    _networkName: 'hardhat',
    _blockListeners: [],
    _transactionHashListeners: Map(0) {},
    _eventListeners: []
  }
}
Owners Address  0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266
    ✔ Wallet contract a simple contract with collecting and transfering money


  10 passing (809ms)

```
---
# 2: Running multiple test, connecting to other accounts, transfering tokens
- `test/Wallet.js`
```js
const { expect } = require("chai");
const { ethers } = require("hardhat");

describe("Wallet Contract",function() { // describing the working of this function
    it("Wallet contract a simple contract with collecting and transfering money",async function() { // Test case1
        const [owner] = await ethers.getSigners(); // getting all the signer account from blockchain
        const wallet = await ethers.getContractFactory("Wallet"); // fetching the contract from contracts 
        const WalletContract = await wallet.deploy(); // deploying the contract
        const ownersBalance = await WalletContract.balanceOf(owner.address); // fetching the balance of owner using balanceOf function from Wallet.sol
        expect(await WalletContract.totalSupply()).to.equal(ownersBalance); // running an check that the owner have all the tokens of Wallet.sol
    });

	// Previous test changes doesn't affect this test case
    it("Checking Transfer and connecting with different accounts", async function () { // Test case2
        const [owner,addr1,addr2] = await ethers.getSigners(); // getting 3 accounts from blockchain
        const Wallet = await ethers.getContractFactory("Wallet"); // fetching the contract from contracts
        const walletContract = await Wallet.deploy();
        // Transfering tokens from owner to addr1 - sending 50 tokens from owner -> addr1
        await walletContract.transfer(addr1.address,50);
        expect(await walletContract.balanceOf(addr1.address)).to.equal(50);
        // Transfering tokens from addr1 to add2 - sending 10 tokens from addr1 -> addr2
        await walletContract.connect(addr1).transfer(addr2.address,10);
        expect(await walletContract.balanceOf(addr2.address)).to.equal(10);
    });
});
```
- OUTPUT
```
Documents/WEB3/Learning-hardhat is 📦 v1.0.0 via  v20.11.1 
❯ npx hardhat test


  Lock
    Deployment
      ✔ Should set the right unlockTime (751ms)
      ✔ Should set the right owner
      ✔ Should receive and store the funds to lock
      ✔ Should fail if the unlockTime is not in the future
    Withdrawals
      Validations
        ✔ Should revert with the right error if called too soon
        ✔ Should revert with the right error if called from another account
        ✔ Shouldn't fail if the unlockTime has arrived and the owner calls it
      Events
        ✔ Should emit an event on withdrawals
      Transfers
        ✔ Should transfer the funds to the owner

  Wallet Contract
    ✔ Wallet contract a simple contract with collecting and transfering money
    ✔ Checking Transfer and connecting with different accounts


  11 passing (886ms)

```
---
# 3: Using mocha for testing, DRY coding 
- `test/Wallet.js`
```js
const { expect } = require("chai");
const { ethers } = require("hardhat");

describe("Token contract",function() {
    
    let owner;
    let addr1;
    let addr2;
    let tokenContract;
    let deployedTokenContract;
    beforeEach(async function() { // This function is called before every test cases from mocha framework
        [owner,addr1,addr2, ...addrs] = await ethers.getSigners();
        tokenContract = await ethers.getContractFactory("Wallet");
        deployedTokenContract = await tokenContract.deploy();
    });

    describe("Deployment", async function() {
        it("Checking if the owner is the owner of the contract", async function () {
            expect(await deployedTokenContract.owner()).to.equal(owner.address);
        });
        it("Checking if the owner received all the tokens", async function() {
            const ownersBalance = await deployedTokenContract.balanceOf(owner.address);
            expect(await deployedTokenContract.totalSupply()).to.equal(ownersBalance);    
        });
    });

    describe("Transactions",async function() {
        it("Checking the transfer of token", async function() {
            // owners -> addr1
            await deployedTokenContract.transfer(addr1.address,50);
            expect(await deployedTokenContract.balanceOf(addr1.address)).to.equal(50);

            // addr1 -> addr2
            await deployedTokenContract.connect(addr1).transfer(addr2.address,5);
            expect(await deployedTokenContract.balanceOf(addr2.address)).to.equal(5);
        });

        it("Checking if the transaction fails if token requirement is failed", async function() {
            // addr1 -> owner
            // on the deploy of contract only owner have all the tokens of the smart contract
            const initialBalance = await deployedTokenContract.balanceOf(owner.address);
            await expect(deployedTokenContract.connect(addr1).transfer(owner.address,1)).to.be.revertedWith("not enough amount");
            expect(await deployedTokenContract.balanceOf(owner.address)).to.equal(initialBalance);
            
        });

        it("Checking the updation of balance on transfering tokens", async function () {
            // Initial owner amount of tokens 
            const initialAmountOfTokens = await deployedTokenContract.balanceOf(owner.address);
            // owner -> addr1
            await deployedTokenContract.transfer(addr1.address,10);
            // owner -> addr2
            await deployedTokenContract.transfer(addr2.address,15);
            // checking the updation of values in the owners balance
            expect(await deployedTokenContract.balanceOf(owner.address)).to.equal(initialAmountOfTokens-BigInt(10 + 15));
            expect(await deployedTokenContract.balanceOf(addr1.address)).to.equal(10);
            expect(await deployedTokenContract.balanceOf(addr2.address)).to.equal(15);
        });
    });
});
```
- OUTPUT
```
Documents/WEB3/Learning-hardhat is 📦 v1.0.0 via  v20.11.1 
❯ npx hardhat test


  Lock
    Deployment
      ✔ Should set the right unlockTime (719ms)
      ✔ Should set the right owner
      ✔ Should receive and store the funds to lock
      ✔ Should fail if the unlockTime is not in the future
    Withdrawals
      Validations
        ✔ Should revert with the right error if called too soon
        ✔ Should revert with the right error if called from another account
        ✔ Shouldn't fail if the unlockTime has arrived and the owner calls it
      Events
        ✔ Should emit an event on withdrawals
      Transfers
        ✔ Should transfer the funds to the owner

  Token contract
    Deployment
      ✔ Checking if the owner is the owner of the contract
      ✔ Checking if the owner received all the tokens
    Transactions
      ✔ Checking the transfer of token
      ✔ Checking if the transaction fails if token requirement is failed
      ✔ Checking the updation of balance on transfering tokens


  14 passing (907ms)
```
---
# 4: Debugging using `console.sol`
- `contracts/Wallet.sol`
```sol
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

import "hardhat/console.sol"; // A library which will allow us to use console features of javascript for debugging
contract Wallet {
    address public owner;
    string public name="Test Token";
    string public symbol="TT";
    mapping(address=>uint) public balances;
    uint public totalSupply=10000;

    constructor() {
        balances[msg.sender] = totalSupply;
        owner = msg.sender;
    }

    function transfer(address _to, uint _amt) public {
        // Debugging code
        console.log("[SOL LOG]>> Current balance of the sender : %s", balances[msg.sender]);
        console.log("[SOL LOG]>> %s amount of tokens is transfered to %s",_amt,_to);
        require(balances[msg.sender] > _amt, "not enough amount");
        balances[msg.sender] -= _amt;
        balances[_to] += _amt;
    }

    function balanceOf(address _addr) public view returns (uint) {
        return balances[_addr];
    }

}
```
- OUTPUT
```
Documents/WEB3/Learning-hardhat is 📦 v1.0.0 via  v20.11.1 
❯ npx hardhat test
Compiled 2 Solidity files successfully (evm target: paris).


  Lock
    Deployment
      ✔ Should set the right unlockTime (1238ms)
      ✔ Should set the right owner
      ✔ Should receive and store the funds to lock
      ✔ Should fail if the unlockTime is not in the future
    Withdrawals
      Validations
        ✔ Should revert with the right error if called too soon
        ✔ Should revert with the right error if called from another account
        ✔ Shouldn't fail if the unlockTime has arrived and the owner calls it
      Events
        ✔ Should emit an event on withdrawals
      Transfers
        ✔ Should transfer the funds to the owner

  Token contract
    Deployment
      ✔ Checking if the owner is the owner of the contract
      ✔ Checking if the owner received all the tokens
    Transactions
[SOL LOG]>> Current balance of the sender : 10000
[SOL LOG]>> 50 amount of tokens is transfered to 0x70997970c51812dc3a010c7d01b50e0d17dc79c8
[SOL LOG]>> Current balance of the sender : 50
[SOL LOG]>> 5 amount of tokens is transfered to 0x3c44cdddb6a900fa2b585dd299e03d12fa4293bc
      ✔ Checking the transfer of token
[SOL LOG]>> Current balance of the sender : 0
[SOL LOG]>> 1 amount of tokens is transfered to 0xf39fd6e51aad88f6f4ce6ab8827279cfffb92266
      ✔ Checking if the transaction fails if token requirement is failed
[SOL LOG]>> Current balance of the sender : 10000
[SOL LOG]>> 10 amount of tokens is transfered to 0x70997970c51812dc3a010c7d01b50e0d17dc79c8
[SOL LOG]>> Current balance of the sender : 9990
[SOL LOG]>> 15 amount of tokens is transfered to 0x3c44cdddb6a900fa2b585dd299e03d12fa4293bc
      ✔ Checking the updation of balance on transfering tokens


  14 passing (1s)
```
---
# 5: Deployment to testnet/mainnet
- `scripts/deploy.js`
```js
const hre = require("hardhat");

async function main() {
    const [owner] = await hre.ethers.getSigners();
    const walletContract = await hre.ethers.getContractFactory("Wallet");
    const deployedWalletContract = await walletContract.deploy();
    await deployedWalletContract.waitForDeployment();
    console.log("Contract Address:", await deployedWalletContract.getAddress());
}

main()
    .then(() => process.exit(0))
    .catch((error) => {
        console.error(error);
        process.exit(1);
    });

```
- run the code using `npx hardhat run scripts/deploy.js`
- OUTPUT
```
Documents/WEB3/Learning-hardhat is 📦 v1.0.0 via  v20.11.1 
❯ npx hardhat run scripts/deploy.js
Contract Address: 0x5FbDB2315678afecb367f032d93F642f64180aa3
```
## Deploying to testnet / mainnet
- `hardhat.config.js`
```js
require("@nomicfoundation/hardhat-toolbox");

/** @type import('hardhat/config').HardhatUserConfig */
const ALCHEMY_API_KEY="";
const ROPSTEN_PRIVATE_KEY="";
module.exports = {
  solidity: "0.8.24",
  networks:{
    ropsten: {
      url:`https://eth-ropsten.alchemyapi.io/v2/${ALCHEMY_API_KEY}`,
      accounts: [`0x${ROPSTEN_PRIVATE_KEY}`],
    }
  }
};

```
- run the code using `npx hardhat run scripts/deploy.js --network ropsten`
---
# 6: creating an upgradable smart contract
- https://www.youtube.com/watch?v=uqzM_KAMvEw
- https://www.quicknode.com/guides/ethereum-development/smart-contracts/how-to-create-and-deploy-an-upgradeable-smart-contract-using-openzeppelin-and-hardhat
- https://www.npmjs.com/package/@openzeppelin/hardhat-upgrades
- We use `hardhat-upgrades` package to do it
#### INSTALLATION
```
npm install --save-dev @openzeppelin/hardhat-upgrades
npm install --save-dev @nomicfoundation/hardhat-ethers ethers # peer dependencies
```
- upgrading from `Count1.sol` to `Count2.sol`
#### `Count1.sol`
```sol
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

contract Counter {
    uint256 public count;

    function inc() public {
        count++;
    }

    function get() public view returns (uint256) {
        return count;
    }

    function set(uint _amt) public {
        count = _amt;
    }

}
```

#### `deploy-counterV1.js`
```js
const { ethers, upgrades } = require("hardhat");

async function main() {
  const COUNTERV1 = await ethers.getContractFactory("Counter");
  const counterv1 = await upgrades.deployProxy(COUNTERV1, [1], {
    initializer: "set",
 });
  await counterv1.waitForDeployment();
  console.log("Counter deployed to:", await counterv1.getAddress());
}

main();
```

#### `COMMAND TO RUN`
```
npx hardhat run scripts/deploy-counterV1.js --network <NETWORK NAME>
```

## Upgradation Process starts here
#### `Count2.sol`
```sol
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

contract Counter2 {
    uint256 public count;

    function inc() public {
        count++;
    }

    function get() public view returns (uint256) {
        return count;
    }

    function set(uint _amt) public {
        count = _amt;
    }

    function dec() public {
        count--;
    }

}
```
#### `deploy-counterV2.js`
```js
const { ethers, upgrades } = require("hardhat");

async function main() {
    const COUNTERV1 = await ethers.getContractFactory("Counter2");
    await upgrades.upgradeProxy("0xe7f1725E7734CE288F8367e1Bb143E90bb3F0512", COUNTERV1); // ProxyAdmin address - address which was earlier used for interaction with Counter contract
    console.log("Contract Upgraded");
}

main();
```

#### `COMMAND TO RUN`
```
npx hardhat run scripts/deploy-counterV2.js --network <NETWORK NAME>
```
---
