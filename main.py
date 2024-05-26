# main.py

from blockchain import Blockchain
from transaction import Transaction

def main():
    my_blockchain = Blockchain()
    
    # Create transactions
    tx1 = Transaction("Alice", "Bob", 50)
    tx2 = Transaction("Bob", "Charlie", 25)
    
    # Add transactions to the blockchain
    my_blockchain.create_transaction(tx1)
    my_blockchain.create_transaction(tx2)
    
    print("Starting the miner...")
    my_blockchain.mine_pending_transactions("MinerAddress")
    
    print("Mining complete. Reward sent to MinerAddress")
    
    print("Starting the miner again...")
    tx3 = Transaction("Charlie", "Alice", 10)
    my_blockchain.create_transaction(tx3)
    my_blockchain.mine_pending_transactions("MinerAddress")
    
    print("Mining complete. Reward sent to MinerAddress")
    
    for block in my_blockchain.chain:
        print(f"Block {block.index} [Hash: {block.hash}, Previous Hash: {block.previous_hash}, Transactions: {block.transactions}]")
    
    print("Blockchain valid?", my_blockchain.is_chain_valid())

if __name__ == "__main__":
    main()
