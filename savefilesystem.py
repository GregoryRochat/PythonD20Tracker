import os

def readfile(filename):
    if checkfile(filename):
        filestr =  "savefiles\\" + filename + ".txt"
        file = open(filestr, "r")
        return file
    else:
        return 0

def createfile(filename):
    filestr =  "savefiles\\" + filename + ".txt"
    file = open(filestr,"w")
    file.close()

def checkfile(filename):
    filestr = "savefiles\\" + filename + ".txt"
    try:
        file = open(filestr,"r")
        file.close()
        return True
    except FileNotFoundError:
        return False

def deletefile(filename):
    filestr =  "savefiles\\" + filename + ".txt"
    try:
        os.remove(filestr)
        return True
    except FileNotFoundError:
        return False

def writetofile(filename, txt):
    filestr = "savefiles\\" + filename + ".txt"
    try:
        file = open(filestr, "a")
        file.write(txt)
        file.close()
    except FileNotFoundError:
        return False
    return 0

def listallfiles():
    print(os.listdir("savefiles\\"))



lst = os.listdir()
for x in lst:
    if "py" in x:
        print(x)
