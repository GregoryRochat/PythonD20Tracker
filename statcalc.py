import random
import math
import os







#d20 throw simulator that throws everything into a list
#------------------------------------------------------------------------------------------------------------------------------------------------------------------
lst = []
lst2 = []
lst3 = []
for x in range(1,21):
    lst2.append([x,0])

for x in range(0,32):
    b = random.randint(1,20)
    lst.append(b)
    lst2[b-1][1] += 1

#------------------------------------------------------------------------------------------------------------------------------------------------------------------


#d20 file loader that puts a file with numbers into a list
#------------------------------------------------------------------------------------------------------------------------------------------------------------------

def d20rollsfilewriter(lst,filenamestr):
    file = open(filenamestr, 'w')
    for x in range(0,len(lst)):
        if x == (len(lst)-1):
            file.write(str(lst[x]))
        else:
            file.write(str(lst[x]) + ",")
    return 0

def d20rollsfilewriterrandomizer(lst,filenamestr):
    file = open(filenamestr, 'w')
    file.write("bla,")
    for x in range(0,len(lst)):
        if x == (len(lst)-1):
            file.write(str(lst[x]))
        else:
            if (random.randint(1,4) == 3):
                file.write(" ")
            file.write(str(lst[x]) + ",")
    return 0


def d20rollsfilereader(lst,filenamestr):
    file = open(filenamestr, 'r')
    x = file.read()
    x = x.replace(" ",'')
    while not x[0].isdigit():
        x = x[1:]
    print(x)
    number = 0
    for s in range(0,len(x)):
        if (x[s].isdigit()):
            number = number * 10 + int(x[s])
            if s == (len(x) -1):
                lst.append(number)
        else:
            lst.append(number)
            number = 0
    return lst

#------------------------------------------------------------------------------------------------------------------------------------------------------------------

#savefileforD20names writer and loader
#------------------------------------------------------------------------------------------------------------------------------------------------------------------
def readnamessavefile():
    file = open("d20namessavefile.txt","r")
    x = file.readlines()
    for line in x:
        words = line.split(',')
        print(words)

def addnamestonamesavefile(strname):
    try:
        file = open("d20namessavefile.text", "r")
    except
#actual d20 list operators
#------------------------------------------------------------------------------------------------------------------------------------------------------------------
def findD20mode(lst2):
    "finds the mode in a list of numbers and returns a list of that/those modes"
    highest = 0
    mode = []
    for x in lst2:
        if(x[1] > highest):
            highest = x[1]
    for x in lst2:
        if(highest == x[1]):
            mode.append(x[0])
    return mode

def findmedian(lst2):
    "finds the median of a list in list and returns it as a list"
    templst = []
    for x in lst2:
        templst.append(x[0])
    templst.sort()
    medianlst = []
    a = 0
    b = (len(templst)-1)
    while(a <= b):
        if(templst[a] == templst[b]):
            medianlst.append(templst[a])
        a+=1
        b-=1

    if(len(medianlst) == 0):
        medianlst.append(templst[b])
        medianlst.append(templst[a])
    return medianlst

def leastthrownd20side(lst2):
    "returns the least thrown numbers from d20 list"
    lowest = int(lst2[0][1])
    minmode = []
    for x in lst2:
        if (x[1] < lowest):
            lowest = x[1]
    for x in lst2:
        if (lowest == x[1]):
            minmode.append(x[0])
    return minmode

def percentageD20numberscalc(lst2):
    "calculate the percentages of numbers thrown on a dice from a list and return those results as a list"
    percentagelst = []
    for x in lst2:
        percentagethrown = round(((x[1] / len(lst2)) * 100),2)
        #print(str(x[0]) + ": " + str(percentagethrown) + "%")
        percentagelst.append([x[0], percentagethrown])
    return percentagelst

def longestd20repeat(lst):
    "returns a nested list with the first entry showing how many repeats the longest repeated d20 number had\
    and the second entry the numbers that repeated that many times"
    repeatlst = []
    high = 0
    current = 0
    for x in range(0,len(lst)):
        if not (x+1 == len(lst)):
            if(lst[x] == lst[x+1]):
                if(current == 0):
                    current = 2
                else:
                    current +=1
                if (current == high):
                    repeatlst.append(lst[x])
                elif (current > high):
                    repeatlst.clear()
                    high = current
                    repeatlst.append(lst[x])
            else:
                current = 0
    if(high == 0):
        high = 1
        repeatlst.clear()
        for x in range(1,21):
            repeatlst.append(x)
    endlst = [high,repeatlst]
    return endlst

def averaged20numthrown(lst):
    x = sum(lst)
    return (x/len(lst))

#------------------------------------------------------------------------------------------------------------------------------------------------------------------


#TESTING ENVIRONMENT
#------------------------------------------------------------------------------------------------------------------------------------------------------------------
#lst is a list of all the numbers
#lst2 is a nested list of 1 to 20 and the number of times each number was thrown
#lst3 is for lists loaded from files

#d20rollsfilewriter(lst, "d20rollednumbers.txt")
#d20rollsfilewriterrandomizer(lst,"burberry.txt")
#print(d20rollsfilereader(lst3, "burberry.txt"))


repeatlst = longestd20repeat(lst)
print("Average number thrown: ", averaged20numthrown(lst))
print("Length of longest same number sequence: ", repeatlst[0])
print("Number(s) with that length sequence: ", repeatlst[1])
if(repeatlst[0] == 1):
    print("Odds of that happening: 1 in 1")
else:
    print("Odds of that happening: 1 in", int(math.pow(20,repeatlst[0])))
print("Most favored number(s): ",end='')
mode = findD20mode(lst2)
for x in range(0,len(mode)):
    if (mode[x] == mode[-1]):
        print(mode[x])
    else:
        print(mode[x],end=", ")
print("Least favored number(s): ",end='')
mode = leastthrownd20side(lst2)
for x in range(0,len(mode)):
    if (mode[x] == mode[-1]):
        print(mode[x])
    else:
        print(mode[x],end=", ")
