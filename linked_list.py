class Node:
	def __init__(self, data = None):
		self.data = data
		self.next = None
	def __str__(self):
		return str(data)

class SinglyLinkedList:
	def __init__(self):
		self.tail = None
		self.head = None
		self.size = 0
		

	def append(self, data):
		node = Node(data)
		if self.head:
			self.head.next = node
			self.head = node
		else:
			self.tail = node
			self.head = node
		self.size +=1

	def Size(self):
		return self.size

	def traverse(self):
		current = self.tail
		while current:
			val = current.data
			current = current.next
			yield val

	def delete(self, desired):
		current = self.tail
		prev = self.tail
		while current:
			if current.data == desired:
				if current == self.tail:
					self.tail = current.next
				else:
					prev.next = current.next

				self.size -= 1
				return
			prev = current
			current = current.next

	def find(self, data):
		for node in self.traverse():
			if data == node:
				return True
		return false

	def clear(self):
		self.tail = None
		self.head = None