#!Python3
class Vertex:
	def __init__(self,key):
		self.id = key
		self.neighbors = {}
		self.distance = 0
		self.predecessor = None
		self.color = 'white'

	def addNeighbor(self,nbr,weight=0):
		self.neighbors[nbr] = weight
	def __str__(self):
		return str(self.id) + 'connectedTo: '+ str([x.id for x in self.neighbors])
	def __repr__(self):
		return str(self.id)	
	def setColor(self,c):
		self.color = c

	def getColor(self):
		return self.color

	def setDistance(self,d):
		self.distance = d

	def getDistance(self):
		return self.distance
	def setPred(self,v):
		self.predecessor = v
	def getPred(self):
		return self.predecessor
	def getNeighbors(self):
		return self.neighbors.keys()
	def getId(self):
		return self.id
	def getWeight(self,nbr):
		return self.neighbors[nbr]

