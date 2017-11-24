class Timsort:
    '''
    Insertion sort is applied if the size of the array is less than 64
    and to bulk up runs to minrun length
    '''    
    def insertion_sort(self, unsortedRun):
        n = len(unsortedRun)
        for i in range(1, n):
            temp = unsortedRun[i]
            j = i
            while temp < unsortedRun[j-1] and j > 0:
                unsortedRun[j] = unsortedRun[j-1]
                j -= 1
            unsortedRun[j] = temp
        sortedRun = unsortedRun # Just to make things clear (not necessary) 

        return sortedRun


    '''
    Takes two ordered lists (either from natural runs or runs bulked up
    to minrun by insertion sort) and merges them to form one larger run
    '''
    def merge_sort(self, run1, run2):
        sortedList = []
        while len(run1) > 0 and len(run2) > 0:
            if run1[0] == run2[0]:
                sortedList.append(run1[0])
                del run1[0]
                sortedList.append(run2[0])
                del run2[0]
            else:
                if run1[0] < run2[0]:
                    sortedList.append(run1[0])
                    del run1[0]
                else:
                    sortedList.append(run2[0])
                    del run2[0]
        if len(run1) == 0:
            sortedList += run2
        elif len(run2) == 0:
            sortedList += run1

        return sortedList


    '''
    Creates a bitmask (data used for bitwise operations), compares n to
    the mask using an AND operation, and adds 1 to minrun if there are any
    remaining bits
    '''
    def calculate_minrun(self, n):
        mask = (1 << 6) - 1 # Bitwise 'shift left' operation (same as 1 * 2^6 (63))
        minrun = n & mask # Bitwise 'AND' operation 
        remainingBits = n >> 6 # Bitwise 'shift right' operation (same as (2^6)MOD n)
        if remainingBits > 0: 
            minrun += 1

        print("Minrun =", str(minrun))

        return minrun


    '''
    Main logic of the program: decides whether to use insertion sort or to
    search for/build runs of minrun length, and merge them
    '''
    def timsort(self, unsortedList):
        n = len(unsortedList)
        if n < 64: # Applies insertion sort for lists under 64 elements
            sortedList = self.insertion_sort(unsortedList)
        else:
            minrun = self.calculate_minrun(n)
            runs = []
            newRun = []
            newRun.append(unsortedList[0])
            for i in range(1, n):
                if i == n-1: # If it's the last value in the unsorted list
                    newRun.append(unsortedList[i])
                    runs.append(newRun)
                if unsortedList[i] < unsortedList[i-1]:
                    if len(newRun) == 0: # If there are no elements in newRun
                        newRun.append(unsortedList[i])
                    else:
                        runs.append([unsortedList[i]])
                        runs.append(newRun)
                        newRun = []
                else:
                    newRun.append(unsortedList[i])

            length = [y for x in runs for y in x]
            print(len(length))
            toMerge = []
            toInsert = []
            for i in runs:
                if runs.index(i) == (len(runs)-1):
                    toInsert = [y for x in toInsert for y in x]
                    toMerge.append(toInsert)
                    toMerge.append(i)
                elif len(i) < minrun:
                    toInsert.append(i)
                    if len([y for x in toInsert for y in x]) >= minrun:
                        toInsert = [y for x in toInsert for y in x]
                        toMerge.append(self.insertion_sort(toInsert))
                        toInsert = []
                else:
                    toMerge.append(i)
                    
            sortedList = []
            for i in toMerge: # Merges all the runs
                sortedList = self.merge_sort(sortedList, i)

        return sortedList
        
def sort(UnSortedList):
    t = Timsort()
    sortedList = t.timsort(UnSortedList)
    return sortedList

import random

number = int(input("How many random integers between 1 & 100 would you like to sort?: "))
s = [random.randint(1, 100) for i in range(number)]
print("BEFORE:")
print(s)
print("\n\n\n\nAFTER:")
print(sort(s))







    
