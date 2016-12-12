#!python3
from Node import Node

class UnordredListError(Exception):pass

class UnorderedList:
	def __init__(self):
		self.head = None

	def __getitem__(self,index):
		current = self.head
		for i in range(index):
			if current!= None:
				current = current.getNext()
			else:
				return None
		return current.getData()

	def isEmpty(self):
		return self.head is None

	def add(self,item):
		temp = Node(item)
		temp.setNext(self.head)
		self.head = temp

	def size(self):
		current = self.head
		count = 0
		while current != None:
			count += 1
			current = current.getNext()
		return count

	def search(self,item):
		current = self.head
		found = False
		while current != None and not found:
			if current.getData() == item:
				found = True
			else:
				current = current.getNext()
		return found

	def remove(self,item):
		current = self.head
		previous = None
		found = False
		if self.head.getData() == item:
			found = True
			self.head = current.getNext()
			current.remove()
			return found
		previous = current
		current = current.getNext()
		while not found and current != None:
			if current.getData() == item:
				found = True
				previous.setNext(current.getNext())
				current.remove()
			else:
				previous = current
				current = current.getNext()
		return found
	#add places the item in the first place of the list, append to the last
	def append(self,item):
		current = self.head
		while current.getNext() != None:
			current = current.getNext()
		current.setNext(Node(item))
		return True
	def tail(self):
		current = self.head
		while current.getNext() !=None:
			current = current.getNext()
		return current.getData()
	def index(self,n):
		i = 0
		current = self.head
		while current!= None:
			if current.getData() == n:
				return i
			else:
				i+=1
				current = current.getNext()
		return -1

	def insert(self,i,n):
		current = self.head
		if i > self.size():
			print("Chose a position outside the list. Default add.")
			self.add(i)
			return True
		for j in range(i):
			current = current.getNext()
		toPlace = Node(n)
		toPlace.next = current.getNext()
		current.next = toplace
		return True
	def pop_pos(self,pos):
		previous = None
		current = self.head 
		if pos > self.size():
			#raise UnorderedListError("Trying to pop a position not in the list")
		print("Trying to pop an object outside the list")
		return None
		for i in range(pos):
			previous = current
			current = current.getNext()
		previous.next = current.getNext()
		current.next = None
		return current.getData()

	def pop(self):
		previous = None
		current = self.head
		while current.getNext()!= None:
			previous = current
			current = current.getNext()
		previous.next = None
		return current.getData()


