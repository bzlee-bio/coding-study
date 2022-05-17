import random
from time import time


def selectionSort(arr: List) -> List:
    lenArr = len(arr)
    for i in range(lenArr):
        minIdx = i
        for j in range(i+1, lenArr):
            if arr[minIdx] > arr[j]:
                minIdx = j

        arr[i], arr[minIdx] = arr[minIdx], arr[i]
    return arr

#def insertionSort(arr: List) -> List: 
