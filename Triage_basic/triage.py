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

def sortListBySelection(listToSort):
    listSorted = []
    for j in range(len(listToSort)):
        min = j
        for i in range(j+1 , len(listToSort)):
            if (listToSort[i] < listToSort[min]):
                min         =   i
        if j != min:
            temp        =   listToSort[j]
            listToSort[j]     =   listToSort[min]
            listToSort[min]   =   temp
    return listToSort

def sortListByHeap(listToSort):
    def swap(i, j):
        listToSort[i], listToSort[j] = listToSort[j], listToSort[i]

    def heapify(end,i):
        l = 2 * i + 1
        r = 2 * (i + 1)
        max=i
        if l < end and listToSort[i] < listToSort[l]:
            max = l
        if r < end and listToSort[max] < listToSort[r]:
            max = r
        if max != i:
            swap(i, max)
            heapify(end, max)

    end = len(listToSort)
    start = end // 2 - 1
    for i in range(start, -1, -1):
        heapify(end, i)
    for i in range(end-1, 0, -1):
        swap(i, 0)
        heapify(i, 0)

    return listToSort






#-----------------------------------------------------

#Execution of test-----------------------------------------------------

for i in range(1, 10000,1000):
    print(getTimeOfRunFunction(sortListByFonctionSort,createRandomList(i)))
    print(getTimeOfRunFunction(sortListBySelection,createRandomList(i)))
    print(getTimeOfRunFunction(sortListByHeap,createRandomList(i)))

os.system("pause")
