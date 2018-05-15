class HashItem:
	def __init__(self, key, value):
		self.key = key
		self.value = value

class HashTable:
	def __init__(self):
		self.size = 256
		self.slots = [None for i in range(self.size)]
		self.counter = 0

	def __setitem__(self, key, value):
		self.insert(key, value)

	def __getitem__(self, key):
		return self.get(key)

	def _hashing(self, key):
		multiplier = 1
		hashVar = 0
		for char in key:
			hashVar += multiplier * ord(char)
			multiplier += 1
		return hashVar % self.size

	def insert(self, key, value):
		item = HashItem(key, value)
		hashVar = self._hashing(key)

		while self.slots[hashVar] is not None:
			if self.slots[hashVar].key is key:
				break
			hashVar = (hashVar + 1) % self.size

		if self.slots[hashVar] is None:
			self.counter += 1
		self.slots[hashVar] = item

	def get(self, key):
		hashVar = self._hashing(key)

		while self.slots[hashVar] is not None:
			if self.slots[hashVar].key is key:
				return self.slots[hashVar].value
			hashVar = (hashVar + 1) % self.size

		return None

