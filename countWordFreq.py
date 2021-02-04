#import default package
import sys
import subprocess
import importlib.util
from os import listdir
import csv

#import function files
import listAllFiles

def count(target, split, output):
	#list all target files
	targets_dir_path = target
	targets_files = listAllFiles.listFiles(targets_dir_path, 1)

	#list all text files
	text_dir_path = split
	text_files = listAllFiles.listFiles(text_dir_path, 1)

	#output path
	output_dir_path = output



	#process
	for tg_name in targets_files:			#for every file in target dir
		field=['Company', 'Year', 'Total']
		#result
		result = []
		tg = targets_dir_path+tg_name
		tgn = tg_name.split('_')[0]
		with open(tg, 'r', encoding='utf-8') as t:
			temp=t.read()
			words=temp.split(',')
			#field extend
			field.extend(words)
			for te_name in text_files:	#for every file in text dir
				#dictionary that stores result
				dic_result = {'Company':'', 'Year':'', 'Total' :0}
				te = text_dir_path+te_name
				info = te.split('_')
				dic_result['Company']=str(info[1])
				dic_result['Year']=str(info[2][:-4])
				with open(te, 'r', encoding='utf-8') as i:
					contents=i.read()
					content=contents.split('|')
					for word in words:
						dic_result[word]=content.count(word)
						dic_result['Total']+=content.count(word)
				result.append(dic_result)
			ot_name = tgn+'_'+str(info[2][:-4])+'.csv'
			with open(output_dir_path+ot_name, 'w', encoding='utf-8') as o:
				d = csv.DictWriter(o, field)
				d.writeheader()
				for r in result:
					d.writerow(r)
	print('done!')
