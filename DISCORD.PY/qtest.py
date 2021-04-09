import queue
from collections import deque

class Queue:
	def __init__(self):
		self.buffer = deque()
		
	def enqueue(self, val):
		self.buffer.appendleft(val)
		
	def dequeue(self):
		return self.buffer.pop()
	
	def is_empty(self):
		return len(self.buffer)==0		
	def size(self):
		return len(self.buffer)
		
		
pq = Queue()

pq.enqueue('test')
pq.enqueue('hello dere')
print(pq.buffer)
#print(pq.buffer)
#print(pq.dequeue())
#print(pq.size())
pq.dequeue()
print(pq.buffer)

