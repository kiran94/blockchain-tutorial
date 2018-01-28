'''
    Modules provides a web service to provide interaction with the BlockChain instance.
'''

from uuid import uuid4

from flask import Flask, jsonify, request

from blockchain import Blockchain
from consensus import Consensus
from hash import Hash
from nodes import Nodes
from proof import Proof

# Initialise a Node and generate a globally unique address
app = Flask(__name__)
node_id = str(uuid4()).replace('-', '')

blockchain = Blockchain()
proof = Proof()
nodes = Nodes()
consensus = Consensus()

@app.route('/mine', methods=['GET'])
def mine():
    '''
        Mine a new block.
    '''

    # Get the previous block and proof and find the new proof.
    previous_block = blockchain.last_block
    previous_proof = previous_block["proof"]
    new_proof = proof.proof_of_work(previous_proof)

    # Because the user is mining a block, we want to reward them with a block,
    # so we create a transaction which will be added to the blockchain
    # in the new_block method below.
    blockchain.new_transaction(
        sender="0",
        recipient=node_id,
        amount=1
    )

    # Forge the new block by adding it to the blockchain
    previous_hash = Hash.hash(previous_block)
    new_block = blockchain.new_block(new_proof, previous_hash)

    # Send the response back with the block details.
    response = {
        'message': "New Block Forged",
        'index': new_block['index'],
        'transactions': new_block['transactions'],
        'proof': new_block['proof'],
        'previous_hash': new_block['previous_hash'],
    }

    return jsonify(response), 200

@app.route('/transactions/new', methods=['POST'])
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
    response = {'message' : f'Transaction will be added to Block {index}'}
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

@app.route('/node/register', methods=['POST'])
def register():
    '''
        Accepts a list of new nodes in the form of URLs and registers them with the current node.
    '''

    values = request.get_json()
    received_nodes = values.get('nodes')

    if received_nodes is None:
        return "Error: please supply a valid list of nodes", 400

    for node in received_nodes:
        nodes.register_node(node)

    response = {
        'message' : 'New Nodes have been added',
        'total_nodes' : list(nodes.nodes)
    }

    return jsonify(response), 201

@app.route('/node/resolve', methods=['GET'])
def resolve():
    '''
        Runs the Consensus algorithm to resolve any conflicts
        and ensure a node has the correct chain.
    '''
    replaced = Consensus.resolve_conflicts(nodes.nodes, blockchain)

    if replaced:
        response = {
            'message' : 'our chain is replaced',
            'new_chain' : blockchain.chain
        }
    else:
        response = {
            'message' : 'our chain wins',
            'chain' : blockchain.chain
        }

    return jsonify(response), 200

if __name__ == '__main__':
    '''
        Main Entry Point.
    '''
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-p', '--port', type=int, default=5000, help='port to use')
    args = parser.parse_args()

    app.run(host='0.0.0.0', port=args.port)
