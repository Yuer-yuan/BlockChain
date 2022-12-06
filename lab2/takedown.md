- 使用keygen生成3个私钥
  ```
    Private key: cTWkmp93Mbc28ydnwjzYfwgQ1G9a46uCfAT31X7BprCVXpcM74iz
    Address: mrgkY1uyYdpJdvVuyVL6Wjt667dKNgsMvM
  
    Private key: cRB5ujRQ1TULCC5NSXyW7Xa4UtNfiggBJgFrKUfhwYo1eeZk9Jdk
    Address: mxgascCAefUmniA9rcJV88t5mKjMqW4nCX
  
    Private key: cTcDFCNqMsJyCnrzyzkjo6ppbgXuLUuYpUWbLD8cjM4o2TSMVv4C
    Address: mnBZhgatN9MczWW72dEkCHj5JFhgrwww5i
  ```

- 代码修改：

```python
from sys import exit
from bitcoin.core.script import *
from bitcoin.wallet import CBitcoinSecret

from utils import *
from config import my_private_key, my_public_key, my_address, faucet_address
from ex1 import send_from_P2PKH_transaction


cust1_private_key = CBitcoinSecret(
    'cTWkmp93Mbc28ydnwjzYfwgQ1G9a46uCfAT31X7BprCVXpcM74iz')
cust1_public_key = cust1_private_key.pub
cust2_private_key = CBitcoinSecret(
    'cRB5ujRQ1TULCC5NSXyW7Xa4UtNfiggBJgFrKUfhwYo1eeZk9Jdk')
cust2_public_key = cust2_private_key.pub
cust3_private_key = CBitcoinSecret(
    'cTcDFCNqMsJyCnrzyzkjo6ppbgXuLUuYpUWbLD8cjM4o2TSMVv4C')
cust3_public_key = cust3_private_key.pub


######################################################################
# TODO: Complete the scriptPubKey implementation for Exercise 2

# You can assume the role of the bank for the purposes of this problem
# and use my_public_key and my_private_key in lieu of bank_public_key and
# bank_private_key.

ex2a_txout_scriptPubKey = [OP_0, my_public_key, cust1_public_key, cust2_public_key, cust3_public_key, OP_4, OP_CHECKMULTISIGVERIFY, my_public_key, OP_CHECKSIG];
######################################################################

if __name__ == '__main__':
    ######################################################################
    # TODO: set these parameters correctly
    amount_to_send = 0.0012
    txid_to_spend = (
        'cc8fb122460f9f4cd88cd4f3b5f149c07421da36835e55dea30e8162b1e68be3')
    utxo_index = 4
    ######################################################################

    response = send_from_P2PKH_transaction(
        amount_to_send, txid_to_spend, utxo_index,
        ex2a_txout_scriptPubKey)
    print(response.status_code, response.reason)
    print(response.text)

```


  ```jso6f41fc168650349809be6e6ea7709c37a2d37f86431269ce07f6344dacf70001n
  (blockchain) bill@bill-Lenovo-V15-IWL:~/Desktop/blockchain/lab2/pro$ /home/bill/anaconda3/envs/blockchain/bin/python /home/bill/Desktop/blockchain/lab2/pro/ex2a.py
  /home/bill/anaconda3/envs/blockchain/bin/python /home/bill/Desktop/blockchain/lab2/pro/ex2a.py
  201 Created
  {
  "tx": {
    "block_height": -1,
    "block_index": -1,
    "hash": "6f41fc168650349809be6e6ea7709c37a2d37f86431269ce07f6344dacf70001",
    "addresses": [
      "mzLaAohp6ihFnuwQdQFFnm5zZ8jgh4UokJ"
    ],
    "total": 20000,
    "fees": 130000,
    "size": 306,
    "vsize": 306,
    "preference": "high",
    "relayed_by": "2001:250:401:6576:132b:9d8a:c663:5b4d",
    "received": "2022-10-18T03:56:51.856709571Z",
    "ver": 1,
    "double_spend": false,
    "vin_sz": 1,
    "vout_sz": 1,
    "confirmations": 0,
    "inputs": [
      {
        "prev_hash": "cc8fb122460f9f4cd88cd4f3b5f149c07421da36835e55dea30e8162b1e68be3",
        "output_index": 2,
        "script": "47304402200e5288f431fd54b91c9a277616a8ae88b7b8691d226545b004d54f68da49f88102204cf323dbff3084b12a533a5c4e2c97919172a7b00f6f8a9cc761314eb22a2e6c012102db5f0ae1ef53d76bd78a4254ae87cf293175c197bf6270744b7a8e1fa7966804",
        "output_value": 150000,
        "sequence": 4294967295,
        "addresses": [
          "mzLaAohp6ihFnuwQdQFFnm5zZ8jgh4UokJ"
        ],
        "script_type": "pay-to-pubkey-hash",
        "age": 2349299
      }
    ],
    "outputs": [
      {
        "value": 20000,
        "script": "002102057cd667d3e2c481687ef3abc347895c1f3763c53f282a254a1885063ae8b5e021034b0ff4bf574b90816fcda87daa4eaa2c295301fbbc3e9135c5e6e89326612df321021d12629a2fb116591bafb1256a73119f4705aa5c1f30505ff17eaa2847c5b7d353af2102db5f0ae1ef53d76bd78a4254ae87cf293175c197bf6270744b7a8e1fa7966804ac",
        "addresses": null,
        "script_type": "unknown"
      }
    ]
  }
  }
  ```

