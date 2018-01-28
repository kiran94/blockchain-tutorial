'''
    Module contains logic for hashing operations.
'''

import hashlib
import json

class Hash:
    '''
        Hashing Operations.
    '''

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
