'''
    File name: fileSorter.py
    Author: Trevor Gahl
    Date created: 6/27/2018
    Date last modified: 6/27/2018
    Python Version: 3.6
'''

import os
import shutil
from os import walk


def fileSort():

    files = []
    splitFiles = []
    fileExtensions = []

    # Gather list of filenames in current working directory
    for (dirpath, dirnames, filenames) in walk(os.getcwd()):
        files.extend(filenames)
        break

    # Split file extensions off from file names
    for x in files:
        # Prevent erroneous folder creation by ensuring validity of file extension
        if (x.count(".")>1):
            print("Invalid file name, multiple instances of '.' in file name")
            print(x)
            continue
        else:
            splitFiles.extend(x.split('.'))

    # Create a list of file extensions based on extensions in directory
    for y in range(len(splitFiles)):
        if (y%2==1):
            fileExtensions.append(splitFiles[y])
            fileSet = set(fileExtensions)
            fileExtensions = list(fileSet)

    # Check if folder for desired file extension exists, if not create it
    for z in fileExtensions:
        if (z == "ini"):
            continue
        elif not os.path.exists(z):
            os.makedirs(z)

    # Iterate through original list of files and move to corresponding folders
    for i in range(len(files)):
        for j in fileExtensions:
            if (j=="ini"):
                continue
            elif files[i].endswith(j):
                try:
                    shutil.move(files[i],j)
                except Exception as e:
                    print("File already exists: ")
                    print(files[i])
                    shutil.copy(files[i],j)
                    os.remove(files[i])



fileSort()