修改为4人均可以赎回

```
201 Created
{
  "tx": {
    "block_height": -1,
    "block_index": -1,
    "hash": "3c8b0a998b88b23361b3977437d58c98b1b816d757ebfadbb590496f81c4c6a5",
    "addresses": [
      "mzLaAohp6ihFnuwQdQFFnm5zZ8jgh4UokJ"
    ],
    "total": 20000,
    "fees": 130000,
    "size": 340,
    "vsize": 340,
    "preference": "high",
    "relayed_by": "2001:250:401:6576:132b:9d8a:c663:5b4d",
    "received": "2022-10-18T04:02:40.21229246Z",
    "ver": 1,
    "double_spend": false,
    "vin_sz": 1,
    "vout_sz": 1,
    "confirmations": 0,
    "inputs": [
      {
        "prev_hash": "cc8fb122460f9f4cd88cd4f3b5f149c07421da36835e55dea30e8162b1e68be3",
        "output_index": 3,
        "script": "47304402201ecb35ae024a1a3044089136fdc5340706baf924a85ce4ecc5d0f52eb0e05ee90220478cd27750d34311ff892477891220e11bc2d563537f3c0cd62e278c985adac4012102db5f0ae1ef53d76bd78a4254ae87cf293175c197bf6270744b7a8e1fa7966804",
        "output_value": 150000,
        "sequence": 4294967295,
        "addresses": [
          "mzLaAohp6ihFnuwQdQFFnm5zZ8jgh4UokJ"
        ],
        "script_type": "pay-to-pubkey-hash",
        "age": 2349299
      }
    ],
    "outputs": [
      {
        "value": 20000,
        "script": "002102db5f0ae1ef53d76bd78a4254ae87cf293175c197bf6270744b7a8e1fa79668042102057cd667d3e2c481687ef3abc347895c1f3763c53f282a254a1885063ae8b5e021034b0ff4bf574b90816fcda87daa4eaa2c295301fbbc3e9135c5e6e89326612df321021d12629a2fb116591bafb1256a73119f4705aa5c1f30505ff17eaa2847c5b7d354af2102db5f0ae1ef53d76bd78a4254ae87cf293175c197bf6270744b7a8e1fa7966804ac",
        "addresses": null,
        "script_type": "unknown"
      }
    ]
  }
}
```

