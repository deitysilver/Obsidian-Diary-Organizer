from os import listdir
from os.path import isfile, join
import re

file_name = "!Diary Hub.md"

f = open(file_name, "r")
current_diary = f.read().split("\n")
cleaned_strings = [re.sub(r':.*$', '', s) for s in current_diary]
f.close()

mypath = "./"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
onlyfiles.pop()
onlyfiles.pop(0)

for i in onlyfiles:
    for j in cleaned_strings:
        if (re.sub(".md", "", i) == j):
            checker = True
            break
        else:
            checker = False
            
    i = re.sub(".md", "", i)
    if checker == False:
        with open(file_name, "a") as myfile:
            myfile.write(f'\n{i}: [[{i}]]')
