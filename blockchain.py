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
	# Set difficulty
	difficulty = 4

	def __init__(self, chain=[]):
		self.chain = Blockchain

	# Adding a block to the chain
	def add(self, block):
		self.chain.append({
				'hash': block.hash(),
				'previous': block.previous_hash,
				'number': block.number,
				'data': block.data,
				'nonce': block.nonce
				})


def main():
	block = Block("Hello", 1)
	print(block)

if __name__ == '__main__':
	main()