```json
201 Created
{
  "tx": {
    "block_height": -1,
    "block_index": -1,
    "hash": "3ed6977fddfb1805212821c7d285110aebdfb9301deabef3bae7ccb95a6ba32e",
    "addresses": [
      "mzLaAohp6ihFnuwQdQFFnm5zZ8jgh4UokJ"
    ],
    "total": 119999,
    "fees": 30001,
    "size": 340,
    "vsize": 340,
    "preference": "medium",
    "relayed_by": "2001:250:401:6576:132b:9d8a:c663:5b4d",
    "received": "2022-10-18T04:04:06.566151Z",
    "ver": 1,
    "double_spend": false,
    "vin_sz": 1,
    "vout_sz": 1,
    "confirmations": 0,
    "inputs": [
      {
        "prev_hash": "cc8fb122460f9f4cd88cd4f3b5f149c07421da36835e55dea30e8162b1e68be3",
        "output_index": 4,
        "script": "47304402204b0b0d5cf859ec8c60779ae9d310f61c7e38d51e1fcabcbaef576d881ce413940220318abfdca6983666033be2ab808198344c2cb7a50d339108efbea390113be193012102db5f0ae1ef53d76bd78a4254ae87cf293175c197bf6270744b7a8e1fa7966804",
        "output_value": 150000,
        "sequence": 4294967295,
        "addresses": [
          "mzLaAohp6ihFnuwQdQFFnm5zZ8jgh4UokJ"
        ],
        "script_type": "pay-to-pubkey-hash",
        "age": 2349299
      }
    ],
    "outputs": [
      {
        "value": 119999,
        "script": "002102db5f0ae1ef53d76bd78a4254ae87cf293175c197bf6270744b7a8e1fa79668042102057cd667d3e2c481687ef3abc347895c1f3763c53f282a254a1885063ae8b5e021034b0ff4bf574b90816fcda87daa4eaa2c295301fbbc3e9135c5e6e89326612df321021d12629a2fb116591bafb1256a73119f4705aa5c1f30505ff17eaa2847c5b7d354af2102db5f0ae1ef53d76bd78a4254ae87cf293175c197bf6270744b7a8e1fa7966804ac",
        "addresses": null,
        "script_type": "unknown"
      }
    ]
  }
}
```

该交易的验证情况

![image-20221018122146275](report.assets/image-20221018122146275.png)

- 代码修改

```python
from sys import exit
from bitcoin.core.script import *

from utils import *
from config import my_private_key, my_public_key, my_address, faucet_address
from ex1 import P2PKH_scriptPubKey
from ex2a import (ex2a_txout_scriptPubKey, cust1_private_key, cust2_private_key,
                  cust3_private_key)


def multisig_scriptSig(txin, txout, txin_scriptPubKey):
    bank_sig = create_OP_CHECKSIG_signature(txin, txout, txin_scriptPubKey,
                                             my_private_key)
    cust1_sig = create_OP_CHECKSIG_signature(txin, txout, txin_scriptPubKey,
                                             cust1_private_key)
    cust2_sig = create_OP_CHECKSIG_signature(txin, txout, txin_scriptPubKey,
                                             cust2_private_key)
    cust3_sig = create_OP_CHECKSIG_signature(txin, txout, txin_scriptPubKey,
                                             cust3_private_key)
    ######################################################################
    # TODO: Complete this script to unlock the BTC that was locked in the
    # multisig transaction created in Exercise 2a.
    return [bank_sig, OP_0, bank_sig, cust1_sig]
    ######################################################################


def send_from_multisig_transaction(amount_to_send, txid_to_spend, utxo_index,
                                   txin_scriptPubKey, txout_scriptPubKey):
    txout = create_txout(amount_to_send, txout_scriptPubKey)

    txin = create_txin(txid_to_spend, utxo_index)
    txin_scriptSig = multisig_scriptSig(txin, txout, txin_scriptPubKey)

    new_tx = create_signed_transaction(txin, txout, txin_scriptPubKey,
                                       txin_scriptSig)

    return broadcast_transaction(new_tx)

if __name__ == '__main__':
    ######################################################################
    # TODO: set these parameters correctly
    amount_to_send = 0.0001
    txid_to_spend = '3ed6977fddfb1805212821c7d285110aebdfb9301deabef3bae7ccb95a6ba32e'
    utxo_index = 0
    ######################################################################

    txin_scriptPubKey = ex2a_txout_scriptPubKey
    txout_scriptPubKey = P2PKH_scriptPubKey(faucet_address)

    response = send_from_multisig_transaction(
        amount_to_send, txid_to_spend, utxo_index,
        txin_scriptPubKey, txout_scriptPubKey)
    print(response.status_code, response.reason)
    print(response.text)

```

