#1

import os
def create_python_script(filename):
  comments = "# Start of a new Python program"
  with open(filename, 'w') as file:
    file.write(comments)
  filesize = os.path.getsize(filename)
  return(filesize)

print(create_python_script("program.py"))


#2

import os

def new_directory(directory, filename):
  # Before creating a new directory, check to see if it already exists
  fullname = os.path.join(directory, filename)
  os.path.isdir(directory) 
  # Create the new file inside of the new directory
  os.mkdir(directory)
  file = open(fullname, 'x')
  file.close()
  # Return the list of files in the new directory
  return os.listdir(directory)
print(new_directory("PythonPrograms", "script.py"))
