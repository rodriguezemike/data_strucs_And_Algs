#!Python3
class Node(object):
	def __init__(self,data):
		self.__data = data
		self.__next = None
		self.__previous = None
	def __str__(self):
		return str(self.data)
	def __repr__(self):
		return str("(Previous: " + str(self.previous) + ") (Data: "+ str(self.data) + ") (Next: " + str(self.next)+")") 
	
	@property
	def data(self):
		return self.__data
	@property
	def next(self):
		return self.__next
	@property
	def previous(self):
		return self.__previous
 
	@data.setter
	def data(self,newData):
		self.__data = newData

	@next.setter
	def next(self,n):
		self.__next = n

	@previous.setter
	def previous(self,n):
		self.__previous = n

	def remove(self):		
		self.data = None
		self.next = None
		self.previous = None

