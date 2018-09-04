import random
import numpy as np
import matplotlib.pyplot as plt

def draw_hist(myList,Title,Xlabel,Ylabel,Xmin,Xmax,Ymin,Ymax):
	plt.hist(myList,100)
	plt.xlabel(Xlabel)
	plt.xlim(Xmin,Xmax)
	plt.ylabel(Ylabel)
	plt.ylim(Ymin,Ymax)
	plt.title(Title)
	plt.show()

with open('hash', 'r') as f:
	isFirst = True
	vec = []
	for line in f.readlines():
		if isFirst:
			# print(line)
			index1 = line.index('[')
			index2 = line.index(']')
			hashIdNumStr = line[0:index1]
			hashIdNumStr.strip()
			hashIdNum=int(hashIdNumStr)
			str1 = line[index1+1:index2]
			str2 = line[index2+1:]
			strvec= str2.strip().split()
			# print(strvec)
			bandNum = int(strvec[0])
			numPerBand = int(strvec[1])
			
			floatVec = [float(x) for x in str1.strip().split()]
			# floatVec = []
			for num in floatVec:
				pass

			for i in range(28):
				randomnum = random.choice((1.0, -1.0))
				# print(randomnum)
				floatVec.append(randomnum)
			vec.append(floatVec)


	s=[]
	s1=[]
	for i in range(len(vec)):
		for j in range(len(vec)):
			if(i!=j):
				sum1 =0.0
				for k in range(len(vec[i])):
					sum1+=vec[i][k]*vec[j][k]
				s.append(sum1/128)
					# print(sum1/128)
	for j in range(len(vec)):
		if(0!=j):
			sum1 =0.0
			sum2=0.0
			for k in range(len(vec[0])):
				sum1+=vec[0][k]*vec[j][k]
				sum2+=vec[0][k]*vec[0][k]
			s1.append(sum1/128)
			print(sum2)
	
	draw_hist(s,'1','x','y',-1,1,0,10000)
	# draw_hist(s1,'2','x','y',-1,1,0,40)
	print(s1)








