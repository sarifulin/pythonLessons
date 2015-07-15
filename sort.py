import random

__author__ = 'sarif'

# list = [20, 12, 10, 7, 4]
# list = [2, 4, 10, 17, 20]
list = range(0, 10)
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


# xrange bistree chem range, v inete vse pishut
def insertSort(list):
    comparison = 0
    swaps = 0
    # print(list)
    for i in range(0, len(list)):
        x = list[i]
        k = i
        for j in xrange(i - 1, -1, -1):  # i-1 doljno bit >=0
            comparison += 1
            if x < list[j]:
                swaps += 1
                list[j + 1] = list[j]
                k = j
                # print(list)
            else:
                break
        list[k] = x
        swaps += 1
        # print(list)
        # print
    # print(list)
    print
    print("insertSort")
    print("swaps: {0}".format(swaps))
    print("comparison: {0}".format(comparison))


def ShellSort(list):
    comparison = 0
    swaps = 0
    steps = []
    size = len(list)
    i = 0
    while True:
        iteration = shellIteration(i)
        if 3 * iteration > size:
            break
        else:
            steps.append(iteration)
        i += 1
    steps.reverse()

    for step in steps:
        for groupNumber in range(0, step):
            for groupI in xrange(groupNumber, size, step):
                x = list[groupI]
                k = groupI
                for groupJ in xrange(groupI - step, groupNumber-1, -step):
                    comparison +=1
                    if x < list[groupJ]:
                        swaps += 1
                        list[groupJ + step] = list[groupJ]
                        k = groupJ
                    else:
                        break
                list[k] = x
                swaps += 1
    print
    print("ShelltSort")
    print("swaps: {0}".format(swaps))
    print("comparison: {0}".format(comparison))




def shellIteration(s):
    if s % 2 == 0:
        return 9 * 2 ** s - 9 * 2 ** (s / 2) + 1
    else:
        return 8 * 2 ** s - 6 * 2 ** ((s + 1) / 2) + 1


def pushDown(list, i):
    size = len(list)
    childIndex = 2*i+1
    if childIndex > size:
        return
    if (2*i+2) < size and list[2*i+2]> list[childIndex]:
        childIndex = 2*i+2
    if list[i] < list[childIndex]:
        parentSave = list[i]
        list[i] = list[childIndex]
        list[childIndex] = parentSave
        pushDown(list, childIndex)
        print("pushDown list = ", list)


def pyramidSort(list):
    comparison = 0
    swaps = 0
    size = len(list)
    print("original:", list)
    for i in range((size // 2) - 1, -1, -1):
       pushDown(list, i)
    print("our pyramid:", list)
    for j in range(size-1, -1, -1):
        print("j=", j)
        k = list[0]
        print("first:", k)
        print("last:", list[j])
        list[0] = list[j]
        list[j] = k
        print("without root:", list)
        pushDown(list, j)
        print("final result:", list)








pyramidSort([1, 8, 2, 7, 4, 5, 0, 3, 9, 6])
# pyramidSort(list[:])
# selectSort(list[:])
# bubbleSort(list[:])
# insertSort(list[:])
# ShellSort(list[:])

