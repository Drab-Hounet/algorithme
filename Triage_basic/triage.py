from random import *
import time
import os

#Definition of functions------------------------------

def createRandomList(size):
    listToSort = []
    for i in range(size):
        listToSort.append(randint(0, 100))
    return listToSort, size

def getTimeOfRunFunction(function, list):
    startTime       =       time.time()
    function(list[0])
    stopTime        =       time.time()
    return str(function.__name__) + ": time to sort a list of {} elements : {} secondes\n".format(list[1],str(stopTime - startTime))

def sortListByFonctionSort(list):
    list.sort()
    return list

def sortListBySelection(list):
    listSorted = []
    for j in range(len(list)):
        min = j
        for i in range(j+1 , len(list)):
            if (list[i] < list[min]):
                min         =   i
        if j != min:
            temp        =   list[j]
            list[j]     =   list[min]
            list[min]   =   temp
    return list

#-----------------------------------------------------

#Execution of test-----------------------------------------------------

for i in range(10,10000,1000):
    print(getTimeOfRunFunction(sortListByFonctionSort,createRandomList(i)))
    print(getTimeOfRunFunction(sortListBySelection,createRandomList(i)))

os.system("pause")
