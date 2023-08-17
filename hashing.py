import hashlib

for i in range(5):
	hash = hashlib.md5(b"Hashing BTC")
	print(hash.hexdigest())