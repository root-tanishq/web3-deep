# **Cast Cheatsheet**

### **General Format**

bash

Copy code

`cast [command] [options/arguments]`

---

### **1. Sending Transactions**

#### **Send ETH**

bash

Copy code

`cast send <ADDRESS> --value <AMOUNT> [--from <ADDRESS>] [--gas <GAS_LIMIT>] [--gas-price <GAS_PRICE>] [--rpc-url <RPC_URL>]`

- **Description:** Sends ETH to a specified address.
- **Arguments:**
    - `<ADDRESS>`: The recipient's Ethereum address.
    - `--value`: The amount of ETH to send (in wei).
    - `--from`: The sender's Ethereum address (optional).
    - `--gas`: Gas limit (optional).
    - `--gas-price`: Gas price in wei (optional).
    - `--rpc-url`: Custom RPC endpoint (optional).
- **Example:**
    
    bash
    
    Copy code
    
    `cast send 0xRecipientAddress --value 1000000000000000000 --from 0xSenderAddress`
    
- **Response:**
    
    yaml
    
    Copy code
    
    `Transaction sent: 0xTxHash`
    

---

### **2. Query Blockchain Data**

#### **Get ETH Balance**

bash

Copy code

`cast balance <ADDRESS> [--rpc-url <RPC_URL>]`

- **Description:** Retrieves the ETH balance of a specified address.
- **Arguments:**
    - `<ADDRESS>`: The Ethereum address to query.
    - `--rpc-url`: Custom RPC endpoint (optional).
- **Example:**
    
    bash
    
    Copy code
    
    `cast balance 0xYourAddress`
    
- **Response:**
    
    Copy code
    
    `1.23456789 ETH`
    

#### **Get Block Number**

bash

Copy code

`cast block-number [--rpc-url <RPC_URL>]`

- **Description:** Retrieves the latest block number.
- **Example:**
    
    bash
    
    Copy code
    
    `cast block-number`
    
- **Response:**
    
    Copy code
    
    `12345678`
    

#### **Get Storage Slot**

bash

Copy code

`cast storage <CONTRACT_ADDRESS> <SLOT_INDEX> [--rpc-url <RPC_URL>]`

- **Description:** Fetches raw storage data at a specific slot in a contract.
- **Arguments:**
    - `<CONTRACT_ADDRESS>`: Address of the smart contract.
    - `<SLOT_INDEX>`: Index of the storage slot (in hex or decimal).
- **Example:**
    
    bash
    
    Copy code
    
    `cast storage 0xContractAddress 0x0`
    
- **Response:**
    
    Copy code
    
    `0xStorageData`
    

---

### **3. Decoding Data**

#### **Decode ABI-Encoded Data**

bash

Copy code

`cast abi-decode <FUNCTION_SIGNATURE> <ENCODED_DATA>`

- **Description:** Decodes ABI-encoded data into human-readable format.
- **Arguments:**
    - `<FUNCTION_SIGNATURE>`: Function signature (e.g., `transfer(address,uint256)`).
    - `<ENCODED_DATA>`: Encoded data string.
- **Example:**
    
    bash
    
    Copy code
    
    `cast abi-decode "transfer(address,uint256)" 0xa9059cbb0000000000000000000000000xRecipient0000000000000000000000000000001`
    
- **Response:**
    
    json
    
    Copy code
    
    `{   "recipient": "0xRecipient",   "amount": 1 }`
    

#### **Decode Event Logs**

bash

Copy code

`cast abi-decode-log <EVENT_SIGNATURE> <LOG_DATA>`

- **Description:** Decodes event logs into readable fields.
- **Arguments:**
    - `<EVENT_SIGNATURE>`: Event signature (e.g., `Transfer(address,address,uint256)`).
    - `<LOG_DATA>`: Raw log data.
- **Example:**
    
    bash
    
    Copy code
    
    `cast abi-decode-log "Transfer(address,address,uint256)" 0xLogData`
    
- **Response:**
    
    css
    
    Copy code
    
    `{   "from": "0xSender",   "to": "0xRecipient",   "value": 100 }`
    

---

### **4. Encoding Data**

#### **Encode Function Call**

bash

Copy code

`cast abi-encode <FUNCTION_SIGNATURE> [ARGUMENTS...]`

- **Description:** Encodes a function call for a smart contract.
- **Arguments:**
    - `<FUNCTION_SIGNATURE>`: Function signature (e.g., `transfer(address,uint256)`).
    - `[ARGUMENTS...]`: Function arguments.
