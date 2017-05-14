from random import *
from triage import *
import os

#Definition of functions------------------------------

def createRandomList(size):
    listToSort = []
    for i in range(size):
        listToSort.append(randint(0, 100))
    # print (listToSort)
    return listToSort

#-----------------------------------------------------

# for h in range(1):
    # i = 100
for i in range(10, 10000, 1000):

    listToSort1 = AlgoList(createRandomList(i))
    listToSort2 = copy.deepcopy(listToSort1)
    listToSort3 = copy.deepcopy(listToSort1)
    listToSort4 = copy.deepcopy(listToSort1)
    listToSort5 = copy.deepcopy(listToSort1)

    # listToSort1.get()
    print(listToSort1.getTimeOfRunFunction(method = "sortListByFonctionSort",   size = i))
    # listToSort2.get()
    print(listToSort2.getTimeOfRunFunction(method = "sortListBySelection",      size = i))
    # listToSort3.get()
    print(listToSort3.getTimeOfRunFunction(method = "sortListByHeap",           size = i))
    # listToSort4.get()
    print(listToSort4.getTimeOfRunFunction(method = "sortListByBubble",         size = i , optimised = False))
    # listToSort4.get()
    print(listToSort5.getTimeOfRunFunction(method = "sortListByBubble",         size = i , optimised = True))
    print("\n")

os.system("pause")

#-----------------------------------------------------
