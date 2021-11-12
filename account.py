from fastecdsa import curve,ecdsa, keys
from uuid import uuid4
import datetime


class Account:


	def generate_priv_key(self):
		private_key = keys.gen_private_key(curve.secp256k1)
		return private_key

	def generate_pub_key(self, private_key: keys):
		public_key = keys.get_public_key(private_key, curve.secp256k1)
		return public_key

	#next create transcation then sign the transaction with keys

	def create_transaction(self, data) -> str:
		trans_id = str(uuid4()).replace('-','')
		timestamp = str(datetime.datetime.now())
		trans = { 
				 'trans_id': trans_id,
				 'timestamp': timestamp,
				 'data': data
				}

		return trans

		


account = Account()
print (account.create_transaction("hello"))


