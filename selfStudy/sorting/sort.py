import random
from time import time


def selectionSort(arr: list) -> list:
    lenArr = len(arr)
    for i in range(lenArr):
        minIdx = i
        for j in range(i+1, lenArr):
            if arr[minIdx] > arr[j]:
                minIdx = j

        arr[i], arr[minIdx] = arr[minIdx], arr[i]
    return arr

def insertionSort(arr: list) -> list:
    lenArr = len(arr)
    for i in range(1,lenArr):
        for j in range(i,0,-1):
            if arr[j] < arr[j-1]:
               arr[j], arr[j-1] = arr[j-1], arr[j] 
            else:
                break
    return arr
