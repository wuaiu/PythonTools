
class TopK_Max:
	def __init__(self,p_size):
		self.k = p_size
		self.minHeap = MinHeap(self.k)
	def add(self,p_value):
		if (self.minHeap.getElement(1) < p_value):
			self.minHeap.heap_pop()
			self.minHeap.heap_push(p_value)
		print(self.minHeap.list1)

	def min(self):
		index=1
		while self.minHeap.getElement(index)==-1000:
			index = index+1
		return self.minHeap.getElement(index)

class MinHeap:
	def __init__(self,p_size):
		self.k=p_size
		self.list1=[-1000]*self.k;

	def top(self):
		return self.getElement(1);
		pass

	def getElement(self,p_index):
		return self.list1[p_index-1]
	def setElement(self,p_index,p_value):
		self.list1[p_index-1]=p_value

	def heap_pop(self):
		indexStart = 1
		index1=0
		index2=0
		val = self.getElement(self.k)
		while True:
			index1 = indexStart*2
			index2 = index1+1
			if index1 > self.k:
				break
			if index2 == self.k+1 or self.getElement(index1) < self.getElement(index2):
				if val < self.getElement(index1):
					break
				self.setElement(indexStart,self.getElement(index1))
				indexStart = index1
			else:
				if val < self.getElement(index2):
					break
				self.setElement(indexStart,self.getElement(index2))
				indexStart = index2
		self.setElement(indexStart,self.getElement(self.k))
		pass

	def heap_push(self,val):
		indexStart = self.k
		i_father = 0
		while  indexStart > 1:
			i_father = indexStart/2
			if (val >= self.getElement(i_father)):
				break
			self.setElement(indexStart,self.getElement(i_father))
			indexStart=i_father
			pass
		self.setElement(indexStart,val)
		pass
class TopK_Min():
	def __init__(self,p_size):
		self.k = p_size
		self.maxHeap = MaxHeap(self.k)
	def add(self,p_value):
		if (self.maxHeap.getElement(1) > p_value):
			self.maxHeap.heap_pop()
			self.maxHeap.heap_push(p_value)
		print(self.maxHeap.list1)

	def min(self):
		index=1
		while self.maxHeap.getElement(index)==1000:
			index = index+1
		return self.maxHeap.getElement(index)

class MaxHeap:
	def __init__(self,p_size):
		self.k=p_size
		self.list1=[1000]*self.k;

	def top(self):
		return self.getElement(1);
		pass

	def getElement(self,p_index):
		return self.list1[p_index-1]
	def setElement(self,p_index,p_value):
		self.list1[p_index-1]=p_value

	def heap_pop(self):
		indexStart = 1
		index1=0
		index2=0
		val = self.getElement(self.k)
		while True:
			index1 = indexStart*2
			index2 = index1+1
			if index1 > self.k:
				break
			if index2 == self.k+1 or self.getElement(index1) > self.getElement(index2):
				if val > self.getElement(index1):
					break
				self.setElement(indexStart,self.getElement(index1))
				indexStart = index1
			else:
				if val > self.getElement(index2):
					break
				self.setElement(indexStart,self.getElement(index2))
				indexStart = index2
		self.setElement(indexStart,self.getElement(self.k))
		pass

	def heap_push(self,val):
		indexStart = self.k
		i_father = 0
		while  indexStart > 1:
			i_father = indexStart/2
			if (val <= self.getElement(i_father)):
				break
			self.setElement(indexStart,self.getElement(i_father))
			indexStart=i_father
			pass
		self.setElement(indexStart,val)
		pass

if __name__=='__main__':
	obj = TopK_Min(5)
	obj.add(-1)
	obj.add(2)
	obj.add(-1.1)
	obj.add(5)
	# obj.add(6)
	# obj.add(7)
	# obj.add(9)
	print(obj.min())
