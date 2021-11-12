from fastecdsa import curve,ecdsa, keys
from uuid import uuid4
import datetime
import json

class Account:


	def generate_priv_key(self):
		private_key = keys.gen_private_key(curve.secp256k1)
		return private_key

	def generate_pub_key(self, private_key):
		public_key = keys.get_public_key(private_key, curve.secp256k1)
		return public_key

	# create transcation then sign the transaction with keys

	def create_transaction(self, data) -> dict:
		trans_id = str(uuid4()).replace('-','')
		timestamp = str(datetime.datetime.now())
		trans = { 
				'trans_id': trans_id,
				'timestamp': timestamp,
				'data': data
				}

		return trans

	def get_signature(self, trans: dict, private_key: int):
		# sign a message using the elliptic curve digital signature algorithm
		hash_func = ecdsa.sha256
		sign_curve = curve.secp256k1
		
		# note: we need to convert dict to bytes before signing
		trans_to_bytes = json.dumps(trans)

		# we can also encode it 
		encoded_trans = trans_to_bytes.encode()

		signature = ecdsa.sign(encoded_trans, private_key, sign_curve, hash_func)

		# return {x,y}
		return signature




		


account = Account()
transcation = account.create_transaction("I am selling stuff")
private = account.generate_priv_key()
print (account.get_signature(transcation,private))