- 运行结果

```json
201 Created
{
  "tx": {
    "block_height": -1,
    "block_index": -1,
    "hash": "372697da745e6fc3b5d34bd951a90c4dcd92c00e6a3a64728c37f5752f4c9c0c",
    "addresses": [
      "mv4rnyY3Su5gjcDNzbMLKBQkBicCtHUtFB"
    ],
    "total": 10000,
    "fees": 109999,
    "size": 303,
    "vsize": 303,
    "preference": "high",
    "relayed_by": "2001:250:401:6576:132b:9d8a:c663:5b4d",
    "received": "2022-10-18T04:31:57.18363448Z",
    "ver": 1,
    "double_spend": false,
    "vin_sz": 1,
    "vout_sz": 1,
    "confirmations": 0,
    "inputs": [
      {
        "prev_hash": "3ed6977fddfb1805212821c7d285110aebdfb9301deabef3bae7ccb95a6ba32e",
        "output_index": 0,
        "script": "47304402202ff4d33d92bfc98052da01a20e87bc570d35581f67aa46ebe211e67a0f9897ef022078c461b6586081931242bf822019fec94021bd997c05b816cd50f7e390baa610010047304402202ff4d33d92bfc98052da01a20e87bc570d35581f67aa46ebe211e67a0f9897ef022078c461b6586081931242bf822019fec94021bd997c05b816cd50f7e390baa61001483045022100d436d8270b3f3defd38f60a2a14fbc0028e7e9ae8a876c7f1607c452f04b1716022040184f3c4106fed07942a9252ac359b4f7c7fc1bce5ea12133678119adee9ea801",
        "output_value": 119999,
        "sequence": 4294967295,
        "script_type": "unknown",
        "age": 2377027
      }
    ],
    "outputs": [
      {
        "value": 10000,
        "script": "76a9149f9a7abd600c0caa03983a77c8c3df8e062cb2fa88ac",
        "addresses": [
          "mv4rnyY3Su5gjcDNzbMLKBQkBicCtHUtFB"
        ],
        "script_type": "pay-to-pubkey-hash"
      }
    ]
  }
}
```

- 网站截图



