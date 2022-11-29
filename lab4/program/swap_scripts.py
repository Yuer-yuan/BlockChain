from bitcoin.core.script import *


######################################################################
# This function will be used by Alice and Bob to send their respective
# coins to a utxo that is redeemable either of two cases:
# 1) Recipient provides x such that hash(x) = hash of secret 
#    and recipient signs the transaction.
# 2) Sender and recipient both sign transaction
# 
# TODO: Fill this in to create a script that is redeemable by both
#       of the above conditions.
# 
# See this page for opcode: https://en.bitcoin.it/wiki/Script
#
#

# This is the ScriptPubKey for the swap transaction
def coinExchangeScript(public_key_sender, public_key_recipient, hash_of_secret):
    return [
        OP_DUP,                 # 复制栈顶元素
        OP_HASH160,             # 对栈顶元素进行hash160
        hash_of_secret,         # 将秘密的哈希压入栈顶
        OP_EQUAL,               # 比较是与秘密相等
        OP_IF,                  # 如果为秘密
        OP_DROP,                # 弹出栈顶多余的元素
        public_key_recipient,	# 接将收款方公钥压栈，验证收款方的签名
        OP_ELSE,                # 否则，验证是否为返还交易
        public_key_sender,      # 将付款方的公钥压入栈顶 
        OP_ENDIF,               # 结束分支判断
        OP_CHECKSIG             # 验证签名
    ]


# This is the ScriptSig that the receiver will use to redeem coins
def coinExchangeScriptSig1(sig_recipient, secret):
    return [
        sig_recipient, 
        secret
    ]


# This is the ScriptSig for sending coins back to the sender if unredeemed
def coinExchangeScriptSig2(sig_sender, sig_recipient):
    return [
        sig_sender
    ]

#
#
######################################################################
