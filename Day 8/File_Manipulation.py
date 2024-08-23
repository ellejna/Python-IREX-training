# Number 1: How to open a file (1)
file_path = ("example.txt")
file = open(file_path, "r")
content = file.read()
print(content)
file.close()

# Number two: How to open the file (2)

file_path = ("example.txt")
with open(file_path, "r") as file:
    content = file.read()
    print(content)
file.close()

#Number three: Write on the files
with open(file_path, "w") as file:
    file.write("Hello world")
file.close()

# Find file
import os
if os.path.exists(file_path):
    print("Found it!!")