```
201 Created
{
  "tx": {
    "block_height": -1,
    "block_index": -1,
    "hash": "9dfe41ac8cda4059778ff009f13abda382937df15d1ced8603c1b4cde0ab2684",
    "addresses": [
      "mv4rnyY3Su5gjcDNzbMLKBQkBicCtHUtFB"
    ],
    "total": 10000,
    "fees": 10000,
    "size": 302,
    "vsize": 302,
    "preference": "low",
    "relayed_by": "2001:250:401:6571:a748:52d2:102b:d874",
    "received": "2022-10-18T06:05:29.847407667Z",
    "ver": 1,
    "double_spend": false,
    "vin_sz": 1,
    "vout_sz": 1,
    "confirmations": 0,
    "inputs": [
      {
        "prev_hash": "3c8b0a998b88b23361b3977437d58c98b1b816d757ebfadbb590496f81c4c6a5",
        "output_index": 0,
        "script": "4730440220270146dc75f491d6d3a79f76a76d3247db564b544062d371a76fa4d4660912df02200c63106891968df3a68a0ce8600faa04c73c5a19eb8e1bce27b9497df3f21ca401004730440220270146dc75f491d6d3a79f76a76d3247db564b544062d371a76fa4d4660912df02200c63106891968df3a68a0ce8600faa04c73c5a19eb8e1bce27b9497df3f21ca40147304402206903dcf7de8b71e2e07076531cf5d9a74d7d19ff6fc5964f18268eab9caa5dd30220251e8eca3723d341b99922d980a28361026a9a9dcb4c95b53aea9429f19ffb2701",
        "output_value": 20000,
        "sequence": 4294967295,
        "script_type": "unknown",
        "age": 2377026
      }
    ],
    "outputs": [
      {
        "value": 10000,
        "script": "76a9149f9a7abd600c0caa03983a77c8c3df8e062cb2fa88ac",
        "addresses": [
          "mv4rnyY3Su5gjcDNzbMLKBQkBicCtHUtFB"
        ],
        "script_type": "pay-to-pubkey-hash"
      }
    ]
  }
}
```

```
201 Created
{
  "tx": {
    "block_height": -1,
    "block_index": -1,
    "hash": "84b8b0c4e7a61401a3a271c9d3f84a3a34f4fd56864127291ad32985a99e8937",
    "addresses": [
      "mzLaAohp6ihFnuwQdQFFnm5zZ8jgh4UokJ"
    ],
    "total": 119999,
    "fees": 30001,
    "size": 340,
    "vsize": 340,
    "preference": "medium",
    "relayed_by": "2001:250:401:6561:47c2:d4cf:ce28:71be",
    "received": "2022-10-29T14:40:39.616307167Z",
    "ver": 1,
    "double_spend": false,
    "vin_sz": 1,
    "vout_sz": 1,
    "confirmations": 0,
    "inputs": [
      {
        "prev_hash": "cc8fb122460f9f4cd88cd4f3b5f149c07421da36835e55dea30e8162b1e68be3",
        "output_index": 5,
        "script": "47304402204cb3243d62054d28d8a0efd6909ed398b2cb02574c3178b4ca8eedb4f113e15602202ef3688a1df656972f06a3842fefc9e9f90721d58f439ded3d592cc57f56723e012102db5f0ae1ef53d76bd78a4254ae87cf293175c197bf6270744b7a8e1fa7966804",
        "output_value": 150000,
        "sequence": 4294967295,
        "addresses": [
          "mzLaAohp6ihFnuwQdQFFnm5zZ8jgh4UokJ"
        ],
        "script_type": "pay-to-pubkey-hash",
        "age": 2349299
      }
    ],
    "outputs": [
      {
        "value": 119999,
        "script": "002102db5f0ae1ef53d76bd78a4254ae87cf293175c197bf6270744b7a8e1fa79668042102057cd667d3e2c481687ef3abc347895c1f3763c53f282a254a1885063ae8b5e021034b0ff4bf574b90816fcda87daa4eaa2c295301fbbc3e9135c5e6e89326612df321021d12629a2fb116591bafb1256a73119f4705aa5c1f30505ff17eaa2847c5b7d354af2102db5f0ae1ef53d76bd78a4254ae87cf293175c197bf6270744b7a8e1fa7966804ac",
        "addresses": null,
        "script_type": "unknown"
      }
    ]
  }
}
```

