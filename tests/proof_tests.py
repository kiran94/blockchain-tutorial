'''
    Test module contains tests of the Proof class.
'''
import unittest

from proof import Proof


class ProofTests(unittest.TestCase):
    '''
        proof tests
    '''

    def test_proof_of_work(self):
        '''
            Ensures that given the proof of one,
            the next proof is 72608 for 4 leading zero solution.
        '''
        result = Proof.proof_of_work(1)
        self.assertEqual(72608, result)

    def test_valid_proof(self):
        '''
            Ensures that the validation method is working correctly.
        '''
        self.assertTrue(Proof.valid_proof(1, 72608))
