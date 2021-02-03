import sys
import subprocess
import importlib.util
from os import listdir

def preCheck():
	names = ['csv','jieba','jieba.analyse','numpy']
	for name in names:

		if name in sys.modules:
		    print(f'{name!r} already in sys.modules')
		elif (spec := importlib.util.find_spec(name)) is not None:
		    # If you choose to perform the actual import ...
		    module = importlib.util.module_from_spec(spec)
		    sys.modules[name] = module
		    spec.loader.exec_module(module)
		    print(f"{name!r} has been imported")
		else:
		    print(f"can't find the {name!r} module")
		    install(name)

	return 0

def install(package):
	subprocess.check_call([sys.executable, "-m", "pip", "install", package])
