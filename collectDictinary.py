import sys
import arrayClean as ac
import listAllFiles as laf


def collect(res_path):
	result = []
	files = laf.listFiles(res_path, 1)
	for file in files:
		with open(res_path+'/'+file , 'r', encoding='utf-8') as f:
			temp = f.read().split(',')
			temp=ac.clean(temp)
			result=result+temp
	with open('res/myDictionary.txt', 'w', encoding='utf-8') as o:
		for i in range(len(result)):
			o.write(result[i])
			if i != len(result)-1:
				o.write('\n')

