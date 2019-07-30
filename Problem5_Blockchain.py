
# coding: utf-8

# In[1]:


#Problem 5: Blockchain 
import datetime
import hashlib

class Node:
    def __init__(self, block):
        self.block = block
        self.next = None
        
class Block:
    def __init__(self, timestamp, data, previous_hash):
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash()

    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = 'string of data'.encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()
    
    def __repr__(self):
        return f"Timestamp: {self.timestamp} \nData: {self.data} \nPrevious_hash: {self.previous_hash} \nHash: {self.hash}"
    
class BlockChain:
    def __init__(self, timestamp, data):
        self.head = Node(Block(timestamp, data, None))
        self.tail = self.head
        

    def addBlock(self, timestamp, data):
        if data is None:
            print('blockchain empty')
            return
        else:
            newBlock = Block(timestamp, data, self.tail.block.hash)
            newNode = Node(newBlock)
            self.tail.next = newNode
            self.tail = newNode
        
    def printChain(self):
        currentNode = self.head
        while currentNode:
            print(currentNode.block)
            currentNode = currentNode.next

# Test Case 1
print('---test case1---')
blockchain = BlockChain('5:55 6/20/2019', 'blockchain information')
blockchain.addBlock('5:55 7/20/2019', 'blockchain information')
blockchain.printChain()

# Test Case 2 "Block chain empty!"
print('---test case2---')
blockchain2 = BlockChain('', None)
blockchain2.addBlock('', None)
blockchain2.printChain()

# Test Case 3 Another could be to verify if the previous hash of the very first block of the block chain is None.
print('---test case3---')
blockchain2 = BlockChain('', None)
blockchain2.addBlock('', '')
blockchain2.printChain()

