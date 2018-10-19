from collections import deque
import time
class MinQueue:
	def __init__(self,p_size):
		self.size = p_size
		self.deque=deque()
		self.timeDeque=deque()

	def peek(self,p_deque):
		val = p_deque.pop()
		p_deque.append(val)
		return val

	def peekleft(self ,p_deque):
		val = p_deque.popleft()
		p_deque.appendleft(val)
		return val
	def push(self,p_value):
		self.updateTime()
		while  len(self.deque) !=0 and self.peek(self.deque) > p_value:
			self.deque.pop();
			self.timeDeque.pop();
		self.deque.append(p_value)
		self.timeDeque.append((int)(time.time()))
	def printMessage(self):
		size = len(self.deque)
		index=0
		while( index<size):
			value = self.deque.popleft()
			self.deque.append(value)
			value1 = self.timeDeque.popleft()
			self.timeDeque.append(value1)
			print(value,1)
			index = index+1
	def updateTime(self):
		timeNow = (int)(time.time())
		# print ('timeNow: '+str(timeNow))
		# if (len(self.deque) !=0):
		# 	print('time: '+str(self.peek(self.timeDeque)))
		while  len(self.deque) !=0 and timeNow-self.peekleft(self.timeDeque) >3:
			self.deque.popleft()
			self.timeDeque.popleft()

if __name__=='__main__':
	obj = MinQueue(10)
	obj.push(3)
	time.sleep(1)
	obj.push(1)
	time.sleep(1)
	obj.push(4)
	time.sleep(1)
	obj.push(5)
	time.sleep(1)
	obj.push(6)
	obj.printMessage()
