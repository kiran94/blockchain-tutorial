# blockchain-tutorial ⛓ [![Build Status](https://travis-ci.org/kiran94/blockchain-tutorial.svg?branch=master)](https://travis-ci.org/kiran94/blockchain-tutorial) [![Codacy Badge](https://api.codacy.com/project/badge/Grade/11b3a58b3433471ab8925c8131da9aed)](https://www.codacy.com/app/kiran94/blockchain-tutorial?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=kiran94/blockchain-tutorial&amp;utm_campaign=Badge_Grade)

Understanding the basic concepts of Blockchain and implementing a basic solution using a [tutorial](https://hackernoon.com/learn-blockchains-by-building-one-117428612f46).

## Concepts

### Blockchain

A Blockchain is an **immutable, sequential chain of records called blocks**. These blocks can contain transactions, files or any kind of data. The important thing is that they are chained together using *hashes*.

#### Chain
Stored internally to the Blockchain, this represents a list of *Blocks*. The chain is made immutable by linking together blocks via the previous' block hash all the way back to the *genesis block*.

#### Block
These are stored within the chain as immutable units. Each blocks links to the previous block via hashes.

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









