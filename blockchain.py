#!/usr/bin/python
# -*- coding: utf-8 -*-

from datetime import datetime
from hashlib import sha256
import json
from flask import Flask, jsonify, request
import requests
from uuid import uuid4
from urllib.parse import urlparse
from fastecdsa import curve,ecdsa, keys
import zmq
import threading
from flask_mysqldb import MySQL

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

	def __init__(self, data, number = 0):
		self.data = data
		self.number = number

	# Hash the data
	def hash(self):
		hash_txt = form_hash_text(self.prev_hash,self.number,self.data,self.nonce)

		hash_func = sha256()

		hash_func.update(hash_txt.encode('utf-8'))

		new_hash = hash_func.hexdigest()
		return new_hash

	def __str__(self):
		return str("Block#: %s\nHash: %s\nPrevious: %s\nData: %s\nNonce: %s\n"
					%(self.number,self.hash(),self.prev_hash,self.data,self.nonce))


class Blockchain():
	difficulty = 4
#	def create_genesis_block(self):
#		curr_time = datetime.now()
#		block = {}
#		block['index'] = 1
#		block['prev_hash'] = '0000000000'
#		block['nonce'] = 456
#		block['data'] = 'This is the genesis block of blockcahin'
#		block['timestamp'] = curr_time.strftime('%Y-%m-%d %H:%M:%S.%f')

#		encoded_block = json.dumps(block, sort_keys = True).encode()

#		# can change the encryption mode - SHA256
#		new_hash = hashlib.sha256(encoded_block).hexdigest()
#		block['new_hash'] = new_hash

def main():
	block = Block("Hello", 1)
	print(block)

if __name__ == '__main__':
	main()
