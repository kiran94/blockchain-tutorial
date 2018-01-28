'''
    Module contains logic to interact with nodes.
'''

from urllib.request import urlparse

class Nodes:
    '''
        Interactions with nodes.
    '''

    def __init__(self):
        '''
            Initialises a new instance of the nodes.
        '''
        self.nodes = set()


    def register_node(self, address):
        '''
            Add a new node to the set of nodes

            :param address: <str> HTTP Address of the node
            :return None
        '''

        parsed_url = urlparse(address)
        self.nodes.add(parsed_url)
