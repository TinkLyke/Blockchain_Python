#!/usr/bin/python
# -*- coding: utf-8 -*-

from datetime import datetime
from hashlib import sha256
#import json
#from flask import Flask, jsonify, request
#import requests
#from uuid import uuid4
#from urllib.parse import urlparse
#from fastecdsa import curve,ecdsa, keys
#import zmq
#import threading
#from flask_mysqldb import MySQL

# Form the hash text
def form_hash_text(self, *args):
	hash_text = ""
	for arg in args:
		hash_text += str(arg)

	return hash_text

# Create a block
class Block():
	data = ""
	hash = ""
	nonce = 0
	prev_hash = "0"*64

	# Initialize new block, overload block number each time
	def __init__(self, data, number = 0):
		self.data = data
		self.number = number

	# Hash the data
	def hash(self):
		hash_txt = form_hash_text(
				self.prev_hash,
				self.number,
				self.data,
				self.nonce
				)

		hash_func = sha256()
		hash_func.update(hash_txt.encode('utf-8')) 
		new_hash = hash_func.hexdigest()
		return new_hash

	# Print block in good format
	def __str__(self):
		return str("Block#: %s\nHash: %s\nPrevious: %s\nData: %s\nNonce: %s\n" %(
				self.number,
				self.hash(),
				self.prev_hash,
				self.data,
				self.nonce
				))


class Blockchain():
	# Set difficulty - hash with '0000'
	difficulty = 4

	# Initialize blockchain with a empty chain
	def __init__(self, chain=[]):
		self.chain = chain

	# Adding a block to the chain
	def add(self, block):
		self.chain.append({
				'hash': block.hash(),
				'previous': block.prev_hash,
				'number': block.number,
				'data': block.data,
				'nonce': block.nonce
				})

	def mine(self, block):
		# Try to get the previous hash from the last block of the chain
		try:
			block.prev_hash = self.chain[-1].get('hash')

		# If we don't have any
		except IndexError:
			pass

		# If the hash of the block starts with '0000', then we add it into block. else, we increase nonce and re-do the hash.
		while True:
			if block.hash()[:4] == "0" * 4:
				self.add(block)
				break
			else:
				block.nonce += 1




def main():

	# Generating a blockchain and add data into chain
	new_blockchain = Blockchain()
	database = ['hello','I want to','sleep','tired']

	block_number = 0

	# Add data starting with no. 1 block
	for block_data in database:
		block_number += 1
		# Create new block with new data
		new_block = Block(block_data,block_number)
		
		new_blockchain.mine(new_block)

	for single_block in new_blockchain.chain:
		print(single_block)

if __name__ == '__main__':
	main()
