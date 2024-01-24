class ArrayQueue:
	def __init__(self, size):
		self.Arr_size =size
		self.queue =[None]*size
		self.rear=0
		self.front =0
	def size(self):
		return self.rear - self.front
	def is_full(self):
		return self.rear-self.front ==self.Arr_size
	def enqueue(self, val):
		
		if self.is_full()!=True:
			self.queue[(self.rear)%self.Arr_size] =val
			self.rear +=1
	
		else:
			raise Exception("Not enough space")
	
	def remove(self):

		if self.front==self.rear:
			raise Exception("empty queue")
		val =self.queue[self.front%self.Arr_size]
		self.front =self.front+1
		return val
		
	def is_empty(self):
		return self.rear-self.front==0
	def display(self):
	
		if self.front==self.rear:
			raise Exception('Empty List')
		for i in range(self.front, self.rear):
		    print(self.queue[i%self.Arr_size], end=" ")
		
		
	

def main():
	a =ArrayQueue(4)
	a.enqueue(10)
	a.enqueue(20)
	a.enqueue(30)
	a.enqueue(40)
	a.remove()

	a.enqueue(20000)
	

	
	a.display()
	
	


main()