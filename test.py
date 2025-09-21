from bitcoinrpc.authproxy import AuthServiceProxy

p = AuthServiceProxy("http://%s:%s@127.0.0.1:8332"%('yldjw', 'mushroom3'))

blockhash = p.getbestblockhash()
print("Block hash: ", blockhash)
block = p.getblock(blockhash)
transactions = block['tx']
block_value = 0
for txid in transactions:
    tx_value = 0
    tx = p.getrawtransaction(txid, True ,blockhash)
    for output in tx['vout']:
        tx_value += output['value']
    block_value += tx_value
print("Total block value: ", block_value)
