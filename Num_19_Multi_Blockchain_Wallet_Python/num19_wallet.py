# PART I: HD-Wallet-Derive
import subprocess
import json
import os
from pathlib import Path
from dotenv  import load_dotenv

# py file stores coin names
from constants import *

# check current path
# !pwd

# load Mnemonic:
load_dotenv(dotenv_path = Path("C:/Users/Leon/API_keys/.env"))
mnemonic = os.getenv('MNEMONIC')

# function to call hd-wallet-derive:
def derive_wallets(coin_name):
    '''
    input name of the coin:
    ie.
    BTC = 'btc'
    ETH = 'eth'
    BTCTEST = 'btc-test'
    return three child sets of address, public key and private key etc.
    '''
    
    command = f'php hd-wallet-derive/derive -g \
    --mnemonic="{mnemonic}" \
    --coin={coin_name}  --numderive=3 --cols=address,index,path,privkey,pubkey,pubkeyhash,xprv,xpub \
    --format=json'

    # open subprocess to run command:
    p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    output, err = p.communicate()
    p_status = p.wait()
    
    # output and sort in order:
    keys = json.loads(output)
    
    return keys

# Creating an object to hold result for each coin:
coins = {}
coins['btc-test']=derive_wallets(BTCTEST)
coins['eth']=derive_wallets(ETH)

# Pretty Print Result:
import pprint
pprint.pprint(coins)





# PART II: Bitcoin Transaction Function:
import bit
from bit import wif_to_key
from eth_account import Account
from web3 import Web3
from web3.middleware import geth_poa_middleware

w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)

def priv_key_to_account(coin, priv_key):
    '''
    this will convert the **privkey string** in a child key to an **account object**
    that bit or web3.py can use to transact.
    This function needs the following parameters:
    1) coin -- the coin type (defined in constants.py).
    2) priv_key -- the privkey string will be passed through here.
    '''
    if coin == ETH:
        '''
        This function returns an account object from the private key string.
        '''
        account = Account.privateKeyToAccount(priv_key)
    elif coin == BTCTEST:
        '''
        This is a function from the bit libarary that converts the private key string into 
        a WIF (Wallet Import Format) object. 
        WIF is a special format bitcoin uses to designate the types of keys it generates.
        '''
        account = bit.PrivateKeyTestnet(priv_key)
    return account



def create_tx(coin, account, to, amount):
    '''
    this will create the raw, unsigned transaction that contains all metadata needed to transact.
    This function needs the following parameters:
    1) coin -- the coin type (defined in constants.py).
    2) account -- the account object from priv_key_to_account.
    3) to -- the recipient address.
    4) amount -- the amount of the coin to send.
    
    '''
    if coin == ETH:
        gasEstimate = w3.eth.estimateGas(
        {"from": account.address, "to": to, "value": amount}
        )
        return {
            'chainId': w3.eth.chain_id,
            "from": account.address,
            "to": to,
            "value": amount,
            "gasPrice": w3.eth.gasPrice,
            "gas": gasEstimate,
            "nonce": w3.eth.getTransactionCount(account.address),       
            }
    
    elif coin == BTCTEST:
        return bit.PrivateKeyTestnet.prepare_transaction(account.address, [(to, amount, BTC)])


    
def send_tx(coin, account, to, amount):
    '''
    this will call create_tx, sign the transaction, then send it to the designated network.
    This function needs the following parameters:
    1) coin -- the coin type (defined in constants.py).
    2) account -- the account object from priv_key_to_account.
    3) to -- the recipient address.
    4) amount -- the amount of the coin to send.
    '''
    if coin == ETH:
        tx = create_tx(coin, account, to, amount)
        signed_tx = account.sign_transaction(tx)      
        result = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
        # Return Transaction ID
        print(result.hex())
        return result.hex()
    
    elif coin == BTCTEST:
        tx = create_tx(coin, account, to, amount)
        signed = account.sign_transaction(tx)
        return bit.network.NetworkAPI.broadcast_tx_testnet(signed)
    
    