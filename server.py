'''
    Modules provides a web service to provide interaction with the BlockChain instance.
'''

from uuid import uuid4

from flask import Flask
from flask import jsonify

from blockchain import Blockchain

# Initialise a Node
app = Flask(__name__)

# Generate a globally unique address
node_id = str(uuid4()).replace('-', '')

#Initialise the blockchain
blockchain = Blockchain()

@app.route('/mine', methods=['GET'])
def mine():
    '''
        Mine a new block.
    '''
    return "mine"

@app.route('/transactions/new', methods=['GET'])
def new_transactions():
    '''
        Add a new transaction
    '''
    return "mine"

@app.route('/chain', methods=['GET'])
def chain():
    '''
        Get the entire blockchain
    '''
    response = {
        'chain' : blockchain.chain,
        'length' : len(blockchain.chain)
    }

    return jsonify(response), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
