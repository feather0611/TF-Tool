import sys

def clean(list):
	for i in range(len(list)):
		if ' ' in list[i]:
			list[i] = list[i].replace(' ','')
		if '\t' in list[i]:
			list[i] = list[i].replace('\t','')
	return list




