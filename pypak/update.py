import urllib.request
import os.path
import os

version_url = "https://github.com/Ewpratten/pypak/raw/master/pypak/__main__.py"

def update(version):
	print(f"Updating pypak to version: {version}")
	
	if not os.path.isfile("./pypak"):
		print("Detected non-standard installation of pypak...\nInstalling to alternate path")
		install_path = "./pypak-update"
	else:
		install_path = "./pypak"
	
	print("Downloading from GitHub")
	os.system(f"curl https://github.com/Ewpratten/pypak/releases/download/{version}/pypak > {install_path}")
	
	

def checkUpdates(version):
	print("Checking for updates")
	
	new_version =  urllib.request.urlopen(version_url).read().decode().split('"')[1]
	if version == new_version:
		print("pypak up to date")
		return
	update(new_version)