# Foundry
![](../attachments/Pasted%20image%2020240327234207.png)
## What is foundry?
Foundry is a smart contract development toolchain.
Foundry manages your dependencies, compiles your project, runs tests, deploys, and lets you interact with the chain from the command-line and via Solidity scripts.
- https://book.getfoundry.sh/
- https://github.com/foundry-rs/foundry
- https://github.com/t4sk/hello-foundry
- SERIES USED TO LEARN [Foundry Playlist](https://www.youtube.com/playlist?list=PLO5VPQH6OWdUrKEWPF07CSuVm3T99DQki)
- BETTER COURSE https://updraft.cyfrin.io/courses/foundry
# Installing Foundry
- not properly available for windows
- for Linux and Mac
```sh
curl -L https://foundry.paradigm.xyz | bash
```
- Aften installing the utility run `foundryup` to complete the installation process

## Setupping foundry for a project
- Run the below command on a non empty directory 
```
forge init
```

## Building and Testing default project
- All the contracts will be in `src` directory and all the test for the contracts will be in `test` directory
- By default foundry provides a basic counter contract and along with it a test contract for the counter contract as shown below
- ![](../attachments/Pasted%20image%2020240327224913.png)
### Building the contract
- to build the contract use `forge build`
- OUTPUT
```
t@vm:~/Documents/Learning-Foundry$ forge build
[⠊] Compiling...
[⠒] Installing Solc version 0.8.25
[⠆] Successfully installed Solc 0.8.25
[⠆] Compiling 27 files with 0.8.25
[⠔] Solc 0.8.25 finished in 2.07s
Compiler run successful!
```
### Running the tests
- by default it will run all the tests in `test` directory
- to run test use `forge test`
- OUTPUT
```
t@vm:~/Documents/Learning-Foundry$ forge test
[⠒] Compiling...
No files changed, compilation skipped
Ran 2 tests for test/Counter.t.sol:CounterTest
[PASS] testFuzz_SetNumber(uint256) (runs: 256, μ: 30532, ~: 31310)
[PASS] test_Increment() (gas: 31325)
Suite result: ok. 2 passed; 0 failed; 0 skipped; finished in 20.00ms (19.60ms CPU time)
Ran 1 test suite in 20.89ms (20.00ms CPU time): 2 tests passed, 0 failed, 0 skipped (2 total tests)
```
#### More switches
- Verbosity `-v`
	- verbosity can be increased by increasing the `v` in the command like `-v,-vv,-vvv,-vvvv,-vvvvv` for details check `--help`
- Running specific script `--match-path`
	- By default `forge test` runs all the tests but a specific test can be specified like the command below
```
forge test --match-path test/HelloWorld.t.sol
[⠒] Compiling...
No files changed, compilation skipped

Ran 1 test for test/HelloWorld.t.sol:HelloWorldTest
[PASS] testgreet() (gas: 12336)
Suite result: ok. 1 passed; 0 failed; 0 skipped; finished in 854.38µs (174.47µs CPU time)

Ran 1 test suite in 7.13ms (854.38µs CPU time): 1 tests passed, 0 failed, 0 skipped (1 total tests)
```
- Gas Report `--gas-report`
	- Provides the gas report of gas used during running tests
```
forge test --match-path test/Counter.t.sol --gas-report
[⠒] Compiling...
No files changed, compilation skipped

Ran 4 tests for test/Counter.t.sol:CounterTest
[PASS] testDec() (gas: 106028)
[PASS] testFaildec() (gas: 28656)
[PASS] testdecUnderflow() (gas: 32048)
[PASS] testinc() (gas: 52380)
Suite result: ok. 4 passed; 0 failed; 0 skipped; finished in 1.72ms (545.93µs CPU time)
| src/Counter.sol:Counter contract |                 |       |        |       |         |
|----------------------------------|-----------------|-------|--------|-------|---------|
| Deployment Cost                  | Deployment Size |       |        |       |         |
| 108663                           | 287             |       |        |       |         |
| Function Name                    | min             | avg   | median | max   | # calls |
| count                            | 261             | 261   | 261    | 261   | 2       |
| dec                              | 23415           | 24381 | 23415  | 26313 | 3       |
| inc                              | 26294           | 37694 | 43394  | 43394 | 3       |




Ran 1 test suite in 3.67ms (1.72ms CPU time): 4 tests passed, 0 failed, 0 skipped (4 total tests)
```
---
# Creating a `test` contract for a contract
- Basic contract on which the `test` will be created
- `HelloWold.sol`
```sol
// SPDX-License-Indntifier: MIT
pragma solidity ^0.8.13;

contract HelloWorld {
    string public greet = "Hello World!";
}
```
- In order to create a test file a naming convention is followed where the filename is appended with `.t.sol`
- Importing foundry testing library with the below code
```sol
import {Test, console} from "forge-std/Test.sol";
import {HelloWorld} from "../src/HelloWorld.sol";
```
- All the functions must be `public` or `external`
- `setUp` function is created to setup the contract such as initialization and setuping other values and parameters required by the contract which need to be tested.
- then other test functions are return below following it
- All the test functions should start with name `test` following other name the user wants.
- All functions run stand alone other than `setUp` . The `setUp` functions run before other functions so all the tests will have fresh contract.
- `HelloWorld.t.sol`
```
// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;

import {Test, console} from "forge-std/Test.sol";
import {HelloWorld} from "../src/HelloWorld.sol";

contract HelloWorldTest is Test {
    HelloWorld public hw;

    function setUp() public {
        hw = new HelloWorld();
    }

    function testgreet() public view {
        assertEq(hw.greet(), "Hello World!");
    }
}

```

## Running test contract
```
t@vm:~/Documents/Learning-Foundry$ forge test
[⠒] Compiling...
[⠒] Compiling 1 files with 0.8.25
[⠑] Solc 0.8.25 finished in 1.86s
Compiler run successful!

Ran 1 test for test/HelloWorld.t.sol:HelloWorldTest
[PASS] testgreet() (gas: 12336)
Suite result: ok. 1 passed; 0 failed; 0 skipped; finished in 468.89µs (114.47µs CPU time)

Ran 2 tests for test/Counter.t.sol:CounterTest
[PASS] testFuzz_SetNumber(uint256) (runs: 256, μ: 30843, ~: 31310)
[PASS] test_Increment() (gas: 31325)
Suite result: ok. 2 passed; 0 failed; 0 skipped; finished in 19.59ms (19.20ms CPU time)

Ran 2 test suites in 23.56ms (20.06ms CPU time): 3 tests passed, 0 failed, 0 skipped (3 total tests)
```

---

# Checking test fails
- Many times a function is required to fail to work properly or for security purposes
- to test it use `testFail` keyword in the name of `test function`
- such as below 
```sol
 function testFaildec() public {
        // Any function with keyword Fail will check if the function failed or not if failed it will pass the test
        // In short we provide a condition which needs to be fail for contract.
        // setUp function is run before every test so every test has the fresh contract to test for
        counter.dec();
    }
```
- We can also use `vm` options to check for the errors without specifying the `Fail` keyword in function name
- such as below
```sol
    function testdecUnderflow() public {
        // upper function but with specifying what to expect
        vm.expectRevert(stdError.arithmeticError);
        counter.dec();
    }
```
- OUTPUT 
```
forge test --match-path test/Counter.t.sol
[⠒] Compiling...
[⠃] Compiling 1 files with 0.8.25
[⠊] Solc 0.8.25 finished in 1.88s
Compiler run successful!

Ran 4 tests for test/Counter.t.sol:CounterTest
[PASS] testDec() (gas: 33236)
[PASS] testFaildec() (gas: 7592)
[PASS] testdecUnderflow() (gas: 10984)
[PASS] testinc() (gas: 31316)
Suite result: ok. 4 passed; 0 failed; 0 skipped; finished in 2.81ms (432.10µs CPU time)

Ran 1 test suite in 4.25ms (2.81ms CPU time): 4 tests passed, 0 failed, 0 skipped (4 total tests)
```

---
# Specifying solidity version
- foundry will use the specified version to compile all the contracts
- `foundry.toml`
```
[profile.default]
src = "src"
out = "out"
libs = ["lib"]
solc_version = "0.8.24"
optimizer = true
optimizer_runs = 200

# See more config options https://github.com/foundry-rs/foundry/blob/master/crates/config/README.md#all-options
```

---
# Remappings
- Installing, Listing, Updating, Removing modules in foundry.
- If forge commands have any `git` issue then create a commit `git add . ;git commit -m 'save'`
```
forge install rari-capital/solmate                 --> Will install solmate library in lib/
forge remappings                                   --> Listing all the modules installed in foundry
forge update lib/solmate/                          --> Will update already existing library
forge remove solmate                               --> Will remove the library
```
- for Installing openzepplin contract a remapping file is created (more like using an alias name to point to an specific directory)
```
npm i @openzeppelin/contracts
```
- Create a `remappings.txt` file in the foundry directory
- `remappings.txt`
```
@openzeppelin/=node_modules/@openzeppelin
```
- Test contract
```sol
// SPDX-License-Identifier: MIT
pragma solidity 0.8.24;

import "@openzeppelin/contracts/access/Ownable.sol";

contract TestOz is Ownable(msg.sender) {}
```
---
# Auto Format code
- It format the code (pretty)
```
forge fmt
```
---
# Console Logging
- `forge-std/console.sol` can be used for logging data from a contract or a test contract.
- to use the above library we need to import it `import "forge-std/console.sol";`
- NOTE: This library should be removed during deployment as this library is only used for testing purposes only.
```sol
// SPDX-License-Identifier: UNLICENSED
pragma solidity 0.8.24;

import "forge-std/Test.sol";
import "forge-std/console.sol";
import {Counter} from "../src/Counter.sol";

contract CounterTest is Test {
    Counter public counter;

    function setUp() public {
        counter = new Counter();
    }

    function testinc() public {
        console.log("Some value here", 123);                        --> Code starts here
        int x = -1;
        console.logInt(x);
        counter.inc();
        assertEq(counter.count(), 1);
    }
...
```
- double or higher verbosity is required to print the output of logs `-vv`
- OUTPUT
```
forge test --match-path test/Counter.t.sol -vv
[⠊] Compiling...
[⠃] Compiling 1 files with 0.8.24
[⠊] Solc 0.8.24 finished in 1.76s
Compiler run successful!

Ran 4 tests for test/Counter.t.sol:CounterTest
[PASS] testDec() (gas: 33236)
[PASS] testFaildec() (gas: 7592)
[PASS] testdecUnderflow() (gas: 10984)
[PASS] testinc() (gas: 34864)
Logs:
  Some value here 123
  -1

Suite result: ok. 4 passed; 0 failed; 0 skipped; finished in 1.32ms (616.31µs CPU time)

Ran 1 test suite in 5.13ms (1.32ms CPU time): 4 tests passed, 0 failed, 0 skipped (4 total tests)

```
---
# Checking Authentication
- `vm.prank` changes the `msg.sender` for the next call only
- `vm.startPrank` and `vm.stopPrank` can be used to change `msg.sender` for desired amount of calls
- `Wallet.sol`
```sol
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

contract Wallet {
    address payable public owner;

    constructor() {
        owner = payable(msg.sender);
    }

    // Function to receive ether
    receive() payable external { }

    // Function to change owner
    function setOwner(address _newOwner) external {
        require(owner == msg.sender, "not owner");
        owner = payable(_newOwner);        
    }

    // Function to withdraw 
    function withdraw() external {
        require(owner == msg.sender,"not owner");
        payable(msg.sender).transfer(address(this).balance);
    }

    // Function to check balance
    function chkBalance() external view returns(uint) {
        return address(this).balance;
    }
}
```
- `Wallet.t.sol`
```sol
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

import "forge-std/Test.sol";
import {Wallet} from "../src/Wallet.sol";

contract WalletTest is Test {
    Wallet public wallet;

    function setUp() public {
        wallet = new Wallet();
    }

    // An function to check whether the Owner is getting changed properly
    function testchkOwner() public {
        wallet.setOwner(address(1));
        assertEq(wallet.owner(), address(1));
    }

    // An Function to test if the owner is different to fail
    function testFailchkOwner() public {
        vm.prank(address(1)); // It changes the msg.sender for the next call
        wallet.setOwner(address(1));
    }

    function testFailchkOwner2() public {
        wallet.setOwner(address(1));
        vm.startPrank(address(1)); // for all the next calls the msg.sender will be address(1) till its stopped
        wallet.setOwner(address(1));
        wallet.setOwner(address(1));
        wallet.setOwner(address(1));
        vm.stopPrank();

        // function will fail here
        wallet.setOwner(address(1));
    }
}
```
- OUTPUT
```
forge test --match-path test/Wallet.t.sol -vvv
[⠒] Compiling...
No files changed, compilation skipped

Ran 3 tests for test/Wallet.t.sol:WalletTest
[PASS] testFailchkOwner() (gas: 10555)
[PASS] testFailchkOwner2() (gas: 18197)
[PASS] testchkOwner() (gas: 14522)
Suite result: ok. 3 passed; 0 failed; 0 skipped; finished in 1.80ms (627.47µs CPU time)

Ran 1 test suite in 4.75ms (1.80ms CPU time): 3 tests passed, 0 failed, 0 skipped (3 total tests)
```
---
# Errors in Foundry
- `Error.sol`
```sol
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

contract Errors {
    error CError();

    function BasicError() public pure {
        require(false, "not authorized");
    }

    function CustomError() public pure {
        revert CError();
    }
}
```
- `Error.t.sol`
```sol
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

import "forge-std/Test.sol";
import "../src/Error.sol";

contract testErrors is Test {
    Errors public err;

    function setUp() public {
        err = new Errors();
    }

    function testFailBasicError() public view {
        err.BasicError();
    }

    function testExpectRevert() public {
        vm.expectRevert();
        err.CustomError();
    }

    function testRequireMessage() public {
        vm.expectRevert(bytes("not authorized"));
        err.BasicError();
    }

    function testCustomError() public {
        vm.expectRevert(Errors.CError.selector);
        err.CustomError();
    }

    function testAssertionLabel() public pure {
        assertEq(uint(1), uint(1),"test 1");
        assertEq(uint(1), uint(1),"test 2");
        assertEq(uint(1), uint(1),"test 3");
        assertEq(uint(1), uint(1),"test 4");
        assertEq(uint(1), uint(1),"test 5");
    }
}
```
- OUTPUT
```
forge test --match-path test/Error.t.sol -vvv
[⠒] Compiling...
[⠑] Compiling 1 files with 0.8.24
[⠘] Solc 0.8.24 finished in 1.55s
Compiler run successful!

Ran 5 tests for test/Error.t.sol:testErrors
[PASS] testAssertionLabel() (gas: 6545)
[PASS] testCustomError() (gas: 8227)
[PASS] testExpectRevert() (gas: 8293)
[PASS] testFailBasicError() (gas: 5535)
[PASS] testRequireMessage() (gas: 8686)
Suite result: ok. 5 passed; 0 failed; 0 skipped; finished in 4.93ms (448.92µs CPU time)

Ran 1 test suite in 6.78ms (4.93ms CPU time): 5 tests passed, 0 failed, 0 skipped (5 total tests)

```
---
# Event
- `vm.exepectEmit` compares the function emit with the next emit call done.
- It requires 4 arguments -> `check Index 1, check Index 2, check Index 3,checkData`
- `Event.sol`
```sol
pragma solidity 0.8.24;

contract Event {
    event Transfer(address indexed from, address indexed to, uint256 amount);

    function transfer(address _from, address _to, uint256 _amount) public {
        emit Transfer(_from, _to, _amount);
    }

    function transferMany(address _from, address[] calldata _to, uint256[] calldata _amount) public {
        for (uint256 i = 0; i < _to.length; i++) {
            emit Transfer(_from, _to[i], _amount[i]);
        }
    }
}
```
- `Event.t.sol`
```sol
pragma solidity 0.8.24;

import "forge-std/Test.sol";
import {Event} from "../src/Event.sol";

contract TestEvent is Test{
    Event public e;

    event Transfer(address indexed from, address indexed to, uint amount);

    function setUp() public {
        e = new Event();
    }

    function testEmitTransferEvent() public {
        // function expectEmit(
        //     bool checkTopic1,
        //     bool checkTopic2,
        //     bool checkTopic3,
        //     bool checkData
        // ) external;

        // 1. Tell Foundry which data to check
        // Check index 1, index 2 and data
        vm.expectEmit(true, true, false, true);

        // 2. Emit the expected event
        emit Transfer(address(this),address(123),456);

        // 3. Call the function that should emit the event
        e.transfer(address(this),address(123),456);


        // Check only index 1
        vm.expectEmit(true, false, false, false);
        emit Transfer(address(this),address(123),345);
        e.transfer(address(this),address(567),879);
    }

    function testEmitManyTransferEvent() public {
        
        address[] memory to = new address[](2);
        uint[] memory amounts = new uint[](2);
        
        to[0] = address(123); 
        to[1] = address(456);

        amounts[0] = 777;
        amounts[0] = 999;

        for (uint i; i < to.length; i++ ){
            vm.expectEmit(true, true, false, true);
            emit Transfer(address(this), to[i], amounts[i]);
        }

        e.transferMany(address(this), to, amounts);        
    }
}
```
- OUTPUT
```
forge test --match-path test/Event.t.sol -vvv
[⠊] Compiling...
[⠒] Compiling 1 files with 0.8.24
[⠑] Solc 0.8.24 finished in 1.39s
Compiler run successful!

Ran 2 tests for test/Event.t.sol:TestEvent
[PASS] testEmitManyTransferEvent() (gas: 18903)
[PASS] testEmitTransferEvent() (gas: 17234)
Suite result: ok. 2 passed; 0 failed; 0 skipped; finished in 2.62ms (261.88µs CPU time)

Ran 1 test suite in 5.86ms (2.62ms CPU time): 2 tests passed, 0 failed, 0 skipped (2 total tests)

```
---
# Time
- `vm.warp` changes the time according to the argument
- `skip` skip the time to future -> increment time
- `rewind` take back time to past -> decrement time
- `vm.roll` changes the block number to desired number
- `Time.sol`
```sol
pragma solidity 0.8.24;

contract Auction {
    uint public startAt = block.timestamp + 1 days;
    uint public endAt = block.timestamp + 2 days;

    function bid() public view {
        require(block.timestamp >= startAt && block.timestamp < endAt, "cannot bid");
    } 

    function end() public view {
        require(block.timestamp > endAt, "auction ended");
    }
}
```
- `Time.t.sol`
```sol
pragma solidity 0.8.24;

import "forge-std/Test.sol";
import {Auction} from "../src/Time.sol";

contract TestTime is Test {
    Auction public auc;
    uint public startAt;

    function setUp() public {
        auc = new Auction();
        startAt = block.timestamp;
    }

    function testBidFailBeforeBidStarts() public {
        vm.expectRevert(bytes("cannot bid"));
        auc.bid();
    }

    function testBidAfterBidStarts() public {
        // vm.warp can shift block.timestamp time
        vm.warp(startAt + 1 days);
        auc.bid();
    }

    function testBidFailAfterAuction() public {
        vm.warp(startAt + 2 days);
        vm.expectRevert(bytes("auction ended"));
        auc.end();
    }

    function testSkipandRewind() public {
        uint t = block.timestamp;

        // skip increases the time
        skip(100);
        assertEq(block.timestamp,t + 100);

        // Rewind takes the time back
        rewind(10);
        assertEq(block.timestamp, t + 100 - 10);
    }

    function testRoll() public {
        // vm.roll changes the block number
        vm.roll(123);
        assertEq(block.number,123);
    }
}
```
- OUTPUT
```
forge test --match-path test/Time.t.sol -vvv
[⠒] Compiling...
[⠒] Compiling 1 files with 0.8.24
[⠑] Solc 0.8.24 finished in 1.49s
Compiler run successful!

Ran 5 tests for test/Time.t.sol:TestTime
[PASS] testBidAfterBidStarts() (gas: 14678)
[PASS] testBidFailAfterAuction() (gas: 13361)
[PASS] testBidFailBeforeBidStarts() (gas: 10810)
[PASS] testRoll() (gas: 3480)
[PASS] testSkipandRewind() (gas: 4699)
Suite result: ok. 5 passed; 0 failed; 0 skipped; finished in 1.55ms (435.85µs CPU time)

Ran 1 test suite in 4.61ms (1.55ms CPU time): 5 tests passed, 0 failed, 0 skipped (5 total tests)

```
---
# Sending Ether and control Ether
- `deal(address, uint)` --> Deal sets a specific amount of balance to a particular address
- `hoax(address, uint)` --> deal + prank , it changes the balance of the particular address as well it also call prank due to which the next call will have msg.sender as the address provided to hoax
- `Wallet.sol`
```sol
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

contract Wallet {
    address payable public owner;

    event Deploy(address sender, uint amount);

    constructor() {
        owner = payable(msg.sender);
    }

    // Function to receive ether
    receive() external payable {
        emit Deploy(msg.sender,msg.value);
    }

    // Function to change owner
    function setOwner(address _newOwner) external {
        require(owner == msg.sender, "not owner");
        owner = payable(_newOwner);
    }

    // Function to withdraw
    function withdraw() external {
        require(owner == msg.sender, "not owner");
        payable(msg.sender).transfer(address(this).balance);
    }

    // Function to check balance
    function chkBalance() external view returns (uint256) {
        return address(this).balance;
    }
}

```
- `TestWallet.t.sol`
```sol
pragma solidity 0.8.24;

import "forge-std/Test.sol";
import {Wallet} from "../src/Wallet.sol";

contract TestWallet is Test {
    Wallet public wallet;

    function setUp() public {
        wallet = new Wallet();
    }

    function _sendEth(uint amount) public {
        (bool ok,) = address(wallet).call{value: amount}("");
        require(ok,"call failed");
    }

    function testWalletTransferingEthersDeal() public {
        deal(address(1),123); // deal(address, uint) --> Deal sets a specific amount of balance to a particular address
        assertEq(address(1).balance,123);

        // Sending the amount from address(1) to the wallet contract
        vm.prank(address(1)); // sets the msg.sender to address(1) for the next call
        _sendEth(123);
        assertEq(address(wallet).balance,123);
    }

    function testWalletTransferingEthersHoax() public {
        hoax(address(1),123); // hoax(address, uint) --> deal + prank , it changes the balance of the particular address as well it also call prank due to which the next call will have msg.sender as the address provided to hoax
        _sendEth(123);
        assertEq(address(wallet).balance,123);
    }
}
```
---
# Signing a message 
- `Sign.t.sol`
```sol
pragma solidity 0.8.24;

import "forge-std/Test.sol";

contract Signer is Test {
    function testSigner() public pure {
        // Signing a message and checking
        uint privateKey = 342132;
        address publicKey = vm.addr(privateKey);
        bytes32 messageHash = keccak256("Secret Message");
        (uint8 v,bytes32 r, bytes32 s) = vm.sign(privateKey, messageHash);
        address signer = ecrecover(messageHash,v,r,s);
        assertEq(signer,publicKey);

        // Checking Invalid Hash
        bytes32 InvalidHash = keccak256("Invalid Message");
        address signerih = ecrecover(InvalidHash,v,r,s);
        assertTrue(signerih != signer);
    }
}
```
---
# Fuzzing inputs 
- `fuzz` - an random input will be provided by the foundry and test will be run
- `assume` -  If false, then fuzzer will discard the current fuzz inputs and start a new fuzz run
- `bound(input,min,max)` - bound input between min and max
- `runs` - no of times the test run
- `μ` - mean gas (Average)
- `~` - median gas
- `Bit.sol`
```sol
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

contract MostSignificantBitFunction {
    // Find most significant bit using binary search
    function mostSignificantBit(uint256 x)
        external
        pure
        returns (uint256 msb)
    {
        // x >= 2 ** 128
        if (x >= 0x100000000000000000000000000000000) {
            x >>= 128;
            msb += 128;
        }
        // x >= 2 ** 64
        if (x >= 0x10000000000000000) {
            x >>= 64;
            msb += 64;
        }
        // x >= 2 ** 32
        if (x >= 0x100000000) {
            x >>= 32;
            msb += 32;
        }
        // x >= 2 ** 16
        if (x >= 0x10000) {
            x >>= 16;
            msb += 16;
        }
        // x >= 2 ** 8
        if (x >= 0x100) {
            x >>= 8;
            msb += 8;
        }
        // x >= 2 ** 4
        if (x >= 0x10) {
            x >>= 4;
            msb += 4;
        }
        // x >= 2 ** 2
        if (x >= 0x4) {
            x >>= 2;
            msb += 2;
        }
        // x >= 2 ** 1
        if (x >= 0x2) msb += 1;
    }
}

```
- `Fuzz.t.sol`
```sol
pragma solidity 0.8.24;

import "forge-std/Test.sol";
import {MostSignificantBitFunction} from "../src/Bit.sol";


contract FuzzTest is Test {
    MostSignificantBitFunction public b;

    function setUp() public {
        b = new MostSignificantBitFunction();
    }

    function mostSignificantBit(uint x) private pure returns (uint) {
        uint i = 0;
        while ((x >>= 1) > 0) {
            i++;
        }
        return i;
    }

    function testSignificantBitFuzz(uint x) public view {
        // assume - If false, then fuzzer will discard the current fuzz inputs and start a new fuzz run
        // Skip x = 0
        // vm.assume(x > 0);
        // The value of the x will be always greater than 0

        // bound(input,min,max) - bound input between min and max
        uint x2 = bound(x,1,100);

        // FUZZ - an random input will be provided by the foundry and test will be run
        assertEq(b.mostSignificantBit(x2),mostSignificantBit(x2));
    }
}
```
- OUTPUT
```
forge test --match-path test/Fuzz.t.sol
[⠒] Compiling...
[⠒] Compiling 1 files with 0.8.24
[⠑] Solc 0.8.24 finished in 1.43s
Compiler run successful!

Ran 1 test for test/Fuzz.t.sol:FuzzTest
[PASS] testSignificantBitFuzz(uint256) (runs: 257, μ: 13337, ~: 13590)
Suite result: ok. 1 passed; 0 failed; 0 skipped; finished in 18.67ms (18.13ms CPU time)

Ran 1 test suite in 23.69ms (18.67ms CPU time): 1 tests passed, 0 failed, 0 skipped (1 total tests)

```
---
# Invariant in Foundry
- Invariants are conditions expressions that should always hold true over the course of a fuzzing campaign. A good invariant testing suite should have as many invariants as possible, and can have different testing suites for different protocol states.
- The testing function name should starts with keyword `invariant`
- `runs` -> The times the function run
- `calls` -> How many calls were done
- `reverts` -> How many calls were failed
-  https://book.getfoundry.sh/forge/invariant-testing
- `invariant_0.t.sol` --> Falling invariant testing
```sol
pragma solidity 0.8.24;

// Falling invariant testing
// This testing should fail as one of the function will change the value of flag.
contract IntroInvariant {
    bool public flag; 

    function func_1() public {}
    function func_2() public {}
    function func_3() public {}
    function func_4() public {}
    function func_5() public {
        flag = true;
    }
}

import "forge-std/Test.sol";

contract IntroInvariantTesting is Test {
    IntroInvariant public target;

    function setUp() public {
        target = new IntroInvariant();
    }

    function invariant_flag_should_always_false() public view {
        assertEq(target.flag(),false);
    }
}
```
- OUTPUT
```
forge test --match-path test/invariant_0.t.sol -vvvv
[⠒] Compiling...
No files changed, compilation skipped

Ran 1 test for test/invariant_0.t.sol:IntroInvariantTesting
[FAIL. Reason: assertion failed: true != false]
        [Sequence]
                sender=0x7FEAD9e9C4aE2cc5a1a71f40c390F8D4892316b2 addr=[test/invariant_0.t.sol:IntroInvariant]0x5615dEB798BB3E4dFa0139dFa1b3D433Cc23b72f calldata=func_5() args=[]
 invariant_flag_should_always_false() (runs: 256, calls: 3826, reverts: 0)
Traces:
  [77553] IntroInvariantTesting::setUp()
    ├─ [40093] → new IntroInvariant@0x5615dEB798BB3E4dFa0139dFa1b3D433Cc23b72f
    │   └─ ← [Return] 200 bytes of code
    └─ ← [Stop] 

  [22278] IntroInvariant::func_5()
    └─ ← [Stop] 

  [10538] IntroInvariantTesting::invariant_flag_should_always_false()
    ├─ [2364] IntroInvariant::flag() [staticcall]
    │   └─ ← [Return] true
    ├─ [0] VM::assertEq(true, false) [staticcall]
    │   └─ ← [Revert] assertion failed: true != false
    └─ ← [Revert] assertion failed: true != false

Suite result: FAILED. 0 passed; 1 failed; 0 skipped; finished in 302.98ms (300.00ms CPU time)

Ran 1 test suite in 1.74s (302.98ms CPU time): 0 tests passed, 1 failed, 0 skipped (1 total tests)

Failing tests:
Encountered 1 failing test in test/invariant_0.t.sol:IntroInvariantTesting
[FAIL. Reason: assertion failed: true != false]
        [Sequence]
                sender=0x7FEAD9e9C4aE2cc5a1a71f40c390F8D4892316b2 addr=[test/invariant_0.t.sol:IntroInvariant]0x5615dEB798BB3E4dFa0139dFa1b3D433Cc23b72f calldata=func_5() args=[]
 invariant_flag_should_always_false() (runs: 256, calls: 3826, reverts: 0)

Encountered a total of 1 failing tests, 0 tests succeeded

```
## Invariant Handlers
- Test functions under specific conditions
- `targetContract` --> Define a specific contract only that contract functions will be tested
- `targetSelector` --> Defines an array of functions only which need to be tested
- `invariant_2.t.sol`
```sol
// SPDX-License-Identifier: MIT
pragma solidity 0.8.24;

import "forge-std/Test.sol";
import "forge-std/console.sol";
import {WETH} from "../src/WETH.sol";

// Topics
// - handler based testing - test functions under specific conditions
// - target contract
// - target selector

import {CommonBase} from "forge-std/Base.sol";
import {StdCheats} from "forge-std/StdCheats.sol";
import {StdUtils} from "forge-std/StdUtils.sol";

contract Handler is CommonBase, StdCheats, StdUtils {
    WETH private weth;
    uint256 public wethBalance;
    uint256 public numCalls;

    constructor(WETH _weth) {
        weth = _weth;
    }

    receive() external payable {}

    function sendToFallback(uint256 amount) public {
        amount = bound(amount, 0, address(this).balance);
        wethBalance += amount;
        numCalls += 1;

        (bool ok,) = address(weth).call{value: amount}("");
        require(ok, "sendToFallback failed");
    }

    function deposit(uint256 amount) public {
        amount = bound(amount, 0, address(this).balance);
        wethBalance += amount;
        numCalls += 1;

        weth.deposit{value: amount}();
    }

    function withdraw(uint256 amount) public {
        amount = bound(amount, 0, weth.balanceOf(address(this)));
        wethBalance -= amount;
        numCalls += 1;

        weth.withdraw(amount);
    }

    function fail() external {
        revert("fail");
    }
}

contract WETH_Handler_Based_Invariant_Tests is Test {
    WETH public weth;
    Handler public handler;

    function setUp() public {
        weth = new WETH();
        handler = new Handler(weth);

        // Send 100 ETH to handler
        deal(address(handler), 100 * 1e18);
        // Set fuzzer to only call the handler
        targetContract(address(handler));

        bytes4[] memory selectors = new bytes4[](3);
        selectors[0] = Handler.deposit.selector;
        selectors[1] = Handler.withdraw.selector;
        selectors[2] = Handler.sendToFallback.selector;

        // Handler.fail() not called
        targetSelector(
            FuzzSelector({addr: address(handler), selectors: selectors})
        );
    }

    function invariant_eth_balance() public {
        assertGe(address(weth).balance, handler.wethBalance());
        console.log("handler num calls", handler.numCalls());
    }
}
```
## Actor Manager
- Simulating multiple users
- https://www.youtube.com/watch?v=kPx4K8kRvUQ&list=PLO5VPQH6OWdUrKEWPF07CSuVm3T99DQki&index=19
```sol
// SPDX-License-Identifier: MIT
pragma solidity 0.8.24;

import "forge-std/Test.sol";
import "forge-std/console.sol";
import {WETH} from "../src/WETH.sol";
import {Handler} from "./invariant_2.t.sol";

// Topics
// - Actor management

import {CommonBase} from "forge-std/Base.sol";
import {StdCheats} from "forge-std/StdCheats.sol";
import {StdUtils} from "forge-std/StdUtils.sol";

contract ActorManager is CommonBase, StdCheats, StdUtils {
    Handler[] public handlers;

    constructor(Handler[] memory _handlers) {
        handlers = _handlers;
    }

    function sendToFallback(uint256 handlerIndex, uint256 amount) public {
        uint256 index = bound(handlerIndex, 0, handlers.length - 1);
        handlers[index].sendToFallback(amount);
    }

    function deposit(uint256 handlerIndex, uint256 amount) public {
        uint256 index = bound(handlerIndex, 0, handlers.length - 1);
        handlers[index].deposit(amount);
    }

    function withdraw(uint256 handlerIndex, uint256 amount) public {
        uint256 index = bound(handlerIndex, 0, handlers.length - 1);
        handlers[index].withdraw(amount);
    }
}

contract WETH_Multi_Handler_Invariant_Tests is Test {
    WETH public weth;
    ActorManager public manager;
    Handler[] public handlers;

    function setUp() public {
        weth = new WETH();

        for (uint256 i = 0; i < 3; i++) {
            handlers.push(new Handler(weth));
            // Send 100 ETH to handler
            deal(address(handlers[i]), 100 * 1e18);
        }

        manager = new ActorManager(handlers);

        targetContract(address(manager));
    }

    function invariant_eth_balance() public {
        uint256 total = 0;
        for (uint256 i = 0; i < handlers.length; i++) {
            total += handlers[i].wethBalance();
            console.log("Handler num calls", i, handlers[i].numCalls());
        }
        console.log("ETH total", total / 1e18);
        assertGe(address(weth).balance, total);
    }
}
```
---
# FFI (Foreign Function Interface)
-   FFI (Foreign Function Interface) in Foundry allows seamless integration of external libraries and code written in other programming languages, enabling interoperability within the Foundry platform. It facilitates leveraging functionalities and resources from various sources, expanding the capabilities and versatility of Foundry for developers.
- In simple terms you can execute commands.
- `FFI.t.sol`
```sol
pragma solidity 0.8.24;

import "forge-std/Test.sol";
import "forge-std/console.sol";

contract FFITest is Test {
    function testFFI() public {
        // running cat /etc/hostname
        string[] memory cmds = new string[](2);
        cmds[0] = "cat";
        cmds[1] = "/etc/hostname";
        bytes memory res = vm.ffi(cmds);
        console.log(string(res));
    }
}
```
- An special option is used to execute the `vm.ffi` -> `--ffi`
- OUTPUT
```
forge test --match-path test/FFI.t.sol --ffi -vvv
[⠒] Compiling...
[⠆] Compiling 1 files with 0.8.24
[⠰] Solc 0.8.24 finished in 1.46s
Compiler run successful!

Ran 1 test for test/FFI.t.sol:FFITest
[PASS] testFFI() (gas: 7951)
Logs:
  vm

Suite result: ok. 1 passed; 0 failed; 0 skipped; finished in 8.07ms (7.64ms CPU time)

Ran 1 test suite in 14.57ms (8.07ms CPU time): 1 tests passed, 0 failed, 0 skipped (1 total tests)

```
---
# Inspect -> List storage variables, functions, abi calls
- `forge inspect`
- listing storage variables
```
-> forge inspect src/WETH.sol:WETH storage --pretty
| Name      | Type                                            | Slot | Offset | Bytes | Contract          |
|-----------|-------------------------------------------------|------|--------|-------|-------------------|
| name      | string                                          | 0    | 0      | 32    | src/WETH.sol:WETH |
| symbol    | string                                          | 1    | 0      | 32    | src/WETH.sol:WETH |
| decimals  | uint8                                           | 2    | 0      | 1     | src/WETH.sol:WETH |
| balanceOf | mapping(address => uint256)                     | 3    | 0      | 32    | src/WETH.sol:WETH |
| allowance | mapping(address => mapping(address => uint256)) | 4    | 0      | 32    | src/WETH.sol:WETH |

```
- listing methods or functions inside the contract
```
-> forge inspect src/WETH.sol:WETH methods --pretty
{
  "allowance(address,address)": "dd62ed3e",
  "approve(address,uint256)": "095ea7b3",
  "balanceOf(address)": "70a08231",
  "decimals()": "313ce567",
  "deposit()": "d0e30db0",
  "name()": "06fdde03",
  "symbol()": "95d89b41",
  "totalSupply()": "18160ddd",
  "transfer(address,uint256)": "a9059cbb",
  "transferFrom(address,address,uint256)": "23b872dd",
  "withdraw(uint256)": "2e1a7d4d"
}

```
- listing abi calls
```
-> forge inspect src/WETH.sol:WETH abi --pretty
interface WETH {
    event Approval(address indexed src, address indexed guy, uint256 wad);
    event Deposit(address indexed dst, uint256 wad);
    event Transfer(address indexed src, address indexed dst, uint256 wad);
    event Withdrawal(address indexed src, uint256 wad);

    receive() external payable;

    function allowance(address, address) external view returns (uint256);
    function approve(address guy, uint256 wad) external returns (bool);
    function balanceOf(address) external view returns (uint256);
    function decimals() external view returns (uint8);
    function deposit() external payable;
    function name() external view returns (string memory);
    function symbol() external view returns (string memory);
    function totalSupply() external view returns (uint256);
    function transfer(address dst, uint256 wad) external returns (bool);
    function transferFrom(address src, address dst, uint256 wad) external returns (bool);
    function withdraw(uint256 wad) external;
}
```
---
# Cast 
- connecting wallet through command line
- IMPORTING WALLET `cast wallet import burner --private-key <PRIVATE KEY>`
- LISTING WALLET `cast wallet list`
- REMOVING WALLET `rm -rf ~/.foundry/keystores/burner`
- SENDING FUNCTION `cast send --account burner --rpc-url <RPC URL> <DEPLOY ADDRESS> <FUNCTION TO CALL> <FUNCTION ARGUMENTS>`
- CALLING FUNCTION `cast call --rpc-url <RPC URL> <DEPLOY ADDRESS> <FUNCTION WITH RETURN TYPE>`
