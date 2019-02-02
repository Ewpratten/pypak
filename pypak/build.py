import os.path
import os

import zipapp

def zipFolder(path, name):
	print("Packing project")
	zipapp.create_archive(path, f"./build/pypak/{name}", compressed=True)
	print("Done")

def mkFolder(project_name):
	print("Creating build directory")
	os.system("mkdir ./build 2> /dev/null")
	os.system("mkdir ./build/pypak 2> /dev/null")
	
	print("Detecting previous builds")
	
	if os.path.isfile(f"./build/pypak/{project_name}"):
		print("Detected previous build")
		print("Removing old build")
		os.system(f"rm -rf ./build/pypak/{project_name}")
		print("Done")
	else:
		print("None found")
	
	