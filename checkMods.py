#import default package
import sys
import subprocess
import importlib.util
from os import listdir


#import function files
import checkPackage
import splitWords

#Pre Check installed package
if(checkPackage.preCheck()!=0):
	print("Error in import package!")
	sys.exit(0)

#Split Words
splitWords.split()

