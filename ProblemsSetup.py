import os 

# Path of the app
PACKAGE_PATH = os.path.join(os.getcwd(), "..//")
# List with the names of the folders in the folder specified by PACKAGE_PATH
folders = os.listdir(PACKAGE_PATH)

# Print all folders in the path
for folder in folders:
	# Only print if it's a folder and not a file
	if not os.path.isfile(folder):
		print(folder)

# Ask for the folder where the problem folder will be made
index = int(input("Select the folder where you want to setup a problem: "))
# As well as the name of the problem
name = input("Name of the problem: ")

# Paths to the problem folder, python's solution files, and text file
# for the problem link
problem_path = os.path.join(PACKAGE_PATH, folders[index-1], name)
solution1_file_path = os.path.join(problem_path, "Solution1.py")
solution2_file_path = os.path.join(problem_path, "Solution2.py")
problem_link_file_path = os.path.join(problem_path, "ProblemLink.txt")

# If the folder doesn't exist, we create it
try:
	os.mkdir(problem_path)
except:
	pass

# Open the python and text files and write what is needed
with open(solution1_file_path, 'w') as f:
    f.write("# Neetcode.io solution\n\n")
    f.write("# Time complexity: O()\n")
    f.write("# Space complexity: O()\n\n\n\n")
    f.write("print(function()) # \n")
    f.write("print(function()) # \n")
    f.write("print(function()) # ")

with open(solution2_file_path, 'w') as f:
    f.write("# Time complexity: O()\n")
    f.write("# Space complexity: O()\n\n\n\n")
    f.write("print(function()) # \n")
    f.write("print(function()) # \n")
    f.write("print(function()) # ")

with open(problem_link_file_path, 'w') as f:
	name = name.replace(" ", "-")
	name = name.lower()
	f.write(f"https://leetcode.com/problems/{name}")

# Show the file in the file explorer 
os.startfile(problem_path)