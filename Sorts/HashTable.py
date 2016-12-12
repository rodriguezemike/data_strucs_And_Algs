#!Python3 

class HashTable:
	def __init__(self):
		self.size = 11
		self.slots = [None] * self.size
		self.data = [None] * self.size

	def __getitem__(self,key):
		return self.get(key)
	
	def __setitem__(self,key,data):
		self.put(key,data)
	
	def put(self,key,data):
		hashValue = self.hashFunction(key,len(self.slots))

		if self.slots[hashValue] == None:
			self.slots[hashValue] = key
			self.data[hashValue] = data
			self.size += 1
		else:
			if self.slots[hashValue] == key:
				self.data[hashValue] = data
			else:
				nextSlot = self.rehash(hashValue,len(self.slots))
				while self.slots[nextSlot] != None and self.slots[nextSlot] != key:
					nextSlot = self.rehash(nextSlot,self.size)
			
				if self.slots[nextSlot] == None:
					self.slots[nextSlot] = key
					self.data[nextSlot] = data
					self.size += 1
				else:
					self.data[nextSlot] = data # replace the data
	
	def get(self,key):
		startSlot = self.hashFunction(key,len(self.slots))
		
		data = None
		stop = False
		found = False
		position = startSlot
		while self.slots[position] != None and not found and not stop:
			if self.slots[position] == key:
				found = True
				data = self.data[position]
			else:
				position = self.rehash(position,len(self.slots))
				if position == startslot:
					stop = True
		return data
	def hashFunction(self,key,size):
		return key%size
	
	def rehash(self,oldHash,size):
		return (oldHash+1) % size
