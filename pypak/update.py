import urllib.request
import os.path
import os

version_url = "https://api.github.com/repos/ewpratten/pypak/releases/latest"

def toDict(json):
	return eval(json.replace("false", "False").replace("true", "True").replace('null', "None"))

def update(version):
	print(f"Updating pypak to version: {version}")
	
	if not os.path.isfile("./pypak"):
		print("Detected non-standard installation of pypak...\nInstalling to alternate path")
		install_path = "./pypak-update"
	else:
		install_path = "./pypak"
	
	print("Downloading from GitHub")
	os.system(f"curl -L -s https://github.com/Ewpratten/pypak/releases/download/{version}/pypak > {install_path}")
	
	

def checkUpdates(version):
	print("Checking for updates")
	
	new_version =  toDict(urllib.request.urlopen(version_url).read().decode())["tag_name"]
	if version == new_version:
		print("pypak up to date")
		return
	update(new_version)