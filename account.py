from fastecdsa import curve,ecdsa, keys
from uuid import uuid4

class Account:


	def generate_priv_key(self):
		private_key = keys.gen_private_key(curve.secp256k1)
		return private_key

	def generate_pub_key(self, private_key: keys):
		public_key = keys.get_public_key(private_key, curve.secp256k1)
		return public_key



account = Account()

pvk = account.generate_priv_key()
puk = account.generate_pub_key(pvk)


print ('private key: ', pvk)
print ('public key: ', puk)