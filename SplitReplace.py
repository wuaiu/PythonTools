originSplit = ","
toSplit = "%7c"
with open('testout.txt','w') as out:
	with open('test.txt', 'r') as f:
		seq = ("a", "b", "c")
		for line in f.readlines():
			vec = line.split(originSplit)
			if (len(vec)!=0):
				vec[len(vec)-1] =vec[len(vec)-1].strip('\n')
			print(vec)
			str1=''
			for strTemp in vec:
				str1 +=strTemp+toSplit;
			# str1 = ','join(seq)
			# ' '.join(str(x) for x in floatVec)
			str1=str1[:-1*len(toSplit)]
			print(str1)
			out.write(str1)