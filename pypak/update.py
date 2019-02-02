import urllib.request

version_url = "https://raw.githubusercontent.com/Ewpratten/pypak/master/pypak/version.txt"

def update(version):
	print(f"Updating pypak to version: {version}")

def checkUpdates(version):
	print("Checking for updates")
	new_version =  urllib.request.urlopen(version_url).read().decode()
	if version == new_version:
		print("pypak up to date")
		return
	update(new_version)