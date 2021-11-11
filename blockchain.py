import datetime
import hashlib
import json
from flask import Flask, jsonify, request
import requests
from uuid import uuid4
from urllib.parse import urlparse
from fastecdsa import curve,ecdsa, keys
import zmq
import threading
from flask_mysqldb import MySQL

class Blockchain:
	def create_genesis_block:
		curr_time = datetime.datetime.now()
		block = {}
		block['index'] = 1
		block['pre_hash'] = '0000000000'
		block['nonce'] = 456
		block['data'] = 'This is the genesis block of blockcahin'
		block['timestamp'] = curr_time.strftime('%Y-%m-%d %H:%M:%S.%f')

