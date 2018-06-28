

import os
import shutil
from os import walk

files = []
splitFiles = []
fileExtensions = []

for (dirpath, dirnames, filenames) in walk(os.getcwd()):
    files.extend(filenames)
    break

for x in files:
    splitFiles.extend(x.split('.'))

for y in range(len(splitFiles)):
    if (y%2==1):
        fileExtensions.append(splitFiles[y])
        fileSet = set(fileExtensions)
        fileExtensions = list(fileSet)

for z in fileExtensions:
    if not os.path.exists(z):
        os.makedirs(z)

for i in range(len(files)):
    print(files[i])
    for j in fileExtensions:
        if (j=="ini"):
            continue
        elif files[i].endswith(j):
            print("true")
            shutil.move(files[i],j)
