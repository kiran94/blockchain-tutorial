'''
    Test module contains tests of the Hash class.
'''
import unittest
from hash import Hash


class HashTests(unittest.TestCase):
    '''
        hash tests
    '''

    def test_hash_block(self):
        '''
            Ensures when a block is hashed, the SHA-256 hex is returned.
        '''
        block = {
            'index' : 1,
            'timestamp' : '2017',
            'transactions' : [],
            'proof' : '123',
            # New block stores the has of the previous block.
            'previous_hash' : 'previous'
        }

        result = Hash.hash(block)
        self.assertEqual('8b8f4e1c0dbce1064bb672b8d002b510b52e8a8c14cce01ae07f48929543c1e3', result)
