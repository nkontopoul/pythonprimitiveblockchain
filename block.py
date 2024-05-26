# block.py

import hashlib
import datetime

class Block:
    def __init__(self, index, timestamp, transactions, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()
    
    def calculate_hash(self):
        transactions_string = "".join(str(tx) for tx in self.transactions)
        block_string = f"{self.index}{self.timestamp}{transactions_string}{self.previous_hash}"
        return hashlib.sha256(block_string.encode()).hexdigest()
