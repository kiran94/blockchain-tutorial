'''
    Module contains logic to run consensus amongst nodes
'''

import requests

from hash import Hash
from proof import Proof


class Consensus:
    '''
        Consensus class.
    '''

    @staticmethod
    def valid_chain(chain):
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
            if block['previous_hash'] != Hash.hash(last_block):
                return False

            # Check that the proof of work is correct
            # by validating the last blocks proof against the current blocks proof
            if not Proof.valid_proof(last_block['proof'], block['proof']):
                return False

        # If all above checks pass, then the block is valid.
        return True

    @staticmethod
    def resolve_conflicts(nodes, blockchain):
        '''
            Consensus Algorithm, resolves conflicts by replacing our chain with the longest one
            in the network.

            Loop through each of the neighboring nodes.
            If a valid chain is found whose length is greater than ours then replace ours

            :param nodes: <set> list of nodes to resolve conflcts with.
            :param blockchain: <blockchain> blockchain to resolve conflicts on.

            return: <bool> True if the chain was replaced, else False
        '''

        neighbours = nodes
        new_chain = None

        # Store the current length of our chain to compare others.
        max_length = len(blockchain.chain)

        # For each registered nodes, check if their chains are longer and valid.
        for node in neighbours:
            response = requests.get(f'http://{node}/chain')

            if response.status_code == 200:
                length = response.json()['length']
                chain = response.json()['chain']

                # Check if the lenght is longer and it is valid, if so then store.
                if (length > max_length and Consensus.valid_chain(chain)):
                    max_length = length
                    new_chain = chain

        # If we found a new valid chain longer than ours then store it.
        if new_chain:
            blockchain.chain = new_chain
            return True

        return False
