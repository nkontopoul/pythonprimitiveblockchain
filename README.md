# pythonprimitiveblockchain
a simple blockchain without Proof-of-Work


Running the Blockchain

    Navigate to the blockchain_project directory.
    Run the main script:  python main.py



    Explanation

    transaction.py: Defines the Transaction class with sender, receiver, and amount attributes.
    block.py: Defines the Block class that includes the block index, timestamp, transactions, previous hash, and its own hash.
    blockchain.py: Defines the Blockchain class that manages the chain of blocks, pending transactions, mining, and validation.
    main.py: Tests the blockchain by creating transactions, mining them, and displaying the blockchain's contents.


    Transaction Class:
        Defines a transaction with sender, receiver, and amount.
        The __repr__ method provides a string representation for easier debugging.

    Block Class:
        Modified to include a list of transactions.
        The calculate_hash method concatenates transaction strings for hashing.

    Blockchain Class:
        Manages pending transactions and mining rewards.
        The mine_pending_transactions method creates a new block from pending transactions and rewards the miner.
        The create_transaction method adds a new transaction to the pending list.

    Testing:
        Creates transactions and mines blocks, rewarding a miner for validating transactions.
        Prints block information and checks blockchain validity.

Directory Structure

Organize your files in the following directory structure:

blockchain_project/
├── transaction.py
├── block.py
├── blockchain.py
└── main.py

