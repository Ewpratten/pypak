import urllib

version_url = "https://raw.githubusercontent.com/Ewpratten/pypak/master/pypak/version.txt"

def update(version):
	print(f"Updating pypak to version: {version}")

def checkUpdates():
	print("Checking for updates")
	version =  urllib.request.urlopen(version_url)
	print(version)