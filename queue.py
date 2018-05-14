
class ListQueue:
	def __init__(self):
		self.items = []
		self.size = 0

	def enqueue(self, data):
		self.items.insert(0, data)
		self.size += 1

	def dequeue(self):
		data = self.items.pop()
		self.size -= 1
		return data

class StackQueue:
	def __init__(self):
		self.inbound_stack = []
		self.outbound_stack = []

	def enqueue(self, data):
		self.inbound_stack.append(data)

	def dequeue(self):
		if not self.outbound_stack:
			while self.inbound_stack:
				self.outbound_stack.append(self.inbound_stack.pop())
		return self.outbound_stack.pop()


class NodeQueue:
	def __init__(self):
		self.head = None
		self.tail = None
		self.index = 0

	def enqueue(self, data):
		new_node = Node(data, None, None)
		if self.head is None:
			self.head = new_node
			self.tail = self.head
		else:
			new_node.prev = self.tail
			self.tail.next = new_node
			self.tail = new_node

		self.index += 1

	def dequeue(self):
		current = self.head
		if self.index == 1:
			self.index -= 1
			self.head = None
			self.tail = None
		elif self.count > 1:
			self.head = self.head.next
			self.head.prev = None
			self.count -= 1