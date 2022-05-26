import random
from time import time
from sort import bubbleSort, selectionSort, insertionSort

arr = list(range(10**4))
random.shuffle(arr)


### python built-in sort function
timeStart = time()
sortedArr = sorted(arr)
timeEnd = time()

elapsedTime = timeEnd - timeStart
print(f'Python built-in sort elapsed time {elapsedTime}')



### Bubble Sort
timeStart = time()

selectionRes = bubbleSort(arr)

timeEnd = time()

elapsedTime = timeEnd - timeStart
ansTrue = sortedArr == selectionRes
print(f'Bubble sort elapsed time {elapsedTime}, correct? {ansTrue}')

### Insertion sort
timeStart = time()
insertionRes = insertionSort(arr)
timeEnd = time()
ansTrue = sortedArr == insertionRes
elapsedTime = timeEnd - timeStart
print(f'Insertion sort elapsed time {elapsedTime}, correct? {ansTrue}')


### Selection sort
timeStart = time()

selectionRes = selectionSort(arr)

timeEnd = time()

elapsedTime = timeEnd - timeStart
ansTrue = sortedArr == selectionRes
print(f'Selection sort elapsed time {elapsedTime}, correct? {ansTrue}')
#print(arr)
