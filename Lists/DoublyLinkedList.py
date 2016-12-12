#!Python3
import Node
class LinkedListError(Exception): pass

class DoublyLinkedList(object):
	def __init__(self):
		self.head = None
		self.tail = None

	def __str__(self):
		data = []
		temp = self.head
		if(temp is self.head):
			return str(temp.data)
		else:
			while temp is not self.tail:
				data.append(temp.data)
				temp = temp.next
		data.append(temp.data)
		return str(data)

	def __repr__(self):
		temp = self.head
		data = []
		if(temp is self.head):
			return str(temp.data)
		else:
			while temp is not self.tail:
				data.append(str(repr(temp)+'\n'))
				temp = temp.next
		data.append(str(repr(temp)+'\n'))
		return str(data)
		
		
	def insertAfter(self,node,newNode):
		"""
		insert newNode after node:
			node <> oldNext
			node < newNode oldNext  
			node < newNode > oldNext
			node < newNode <> oldNext
			node <> newNode <> oldNext
		"""
		newNode.previous = node
		if node.next is None:
			self.tail = newNode
		else:
			newNode.next = node.next
			node.next.previous = newNode
		node.next = newNode
	
	def insertBefore(self,node,newNode):
		"""
		insert newNoe before node:
			oldPrev <> node
			oldPrev newNode > node
			oldPrev < newNode > node
			oldPrev <> newNode > node
			oldPrev <> newNode <> node
		"""
		newNode.next = node
		if node.previous is None:
			self.head = newNode
		else:
			newNode.previous = node.previous
			node.previous.next = newNode
		node.previous = newNode

	def insertBeginning(self,data):
		if data is not type(Node):
			n = Node.Node(data)
		else:
			n = data
		if self.head is None:
			if self.tail is None:
				self.head = n
				n.next = self.tail
				n.previous = self.head
		else:
			self.insertBefore(self.head,n)

	def insertEnd(self,data):
		if data is not type(Node):
			newNode = Node.Node(data)
		else:
			newNode = data
		if self.tail is None:
			self.insertBeginning(newNode)
		else:
			self.insertAfter(self.tail, newNode)
	
	def insertNode(self,data,Forward=True):
		if forward:
			if self.head is None:
				insertBeginning(data)
			else:
				n = Node.Node(data)
				temp = self.head
				while temp.next is not None:
					temp = temp.next
				temp.next = n
				n.previous = n

	def removeNode(self,n):
		if n.previous is None:
			self.head = n.next
		else:
			n.previous.next = n.next
		if n.next is None:
			self.tail = n.previous
		else:
			n.next.previous = n.previous
		n.remove
		
