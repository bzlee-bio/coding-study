import random
from time import time


def bubbleSort(arr: list) -> list:
    lenArr = len(arr)
    swapFlag = True
    while swapFlag:
        swapFlag = False
    
        for j in range(lenArr-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapFlag = True
    return arr


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


def mergeSort(arr: list) -> list:
    level = 2
    q, r = divmod(len(arr), level) 
    
    while q > 1:
        for i in range(q):
            pL = i*level

            pR = i*level+level/2

            if pR < len(arr):
                leftArr = arr[pL:pR]
                rightArr = arr[pR:pR+level/2]

                while len(leftArr)>0 or  len(rightArr)>0:
                    arr[pL] = leftArr.pop() if leftArr[0]<rightArr[0] else rightArr.pop()
                    

                    pL+=1



