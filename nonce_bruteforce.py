import rlp
from eth_utils import keccak, to_checksum_address

def calculate_contract_address(deployer_address, nonce):
    """
    Calculate the address of a contract deployed by `deployer_address` with a given `nonce`.
    """
    # RLP encode [deployer_address, nonce]
    encoded = rlp.encode([bytes.fromhex(deployer_address[2:]), nonce])
    # Compute the keccak256 hash and take the last 20 bytes
    contract_address = keccak(encoded)[12:]
    # Convert to a checksum address
    return to_checksum_address(contract_address)

def bruteforce_nonce(deployer_address, target_address, max_nonce=1000000):
    """
    Brute-force the nonce to match the target contract address.
    """
    target_address = target_address.lower()  # Normalize the target address
    for nonce in range(max_nonce):
        # Calculate the contract address for the current nonce
        calculated_address = calculate_contract_address(deployer_address, nonce)
        if calculated_address.lower() == target_address:
            return nonce
    return None

if __name__ == "__main__":
    # Replace with your values
    deployer_address = "0xaDb67e10Fa330db49e98201B4c5F19356CfA3f59"  # Address of the deployer
    target_address = "0xFC31cde4aCbF2b1d2996a2C7f695E850918e4007"  # Target contract address you want to match

    # Brute force to find the nonce
    print(f"Bruteforcing nonce for deployer {deployer_address} to match target address {target_address}...")
    nonce = bruteforce_nonce(deployer_address, target_address)
    
    if nonce is not None:
        print(f"Nonce found! The contract address {target_address} will be created at nonce {nonce}.")
    else:
        print(f"No nonce found to match the target address {target_address} within the specified range.")