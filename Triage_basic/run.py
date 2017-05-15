from random import *
from triage import *
import matplotlib.pyplot as plt
import os

#Definition of functions------------------------------

def createRandomList(size):
    listToSort = []
    for i in range(size):
        listToSort.append(randint(0, 100))
    # print (listToSort)
    return listToSort

def createInversedList(size):
    listToSort = []
    for i in range(size):
        listToSort.append(i)
    listToSort.reverse()
    return listToSort

def calculate(typeSort, listToSort, **args):
    listToSortCopy = copy.deepcopy(listToSort)
    # listToSort1.get()
    return listToSortCopy.getTimeOfRunFunction(method = typeSort, size = args.get("size"), optimised = args.get("optimised"))


#-----------------------------------------------------

listTimeToExecuteSortListByFonctionSort      = []
listTimeToExecuteSortListBySelection         = []
listTimeToExecuteSortListByHeap              = []
listTimeToExecuteSortListByBubble            = []
listTimeToExecuteSortListByBubbleOptimised   = []

listSize = []
for i in range(10, 10000, 1000):
    listSize.append(i)
    listToSort  = AlgoList(createRandomList(i))

    listTimeToExecuteSortListByFonctionSort.append(calculate("sortListByFonctionSort", listToSort, size = i ))
    listTimeToExecuteSortListBySelection.append(calculate("sortListBySelection", listToSort, size = i))
    listTimeToExecuteSortListByHeap.append(calculate("sortListByHeap", listToSort, size = i))
    listTimeToExecuteSortListByBubble.append(calculate("sortListByBubble", listToSort, size = i))
    listTimeToExecuteSortListByBubbleOptimised.append(calculate("sortListByBubble", listToSort, size = i, optimised = True))

print(listTimeToExecuteSortListByFonctionSort)
print(listTimeToExecuteSortListBySelection)
print(listTimeToExecuteSortListByHeap)
print(listTimeToExecuteSortListByBubble)
print(listTimeToExecuteSortListByBubbleOptimised)


plt.plot(listSize, listTimeToExecuteSortListByFonctionSort, label="sortListByFonctionSort")
plt.plot(listSize, listTimeToExecuteSortListBySelection, label="sortListBySelection")
plt.plot(listSize, listTimeToExecuteSortListByHeap, label="sortListByHeap")
plt.plot(listSize, listTimeToExecuteSortListByBubble, label="sortListByBubble")
plt.plot(listSize, listTimeToExecuteSortListByBubbleOptimised, label="sortListByBubbleOptimised")


plt.ylabel('Label 1')
plt.xlabel('Numbers of elements')
plt.ylabel('Time (s)')
plt.legend()
plt.show()

# os.system("pause")

#-----------------------------------------------------
