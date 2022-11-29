from bitcoin import SelectParams
from bitcoin.wallet import CBitcoinSecret, P2PKHBitcoinAddress
from bitcoin.core import x

SelectParams('testnet')

######################################################################
# 
# TODO: Fill this in with address secret key for BTC testnet3
#
# Create address in Base58 with keygen.py
# Send coins at https://coinfaucet.eu/en/btc-testnet/

# Only to be imported by alice.py
# Alice should have coins!!
alice_secret_key_BTC = CBitcoinSecret(
    'cSX3H7ZTGKSgBmWsuUSFtKobUDaKzMMXqzhzHeD98qpi1qM4rtUf')

# Only to be imported by bob.py
bob_secret_key_BTC = CBitcoinSecret(
    'cSoUGtb4DFNCZ5BRg3m4BWuv4U8tc19nW8V8Kwy73SWXnfjsR4Nc')

######################################################################
#
# TODO: Fill this in with address secret key for BCY testnet
#
# Create address in hex with
# curl -X POST https://api.blockcypher.com/v1/bcy/test/addrs?token=8acebf7dcf554bc2930bf01f1ec516f0
#
# Send coins with 
# curl -d '{"address": "C3Te5ctMDdNAbDyVUcDxWyNPqhrRKnoPJ3", "amount": 1000000}' https://api.blockcypher.com/v1/bcy/test/faucet?token=8acebf7dcf554bc2930bf01f1ec516f0

# Only to be imported by alice.py
alice_secret_key_BCY = CBitcoinSecret.from_secret_bytes(
    x('30d71b25d368dbe532c30063cc38d59e7f1f10fcafbc8c263e414072877d62b2'))

# Only to be imported by bob.py
# Bob should have coins!!
bob_secret_key_BCY = CBitcoinSecret.from_secret_bytes(
    x('6be882f8746c8ea3bbe9dc15d2c694fd8b75d433c6265dd70558e165849a7200'))

# Can be imported by alice.py or bob.py
alice_public_key_BTC = alice_secret_key_BTC.pub
alice_address_BTC = P2PKHBitcoinAddress.from_pubkey(alice_public_key_BTC)

bob_public_key_BTC = bob_secret_key_BTC.pub
bob_address_BTC = P2PKHBitcoinAddress.from_pubkey(bob_public_key_BTC)

alice_public_key_BCY = alice_secret_key_BCY.pub
alice_address_BCY = P2PKHBitcoinAddress.from_pubkey(alice_public_key_BCY)

bob_public_key_BCY = bob_secret_key_BCY.pub
bob_address_BCY = P2PKHBitcoinAddress.from_pubkey(bob_public_key_BCY)