- **Example:**
    
    bash
    
    Copy code
    
    `cast abi-encode "transfer(address,uint256)" 0xRecipient 100`
    
- **Response:**
    
    Copy code
    
    `0xa9059cbb0000000000000000000000000xRecipient0000000000000000000000000000001`
    

---

### **5. Query Contract State**

#### **Call a Function**

bash

Copy code

`cast call <CONTRACT_ADDRESS> <FUNCTION_SIGNATURE> [--rpc-url <RPC_URL>] [ARGUMENTS...]`

- **Description:** Calls a contract's function as a "read" operation.
- **Arguments:**
    - `<CONTRACT_ADDRESS>`: Address of the contract.
    - `<FUNCTION_SIGNATURE>`: Function signature (e.g., `balanceOf(address)`).
    - `[ARGUMENTS...]`: Function arguments.
- **Example:**
    
    bash
    
    Copy code
    
    `cast call 0xContractAddress "balanceOf(address)" 0xYourAddress`
    
- **Response:**
    
    Copy code
    
    `1000000000000000000`
    

---

### **6. Conversion Utilities**

#### **Convert ETH to WEI**

bash

Copy code

`cast to-wei <AMOUNT> <UNIT>`

- **Description:** Converts a value from ETH to wei.
- **Arguments:**
    - `<AMOUNT>`: Amount to convert.
    - `<UNIT>`: Unit of the amount (e.g., `eth`, `gwei`, etc.).
- **Example:**
    
    bash
    
    Copy code
    
    `cast to-wei 1 eth`
    
- **Response:**
    
    Copy code
    
    `1000000000000000000`
    

#### **Convert WEI to ETH**

bash

Copy code

`cast from-wei <AMOUNT> <UNIT>`

- **Description:** Converts a value from wei to a specified unit.
- **Arguments:**
    - `<AMOUNT>`: Amount in wei.
    - `<UNIT>`: Target unit (e.g., `eth`, `gwei`, etc.).
- **Example:**
    
    bash
    
    Copy code
    
    `cast from-wei 1000000000000000000 eth`
    
- **Response:**
    
    Copy code
    
    `1`
    

---

### **7. Utility Commands**

#### **Fetch Chain ID**

bash

Copy code

`cast chain-id [--rpc-url <RPC_URL>]`

- **Description:** Retrieves the chain ID of the current network.
- **Example:**
    
    bash
    
    Copy code
    
    `cast chain-id`
    
- **Response:**
    
    Copy code
    
    `1`
    

#### **Fetch ENS Name**

bash

Copy code

`cast resolve-name <ENS_NAME> [--rpc-url <RPC_URL>]`

- **Description:** Resolves an ENS name to an Ethereum address.
- **Arguments:**
    - `<ENS_NAME>`: ENS name (e.g., `vitalik.eth`).
- **Example:**
    
    bash
    
    Copy code
    
    `cast resolve-name vitalik.eth`
    
- **Response:**
    
    Copy code
    
    `0xAbc123...`
    

---

### **8. Advanced Features**

#### **Deploy a Contract**

bash

Copy code

`cast send --create <BYTECODE> [--from <ADDRESS>] [--gas <GAS_LIMIT>] [--rpc-url <RPC_URL>]`

- **Description:** Deploys a smart contract using bytecode.
- **Arguments:**
    - `<BYTECODE>`: Compiled contract bytecode.
- **Example:**
    
    bash
    
    Copy code
    
    `cast send --create 0xContractBytecode --from 0xDeployerAddress`
    
- **Response:**
    
    yaml
    
    Copy code
    
    `Contract deployed at: 0xContractAddress`
    

#### **Estimate Gas**

bash

Copy code

`cast estimate <CONTRACT_ADDRESS> <FUNCTION_SIGNATURE> [ARGUMENTS...]`

- **Description:** Estimates the gas cost of a contract call.
- **Arguments:**
    - `<CONTRACT_ADDRESS>`: Contract address.
    - `<FUNCTION_SIGNATURE>`: Function signature.
    - `[ARGUMENTS...]`: Arguments for the function.
- **Example:**
    
    bash
    
    Copy code
    
    `cast estimate 0xContractAddress "transfer(address,uint256)" 0xRecipient 100`
    
- **Response:**
    
    yaml
    
    Copy code
    
    `Gas estimate: 21000`
    

---

This cheatsheet should help you explore and make full use of Foundry's `cast` utility for Web3 development. Let me know if you'd like any additional details!