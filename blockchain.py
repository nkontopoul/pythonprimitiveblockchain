# blockchain.py

from block import Block
from transaction import Transaction
import datetime

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.pending_transactions = []
        self.mining_reward = 100
    
    def create_genesis_block(self):
        return Block(0, datetime.datetime.now(), [], "0")
    
    def get_latest_block(self):
        return self.chain[-1]
    
    def mine_pending_transactions(self, mining_reward_address):
        reward_tx = Transaction(None, mining_reward_address, self.mining_reward)
        self.pending_transactions.append(reward_tx)
        
        new_block = Block(len(self.chain), datetime.datetime.now(), self.pending_transactions, self.get_latest_block().hash)
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)
        
        self.pending_transactions = []
    
    def create_transaction(self, transaction):
        self.pending_transactions.append(transaction)
    
    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            
            if current_block.hash != current_block.calculate_hash():
                print("Current Block Hashes not equal")
                return False
            
            if current_block.previous_hash != previous_block.hash:
                print("Previous Block Hashes not equal")
                return False
        
        return True
