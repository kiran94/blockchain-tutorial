'''
    Modules provides a web service to provide interaction with the BlockChain instance.
'''

from uuid import uuid4

from flask import Flask, jsonify, request

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
        Takes a JSON transaction request and adds it to the BlockChain.
    '''
    values = request.get_json()

    # Check if the incoming request json has all the required fields.
    required = ['sender', 'recipient', 'amount']
    if not all(k in values for k in required):
        return 'Missing values', 400

    # Mak the new transaction and get the block it will be added too.
    index = blockchain.new_transaction(values['sender'], values['recipient'], values['amount'])

    # Return a json message.
    response = { 'message' : f'Transaction will be added to Block {index}'}
    return jsonify(response), 201



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
