import unittest
from triage import *

#python.exe -m unittest -v test

class TestSort(unittest.TestCase):

    def testSortListByFonctionSort(self):
        listToSort = AlgoList([10,9,8,5,7,6,2,1,3,4])
        self.assertEqual(listToSort.sortListByFonctionSort(),[1,2,3,4,5,6,7,8,9,10])

    def testSortListBySelection(self):
        listToSort = AlgoList([10,9,8,5,7,6,2,1,3,4])
        self.assertEqual(listToSort.sortListBySelection(),[1,2,3,4,5,6,7,8,9,10])

    def testSortListByHeap(self):
        listToSort = AlgoList([10,9,8,5,7,6,2,1,3,4])
        self.assertEqual(listToSort.sortListByHeap(),[1,2,3,4,5,6,7,8,9,10])

    def testSortListByBubbleNotOptimised(self):
        listToSort = AlgoList([10,9,8,5,7,6,2,1,3,4])
        self.assertEqual(listToSort.sortListByBubble(optimised = False),[1,2,3,4,5,6,7,8,9,10])

    def testSortListByBubbleOptimised(self):
        listToSort = AlgoList([10,9,8,5,7,6,2,1,3,4])
        self.assertEqual(listToSort.sortListByBubble(optimised = True),[1,2,3,4,5,6,7,8,9,10])
