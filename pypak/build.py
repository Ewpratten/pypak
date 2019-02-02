import os.path
import os.system

def zipFolder(path)
	print("Packing project")

def mkFolder(project_name):
	print("Trying to create folder")
	os.system("mkdir ./build")
	os.system("mkdir ./build/pypak")
	
	print("Detecting previous builds")
	
	if os.path.isfile(f"./build/pypak/{project_name}"):
		print("Detected previous build")
		print("Removing old build")
		os.system(f"rm -rf ./build/pypak/{project_name}")
		print("Done")
	
	