import time
import copy

class AlgoList:

    def __init__(self, listToSort):
        self.listToSort = listToSort

    def get(self):
        print (self.listToSort)

    def swap(self, list, index1, index2):
        list[index1], list[index2] = list[index2], list[index1]

    def sortListByFonctionSort(self, **args):
        self.listToSort.sort()
        # print (self.listToSort)
        return self.listToSort

    def sortListBySelection(self, **args):
        for j in range(len(self.listToSort)):
            indexMin = j
            for i in range(j+1 , len(self.listToSort)):
                if (self.listToSort[i] < self.listToSort[indexMin]):
                    indexMin         =   i
            if j != indexMin:
                self.swap(self.listToSort, j, indexMin)
        # print (self.listToSort)
        return self.listToSort

    def sortListByHeap(self, **args):
        def heapify(end,i):
            l = 2 * i + 1
            r = 2 * (i + 1)
            max=i
            if l < end and self.listToSort[i] < self.listToSort[l]:
                max = l
            if r < end and self.listToSort[max] < self.listToSort[r]:
                max = r
            if max != i:
                self.swap(self.listToSort, i, max)
                heapify(end, max)

        end = len(self.listToSort)
        start = end // 2 - 1
        for i in range(start, -1, -1):
            heapify(end, i)
        for i in range(end-1, 0, -1):
            self.swap(self.listToSort, i, 0)
            heapify(i, 0)
        # print (self.listToSort)
        return self.listToSort

    def sortListByBubble(self, **args):
        optimised = args.get("optimised")
        for i in range(len(self.listToSort)):
            tabSorted = optimised
            for j in range(len(self.listToSort) - i):
                if (j < (len(self.listToSort) - 1)):
                    if (self.listToSort[j] > self.listToSort[j + 1]):
                        self.swap(self.listToSort, j , j + 1)
                        tabSorted = False
            if (tabSorted):
                break
        # print (self.listToSort)
        return self.listToSort

    def getTimeOfRunFunction(self, **args):

        startTime       = time.time()
        if(args.get("method") == "sortListByFonctionSort"):
            self.sortListByFonctionSort()

        elif(args.get("method") == "sortListBySelection"):
            self.sortListBySelection()

        elif(args.get("method") == "sortListByHeap"):
            self.sortListByHeap()

        elif(args.get("method") == "sortListByBubble"):
            self.sortListByBubble(optimised = args.get("optimised"))

        elif(args.get("method") == "sortListByBubble"):
            self.sortListByBubble(optimised = args.get("optimised"))

        stopTime        = time.time()
        return args.get("method") + " : time to sort a list of {} elements : {} secondes\n".format(args.get("size"), str(stopTime - startTime))
