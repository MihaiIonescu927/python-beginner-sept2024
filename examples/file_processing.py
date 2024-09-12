import os

# current working directory
cwd = os.getcwd()
print(cwd)

# using file name for files at current working directory
f = open("imports.py", "r")
print(f.read())
f.close()

# using absolute path for files at different location
f = open("/Users/iulia/PycharmProjects/python-beginner-sept2024/"
         "requirements.txt", "r")
print(f.read())
f.close()

# using relative path for files at different location
f = open("../requirements.txt", "r")
print(f.read())
f.close()

# without hardcoding the path (more portable)
# https://docs.python.org/3/library/os.path.html
# https://docs.python.org/3/library/pathlib.html
project_path = os.path.dirname(cwd)
requirements_path = os.path.join(project_path, "requirements.txt")
f = open(requirements_path, "r")
print(f.read())
f.close()
