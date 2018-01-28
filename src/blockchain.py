'''
    This module provides a Simple Blockchain implementation for learning.

    Block Structure: https://gist.github.com/dvf/79633bf97e2a831f066f699d41c2b9d5#file-blockchain-py
'''

from time import time
from hash import Hash

class Blockchain:
    '''
        Blockchain implementation
        Responsible for managing the chain
        and will store transactions and have some helper
        functions for interacting with the chain.
    '''

    def __init__(self):
        '''
            Creates an Empty Blockchain instance.
        '''

        # Create an empty chain and no transactions on start.
        self.chain = []
        self.current_transactions = []

        # Create the Genesis Block.
        self.new_block(proof=100, previous_hash=1)


    def new_block(self, proof, previous_hash=None):
        '''
            Creates a new Block in the Blockchain.

            :param proof: <int> The Proof given by the proof of work algorithm
            :param previous_hash: (Optional) <str> Hash of the previous block
            :return <dict> New Block.
        '''

        # Create the new block with the current transactions
        # and linked to the previous hash or latest in the chain.
        block = {
            'index' : len(self.chain) + 1,
            'timestamp' : time(),
            'transactions' : self.current_transactions,
            'proof' : proof,
            # New block stores the has of the previous block.
            'previous_hash' : previous_hash or Hash.hash(self.chain[-1])
        }

        # Reset the current list of transactions
        # as they have been mined into the above block.
        self.current_transactions = []

        # Add the block to the chain.
        self.chain.append(block)

        return block


    def new_transaction(self, sender, recipient, amount):
        '''
            Creates a new transaction to go to the next mined block.

            :param sender: <str> Address of the sender
            :param recipient: <str> Address of the recipient
            :param amount: <int> Amount to send
            :return: <int> The index of the block that will hold this transaction.
        '''

        # Add the new transaction to the current transactions,
        # to be mined in the next block.
        self.current_transactions.append(
            {
                'sender' : sender,
                'recipient' : recipient,
                'amount' : amount
            })

        return self.last_block["index"] + 1

    @property
    def last_block(self):
        '''
            Returns the last block in the chain.
        '''

        return self.chain[-1]