```
201 Created
{
  "tx": {
    "block_height": -1,
    "block_index": -1,
    "hash": "d0fb40c73775f4d7a37434f18a41c15d62bf1ea7908f836bf8b368594f06e353",
    "addresses": [
      "mzLaAohp6ihFnuwQdQFFnm5zZ8jgh4UokJ"
    ],
    "total": 119999,
    "fees": 30001,
    "size": 340,
    "vsize": 340,
    "preference": "medium",
    "relayed_by": "2001:250:401:6561:47c2:d4cf:ce28:71be",
    "received": "2022-10-29T14:48:29.177391284Z",
    "ver": 1,
    "double_spend": false,
    "vin_sz": 1,
    "vout_sz": 1,
    "confirmations": 0,
    "inputs": [
      {
        "prev_hash": "cc8fb122460f9f4cd88cd4f3b5f149c07421da36835e55dea30e8162b1e68be3",
        "output_index": 6,
        "script": "473044022076a39f15e59e6a4f3f68ad440f5d7873ed04620fe468698b027abbf1787b15bb02203fc13fdcbb095a07e4f326e4baca2a30b9b2563638a611451645c1e4121aa090012102db5f0ae1ef53d76bd78a4254ae87cf293175c197bf6270744b7a8e1fa7966804",
        "output_value": 150000,
        "sequence": 4294967295,
        "addresses": [
          "mzLaAohp6ihFnuwQdQFFnm5zZ8jgh4UokJ"
        ],
        "script_type": "pay-to-pubkey-hash",
        "age": 2349299
      }
    ],
    "outputs": [
      {
        "value": 119999,
        "script": "522102db5f0ae1ef53d76bd78a4254ae87cf293175c197bf6270744b7a8e1fa79668042102057cd667d3e2c481687ef3abc347895c1f3763c53f282a254a1885063ae8b5e021034b0ff4bf574b90816fcda87daa4eaa2c295301fbbc3e9135c5e6e89326612df321021d12629a2fb116591bafb1256a73119f4705aa5c1f30505ff17eaa2847c5b7d354af2102db5f0ae1ef53d76bd78a4254ae87cf293175c197bf6270744b7a8e1fa7966804ac",
        "addresses": null,
        "script_type": "unknown"
      }
    ]
  }
}
```

```
201 Created
{
  "tx": {
    "block_height": -1,
    "block_index": -1,
    "hash": "7832832410d14e170fc2aa762282e7f4b228229869062e66193bd1c393811b4e",
    "addresses": [
      "mv4rnyY3Su5gjcDNzbMLKBQkBicCtHUtFB"
    ],
    "total": 100000,
    "fees": 19999,
    "size": 304,
    "vsize": 304,
    "preference": "medium",
    "relayed_by": "2001:250:401:6561:47c2:d4cf:ce28:71be",
    "received": "2022-10-29T15:56:15.625918082Z",
    "ver": 1,
    "double_spend": false,
    "vin_sz": 1,
    "vout_sz": 1,
    "confirmations": 0,
    "inputs": [
      {
        "prev_hash": "d0fb40c73775f4d7a37434f18a41c15d62bf1ea7908f836bf8b368594f06e353",
        "output_index": 0,
        "script": "4730440220537cc1265cbc2b9a2def5a09e573210277ba658ff20db9f94dfe3611c82e22ff02207d1d67bf2713b2f3b5cdc68a487d57b84fe6d2bdc867bcd307b279b4c51a4dd90100483045022100f2b42c4720f2b4c5c730411a2f4f3726a7f328cbc38b8beb62ed8d1c2e3dce4102200f69fbad7e0de0ebeace8a0e9557cb759d34181d1874fe63a8869af75fe3b67101483045022100f62dc1434c3213d8727873bc5374e0783f353730c1142b305538b1b6107c560f02206102544e43cffaa05d861aff92dfeb85b2ff744aaacab238d86f809a5c9e11d701",
        "output_value": 119999,
        "sequence": 4294967295,
        "script_type": "unknown",
        "age": 2378610
      }
    ],
    "outputs": [
      {
        "value": 100000,
        "script": "76a9149f9a7abd600c0caa03983a77c8c3df8e062cb2fa88ac",
        "addresses": [
          "mv4rnyY3Su5gjcDNzbMLKBQkBicCtHUtFB"
        ],
        "script_type": "pay-to-pubkey-hash"
      }
    ]
  }
}
```