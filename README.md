# blockchain-tutorial ⛓
[![Build Status](https://travis-ci.org/kiran94/blockchain-tutorial.svg?branch=master)](https://travis-ci.org/kiran94/blockchain-tutorial) [![Codacy Badge](https://api.codacy.com/project/badge/Grade/11b3a58b3433471ab8925c8131da9aed)](https://www.codacy.com/app/kiran94/blockchain-tutorial?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=kiran94/blockchain-tutorial&amp;utm_campaign=Badge_Grade)

Understanding the basic concepts of Blockchain and implementing a basic solution using a [tutorial](https://hackernoon.com/learn-blockchains-by-building-one-117428612f46).

- [blockchain-tutorial ⛓](#blockchain-tutorial-%E2%9B%93)
    - [Concepts](#concepts)
        - [Blockchain](#blockchain)
            - [Chain](#chain)
            - [Block](#block)
            - [Genesis Block](#genesis-block)
        - [Proof Of Work](#proof-of-work)
            - [Example](#example)
        - [Consensus](#consensus)

## Concepts

### Blockchain

A Blockchain is an **immutable, sequential chain of records called blocks**. These blocks can contain transactions, files or any kind of data. The important thing is that they are chained together using *hashes*.

#### Chain
Stored internally to the Blockchain, this represents a list of *Blocks*. The chain is made immutable by linking together blocks via the previous' block hash all the way back to the *genesis block*.

#### Block
These are stored within the chain as immutable units. Each blocks links to the previous block via hashes. Blocks contain a collection of transactions to be mined at this particular time.

A Block has the following attributes:
- Index
- Timestamp (Unix Time)
- List of Transactions
- A Proof
- Hash of the previous Block

It may look like this in python:

```python
block =
{
    'index' : 1,
    'timstamp' : 1506057125.900785,
    'transaction':
    [
        {
            'sender' : 'a3c7b0ac4847de209d9bb97456d73e8e90be9731',
            'recipient' : '05ded7cc61dd1dc39079078fa5e14a61fcea5d72',
            'amount' : 5
        }
    ],
    'proof' : '98763248642',
    'previous_hash' : '4768898f3bb54180ac6ba1ad11094f04ea07f30f'
}
```
**The previous hash is crucial here and gives the Blockchain Immutability. It means that if an attacker corrupted an earlier block in the chain then all subsequent blocks will contain incorrect hashes. This is because any changes to the input of a hash function will drastically change the output. Linking this together in a chain means that any changes to earlier blocks, drastically changes all subsequent hashes in the chain.**

#### Genesis Block
Due to the chaining of these blocks, we need a way to seed the very start of the Blockchain. This is achieved using the Genesis block. This block has no predecessors and is mined at initialization.

### Proof Of Work
A Proof of Work (Pow) algorithm is *how blocks are created (mined)* on the blockchain. *The goal of PoW is to discover a number which solves a problem.*

The number must be computationally difficult to find but easy to verify by anyone on the network.

#### Example
Given `x` and `y`, find the hash which when `x` and `y` are multiplied, the result must end in `0`.

`hash(x * y) = ac23dc...0`

To simplify this example, we will fix `x=5` and just examine the `y` value.

This algorithm may look like this:

```python
from hashlib import sha256

x = 5
y = 0 #  To start with

# While the end of the hash of the
# multiplication of x and y does not equal 0,
# keep incrementing y
while sha256(f'{x * y}'.encode()).hexdigest()[-1] != "0":
    y +=1

print(f'The solution is y = {y}')
```

The solution for this specific example is `y = 21`. This is because the produced has of `hash(5 * 21) = 1253e937...0` which ends in zero and therefore meets our requirement.

*The PoW algorithm used in Bitcoin is not too different to this example. Miners race to solve this kind of problem in order to create a new block. When they eventually do solve the problem, they are awarded coins in the form of a transaction. This transaction is added to the currently mined block just before it is added to the chain.*

**In general, the difficulty is determined by the number of characters searched for in the string.** We can adjust the difficulty by modifying the number of leading zeroes required. Adding additional zeros makes big differences in the time required to compute the hash.

The network is then easily able to verify the solution by running the two numbers in the hash algorithm and verifying the 0 requirement in the produced hash.

### Consensus
The Consensus Algorithm ensures that we have the same chain in a decentralized system. Blockchain is decentralised and we therefore each node has its own copy of the chain.

**A conflict is when one node has a different chain to another node. To resolve this, we'll make the rule that the longest valid chain is authoritative.** Using this we can ensure the nodes reach a *Consensus* on the chain in the network.