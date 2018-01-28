'''
    Module provides a proof of work algorithm and validation implementation.
'''

import hashlib

class Proof:
    '''
        Proof of work implementation.
    '''

    @staticmethod
    def proof_of_work(last_proof):
        '''
            Simple Proof of Work Algorithm:
            - Find a number p' such that hash(pp') contains 4 leading zeros.
            - Where p is the previous proof of work and p' is the new one.

            :param last_proof: <int> the previous proof of work
            :return <int> the new proof of work
        '''

        # While the new proof is not valid, keep incrementing it.
        proof = 0
        while Proof.valid_proof(last_proof, proof) is False:
            proof += 1

        return proof

    @staticmethod
    def valid_proof(last_proof, proof):
        '''
            Validates the Proof: Does hash(last_proof, proof) contain 4 leading zeros?

            :param last_proof: <int> previous proof
            :param proof: <int> current proof
            :return: <bool>: True if valid, else False.
        '''

        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()

        # If the hash of the previous and current does not have 4 leading zeros then return faslse
        return guess_hash[:4] == "0000"
