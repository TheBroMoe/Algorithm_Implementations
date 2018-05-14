class Node:
	def __init__(self, data = None):
		self.data = data
		self.next = None
	def __str__(self):
		return str(data)
class SinglyLinkedList:
	def __init__(self):
		self.tail = None