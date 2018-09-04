
import random
with open('indexspl.txt','w') as out:
	with open('hash', 'r') as f:
		isFirst = True
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
				sum1=0
				for num in floatVec:
					# print(num)
					sum1=sum1 + num
					pass
				print(sum1)
				

				# for i in range(28):
				# 	randomnum = random.choice((1.0, -1.0))
				# 	# print(randomnum)
				# 	floatVec.append(randomnum)
				# print(len(floatVec))
				# strResult =' '.join(str(x) for x in floatVec)
				# print(strResult)
				# print(hashIdNum)
				# print(str1)
				# print(bandNum)
				# print(numPerBand)
				# print('('+str(hashIdNum) + ", ' "+strResult+" ' ," + str(bandNum)+' ,'+str(numPerBand)+' ,'+str(1)+'),'+'\n')
				# out.write('('+str(hashIdNum) + ", ' "+strResult+" ' ," + str(bandNum)+' ,'+str(numPerBand)+' ,'+str(1)+'),'+'\n')
				# isFirst = False
	    # print(f.read())
	# print(f.closed)