#!python3

from Graph import Graph
from Vertex import Vertex
from Queue import Queue

def bfs(g,start):
	start.setDistance(0)
	start.setPred(0)
	vertQueue = Queue()
	vertQueue.enqueue(start)
	while(vertQueue.size() > 0):
		currentVert = vertQueue.dequeue()
		for nbr in currentVert.getNeighbors():
			if(nbr.getColor() == 'white'):
				nbr.setColor('gray')
				nbr.setDistance(currentVert.getDistance() + 1)
				nbr.setPred(currentVert)
				vertQueue.enqueue(nbr)
		currentVert.setColor('black')

def traverse(y):
	x = y
	while(x.getPred()):
		print(x.getId())
		x = x.getPred()
	print(x.getId())

