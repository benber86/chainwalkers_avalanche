import argparse
import json
import sys
import os

BASE_DIR = (os.path.abspath(os.path.dirname(__file__))).replace("/parsing/scripts", '')
sys.path.append(BASE_DIR)

from parsing.config import NODE_URL
from parsing.node import Node


def main(block_heights):
    node = Node(NODE_URL)

    results = []
    for height in block_heights:
        block = node.get_block(height)
        block_data = {
            "difficulty": block.difficulty,
            "extra_data": block.extra_data,
            "gas_limit": block.gas_limit,
            "gas_used": block.gas_used,
            "hash": block.hash,
            "logs_bloom": block.logs_bloom,
            "mix_hash": block.mix_hash,
            "nonce": block.nonce,
            "number": block.number,
            "parent_hash": block.parent_hash,
            "sha3_uncles": block.sha3_uncles,
            "size": block.size,
            "state_root": block.state_root,
            "timestamp": block.timestamp,
            "total_difficulty": block.total_difficulty,
            "transactions": block.transactions,
            "transactions_root": block.transactions_root,
            "uncles": block.uncles,

            "blockHeight": block.blockHeight,
            "blockTime": block.blockTime
        }

        transactions = []
        for tx in block.get_transactions():
            transactions.append({
                "block_hash": tx.block_hash,
                "block_number": tx.block_number,
                "from": tx.from_,
                "gas": tx.gas,
                "gas_price": tx.gas_price,
                "hash": tx.hash,
                "input": tx.input,
                "nonce": tx.nonce,
                "to": tx.to,
                "transaction_index": tx.transaction_index,
                "value": tx.value,
                "r": tx.r,
                "s": tx.s,
                "v": tx.v
            })

        block_data['transactions'] = transactions
        block_data['tx_count'] = len(transactions)
        results.append(block_data)
    
    sys.stdout.write(json.dumps(results))



if __name__ == "__main__":
    argParser = argparse.ArgumentParser()
    argParser.add_argument("--heights", nargs='+', default=None, help="List of block heights to parse.")
    args = argParser.parse_args()
    if not args.heights:
        raise Exception("No block heights provided.")

    block_heights = [int(height) for height in args.heights if height]
    main(block_heights)
