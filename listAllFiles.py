#import default package
import sys
import subprocess
import importlib.util
import os
from os import listdir


def listFiles(path, mode):
	files = sorted(listdir(path))
	if '.DS_Store' in files:
		files.remove('.DS_Store')
	if (mode == 1):
		fs=files
		for f in fs:
			if os.path.isdir(path+'/'+f):
				files.remove(f)
	return files
