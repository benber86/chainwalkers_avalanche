from datetime import datetime
from parsing.utils.decimals import hex_to_decimal
from pprint import pprint


class BlockSchema(object):

    def __init__(self, data):
        self.difficulty = hex_to_decimal(data['difficulty'])
        self.extra_data = data['extraData']
        self.gas_limit = hex_to_decimal(data['gasLimit'])
        self.gas_used = hex_to_decimal(data['gasUsed'])
        self.hash = data['hash']
        self.logs_bloom = data['logsBloom']
        self.miner = data['miner']
        self.mix_hash = data['mixHash']
        self.nonce = data['nonce']
        self.number = hex_to_decimal(data['number'])
        self.parent_hash = data['parentHash']
        self.receipts_root = data['receiptsRoot']
        self.sha3_uncles = data['sha3Uncles']
        self.size = hex_to_decimal(data['size'])
        self.state_root = data['stateRoot']
        self.timestamp = hex_to_decimal(data['timestamp'])
        self.total_difficulty = hex_to_decimal(data['totalDifficulty'])
        self.transactions = []
        self.transactions_root = data['transactionsRoot']
        self.uncles = data['uncles']

        self.blockHeight = hex_to_decimal(data['number'])
        self.blockTime = hex_to_decimal(data['timestamp'])

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def get_transactions(self):
        return self.transactions

    def __repr__(self):
        header = "block height: %d, tx count %d" % (self.blockHeight, len(self.transactions))
        transactions = []
        for tx in self.transactions:
            transactions.append(str(tx))
        return "\n".join([header] + transactions)


class TransactionSchema(object):

    def __init__(self, data):
        self.block_hash = data['blockHash']
        self.block_number = hex_to_decimal(data['blockNumber'])
        self.from_ = data['from']
        self.gas = hex_to_decimal(data['gas'])
        self.gas_price = hex_to_decimal(data['gasPrice'])
        self.hash = data['hash']
        self.input = data['input']
        self.nonce = data['nonce']
        self.to = data['to']
        self.transaction_index = hex_to_decimal(data['transactionIndex'])
        self.value = hex_to_decimal(data['value'])
        self.r = data['r']
        self.s = data['s']
        self.v = data['v']

    def __repr__(self):
        return "tx: {}".format(self.hash)
