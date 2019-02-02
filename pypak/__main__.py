version = "0.0.2"
# line above is parsed over http by the update script. Do not move it

from update import update, checkUpdates
import sys

if len(sys.argv) != 2:
	print("Usage: pypak <source folder>")
	exit(1)

# Check for updates
checkUpdates(version)

project_path = sys.argv[1]

project_name = project_path.split("/")
if project_name[len(project_name) - 1] == "":
	project_name = project_name[len(project_name) - 2]
else:
	project_name = project_name[len(project_name) - 1]

print(f"Detected project name: {project_name}")