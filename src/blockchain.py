'''
    This module provides a Simple Blockchain implementation for learning.

    Block Structure: https://gist.github.com/dvf/79633bf97e2a831f066f699d41c2b9d5#file-blockchain-py
'''

from time import time
import json
import hashlib
from urllib.parse import urlparse
import requests
from proof import Proof


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

        # Create a set of nodes in the network.
        self.nodes = set()

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
            'previous_hash' : previous_hash or self.hash(self.chain[-1])
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


    @staticmethod
    def hash(block):
        '''
            Creates a SHA-256 hash of the block

            :param block: <dict> block
            :return <str> The hash of the block.
        '''

        # Dictionary is ordered so that hashes are not inconsistent.
        block_string = json.dumps(block, sort_keys=True).encode()

        # Hash the string and produce a hexadecimal digest
        # so that it can be shared safely.
        return hashlib.sha256(block_string).hexdigest()


    @property
    def last_block(self):
        '''
            Returns the last block in the chain.
        '''

        return self.chain[-1]


    def register_node(self, address):
        '''
            Add a new node to the set of nodes

            :param address: <str> HTTP Address of the node
            :return None
        '''

        parsed_url = urlparse(address)
        self.nodes.add(parsed_url)


    def valid_chain(self, chain):
        '''
            Determine if a given blockchain is valid by looping through
            each block and verifying both hash and the proof

            :param chain: <list> A blockchain to verify
            :return: <bool> True if valid, else False
        '''

        last_block = chain[0]
        current_index = 1

        while current_index < len(chain):
            block = chain[current_index]
            print(f'{last_block}')
            print(f'{block}')
            print('\n-------\n')

            # Check of the current block is correct
            if block['previous_hash'] != self.hash(last_block):
                return False

            # Check that the proof of work is correct
            # by validating the last blocks proof against the current blocks proof
            if not Proof.valid_proof(last_block['proof'], block['proof']):
                return False

        # If all above checks pass, then the block is valid.
        return True

    def resolve_conflicts(self):
        '''
            Consensus Algorithm, resolves conflicts by replacing our chain with the longest one
            in the network.

            Loop through each of the neighboring nodes.
            If a valid chain is found whose length is greater than ours then replace ours

            return: <bool> True if the chain was replaced, else False
        '''

        neighbours = self.nodes
        new_chain = None

        # Store the current length of our chain to compare others.
        max_length = len(self.chain)

        # For each registered nodes, check if thier chains are longer and valid.
        for node in neighbours:
            response = requests.get(f'http://{node}/chain')

            if response.status_code == 200:
                length = response.json()['length']
                chain = response.json()['chain']

                # Check if the lenght is longer and it is valid, if so then store.
                if (length > max_length and self.valid_chain(chain)):
                    max_length = length
                    new_chain = chain

        # If we found a new valid chain longer than ours then store it.
        if new_chain:
            self.chain = new_chain
            return True

        return False
