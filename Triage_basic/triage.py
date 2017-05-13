from random import *
import time
import os
import unittest


#Definition of functions------------------------------

def createRandomList(size):
    listToSort = []
    for i in range(size):
        listToSort.append(randint(0, 100))
    # print (listToSort)
    return listToSort

def getTimeOfRunFunction(function, **args):
    listToSort      = args.get("listToSort")
    size            = args.get("size")
    optimised       = args.get("optimised")

    startTime       = time.time()
    function(listToSort, optimised = optimised)
    stopTime        = time.time()
    return str(function.__name__) + ": time to sort a list of {} elements : {} secondes\n".format(size, str(stopTime - startTime))

def sortListByFonctionSort(listToSort, **args):
    listToSort.sort()
    return listToSort

def swap(list, index1, index2):
    list[index1], list[index2] = list[index2], list[index1]

def sortListBySelection(listToSort, **args):
    for j in range(len(listToSort)):
        indexMin = j
        for i in range(j+1 , len(listToSort)):
            if (listToSort[i] < listToSort[indexMin]):
                indexMin         =   i
        if j != indexMin:
            swap(listToSort, j, indexMin)
    # print (listToSort)
    return listToSort

def sortListByHeap(listToSort, **args):
    def heapify(end,i):
        l = 2 * i + 1
        r = 2 * (i + 1)
        max=i
        if l < end and listToSort[i] < listToSort[l]:
            max = l
        if r < end and listToSort[max] < listToSort[r]:
            max = r
        if max != i:
            swap(listToSort, i, max)
            heapify(end, max)

    end = len(listToSort)
    start = end // 2 - 1
    for i in range(start, -1, -1):
        heapify(end, i)
    for i in range(end-1, 0, -1):
        swap(listToSort, i, 0)
        heapify(i, 0)
    # print (listToSort)
    return listToSort

def sortListByBubble(listToSort, **args):
    optimised = args.get("optimised")
    for i in range(len(listToSort)):
        tabSorted = optimised
        for j in range(len(listToSort) - i):
            if (j < (len(listToSort) - 1)):
                if (listToSort[j] > listToSort[j + 1]):
                    swap(listToSort, j , j + 1)
                    tabSorted = False
        if (tabSorted):
            break
    # print (listToSort)
    return listToSort

#-----------------------------------------------------

#Execution of test-----------------------------------------------------
# for h in range(1):
#     i = 50000
for i in range(10, 10000, 1000):

    print("1 " + getTimeOfRunFunction(sortListByFonctionSort,   listToSort = createRandomList(i), size = i))
    # print("2 " + getTimeOfRunFunction(sortListBySelection,      listToSort = createRandomList(i), size = i))
    # print("3 " + getTimeOfRunFunction(sortListByHeap,           listToSort = createRandomList(i), size = i))
    # print("4 " + getTimeOfRunFunction(sortListByBubble,         listToSort = createRandomList(i), size = i, optimised = True))
    # print("5 " + getTimeOfRunFunction(sortListByBubble,         listToSort = createRandomList(i), size = i, optimised = False))

    print("\n")


os.system("pause")

#-----------------------------------------------------

class TestSort(unittest.TestCase):

    def testSortListByFonctionSort(self):
        self.assertEqual(sortListByFonctionSort([10,9,8,5,7,6,2,1,3,4]),[1,2,3,4,5,6,7,8,9,10])

    def testSortListBySelection(self):
        self.assertEqual(sortListBySelection([10,9,8,5,7,6,2,1,3,4]),[1,2,3,4,5,6,7,8,9,10])

    def testSortListByHeap(self):
        self.assertEqual(sortListByHeap([10,9,8,5,7,6,2,1,3,4]),[1,2,3,4,5,6,7,8,9,10])

    def testSortListByBubbleNotOptimised(self):
        self.assertEqual(sortListByBubble([10,9,8,5,7,6,2,1,3,4], optimised = False),[1,2,3,4,5,6,7,8,9,10])

    def testSortListByBubbleOptimised(self):
        self.assertEqual(sortListByBubble([10,9,8,5,7,6,2,1,3,4], optimised = True),[1,2,3,4,5,6,7,8,9,10])
