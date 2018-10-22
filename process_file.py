import os
import csv
def file_name(file_dir):   
	L=[]   
	for root, dirs, files in os.walk(file_dir):  
		for file in files:  
			if os.path.splitext(file)[1] == '.csv' and file!='result.csv':  
				L.append(os.path.join(root, file))  
	return L 

# print(file_name('/Users/tianjunjie02/python_test'))
# print(os.getcwd())

if __name__=='__main__':
	pwdPath = os.getcwd()
	files = file_name(pwdPath)
	print("current path : " +pwdPath)
	print(".csv file amount : " +str(len(files)))
	with open('result.csv','w')as out:
		for fileName in files:
			with open(fileName,'r') as fin:
				# csv_reader_lines = csv.reader(fin)
				for one_line in fin:
					out.write(one_line)
					# print(one_line)
			pass
