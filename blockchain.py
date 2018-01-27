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

    def new_transaction(self, sender, recipient, amount):
        '''
            Creates a new transaction to go to the next mined block.

            :param sender: <str> Address of the sender
            :param recipient: <str> Address of the recipient
            :param amount: <int> Amount to send
            :return: <int> The index of the block that will hold this transaction.
        '''

        self.current_transactions.append(
            {
                'sender' : sender,
                'recipient' : recipient,
                'amount' : amount
            })

        return self.last_block["index"] + 1

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
