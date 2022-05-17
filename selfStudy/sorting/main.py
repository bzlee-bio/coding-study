import random
from time import time
from sort import selectionSort, insertionSort

arr = list(range(10**4))
random.shuffle(arr)

timeStart = time()
sortedArr = sorted(arr)
timeEnd = time()

elapsedTime = timeEnd - timeStart
print(f'Python sort elapsed time {elapsedTime}')

#print(f'Before selection sort: {arr}')

timeStart = time()
insertionRes = insertionSort(arr)
timeEnd = time()
ansTrue = sortedArr == insertionRes
elapsedTime = timeEnd - timeStart
print(f'Insertion sort elapsed time {elapsedTime}, correct? {ansTrue}')


timeStart = time()

selectionRes = selectionSort(arr)

timeEnd = time()

elapsedTime = timeEnd - timeStart
ansTrue = sortedArr == selectionRes
print(f'Selection sort elapsed time {elapsedTime}, correct? {ansTrue}')
#print(arr)
