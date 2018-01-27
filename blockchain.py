'''
    This module provides a Simple BlockChain implementation for learning.

    Block Structure: https://gist.github.com/dvf/79633bf97e2a831f066f699d41c2b9d5#file-blockchain-py
'''

class Blockchain(object):
    '''
        Blockchain implementation
        Responsible for managing the chain and will store transactions and have some helper
        functions for interacting with the chain.
    '''

    def __init__(self):
        '''
            Creates an Empty Blockchain instance.
        '''
        self.chain = []
        self.current_transactions = []

    def new_block(self):
        '''
            Creates a new block and adds it to the chain.
        '''
        pass

    def new_transaction(self):
        '''
            Adds a new transaction to the list of transactions.
        '''
        pass

    @staticmethod
    def hash(block):
        '''
            Hashes a Block.
        '''
        pass

    @property
    def last_block(self):
        '''
            Returns the last block in the chain.
        '''
        pass
