#  os module
import os
# Create a directory
try:
    os.mkdir("mydir")
except Exception as e:
    print(e)
    
# Print current working directory
print(os.getcwd())
os.chdir("../")
print(os.getcwd())
os.chdir("./Data processing")

# List current working directory
print(os.listdir("./"))

# scan all dirs and sub dirs topdown by default, returns a generator object
"""
For each directory in the directory tree rooted at top (including top
    itself, but excluding '.' and '..'), yields a 3-tuple

        dirpath, dirnames, filenames
"""
for d in os.walk(os.getcwd(), topdown=False):
    print(d)

# remove an empty directory
try:
    os.rmdir("./mydir")
except Exception as e:
    print(e)

# os.path - methods
print(dir(os.path))

# sys module - for manipulating python runtime environment
import sys

# command line arguments as argument vector
print(sys.argv)
# version
print(sys.version)
# max int
print(sys.maxsize)
# search path for aall python modules
print(sys.path)
# Use to safely exit in case of exception
sys.exit()
