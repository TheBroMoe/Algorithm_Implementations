class Node:
	def __init__(self, data = None, next = None, prev = None):
		self.data = data
		self.next = next
		self.prev = prev
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

class DoublyLinkedList(object):
	def __init__(self):
		self.head = None
		self.tail = None
		self.index = 0
	
	def traverse(self):
		current = self.tail
		while current:
			val = current.data
			current = current.next
			yield val
	
	def append(self, data):
		new_node = Node(data, None, None)
		if self.head is None:
			self.head = new_node
			self.tail = self.head
		else:
			new_node.prev = self.tail
			self.tail.next = new_node
			self.tail = new_node

			self.index +=1

	def delete(self, data):
		current = self.head
		node_deleted = False

		if current is None:
			node_deleted = False

		elif current.data == data:
			self.head = current.next
			self.head.prev = None
			node_deleted = True

		elif self.tail.data == data:
			self.tail = self.tail = prev
			self.tail.next = None
			node_deleted = True
		else:
			while current:
				if current.data == data:
					current.prev.next = current.next
					current.next.prev = current.prev
					node_deleted = True
					current = current.next
		if node_deleted:
			self.index -= 1

	def find(self, data):
		for node_data in self.iter():
			if data == node_data:
				return True
		return false