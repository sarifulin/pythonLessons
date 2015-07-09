import random

__author__ = 'sarif'

# list = [20, 12, 10, 7, 4]
# list = [2, 4, 10, 17, 20]
list = range(0, 1000)
# list.reverse()
random.shuffle(list)


def isSorted(list):
    if len(list) == 0:
        return True
    j = list[0]
    for i in list:
        if j > i:
            return False
        j = i
    return True


def bubbleSort(list):
    swaps = 0
    comparison = 0
    arrayIsSorted = False
    while not arrayIsSorted:
        arrayIsSorted = True
        j = 0
        for i in range(0, len(list)):
            comparison += 1
            if list[j] > list[i]:
                arrayIsSorted = False
                pustoiGaraj = list[j]
                list[j] = list[i]
                list[i] = pustoiGaraj
                swaps += 1
            j = i
    print
    print("BubbleSort")
    print("swaps: {0}".format(swaps))
    print("comparison: {0}".format(comparison))


def selectSort(list):
    comparison = 0
    swaps = 0
    for i in range(0, len(list)):
        a = list[i]
        x = list[i]
        k = i
        flag = False
        for j in range(i + 1, len(list)):
            comparison += 1
            if x > list[j]:
                flag = True
                x = list[j]
                k = j
        if flag:
            swaps += 1
            list[i] = x
            list[k] = a
    print
    print("SelectSort")
    print("swaps: {0}".format(swaps))
    print("comparison: {0}".format(comparison))


def insertSort(list):
    comparison = 0
    swaps = 0
    #print(list)
    for i in range(0, len(list)):
        x = list[i]
        k = i
        for j in xrange(i-1, -1, -1):  # i-1 doljno bit >=0
            comparison += 1
            if x < list[j]:
                swaps += 1
                list[j + 1] = list[j]
                k = j
                #print(list)
            else:
                break
        list[k] = x
        swaps += 1
        #print(list)
        #print
    #print(list)
    print
    print("insertSort")
    print("swaps: {0}".format(swaps))
    print("comparison: {0}".format(comparison))



list1 = list[:]
list2 = list[:]
list3 = list[:]
selectSort(list1)
bubbleSort(list2)
insertSort(list3)
