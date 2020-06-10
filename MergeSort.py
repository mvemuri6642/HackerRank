# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 15:58:58 2020

@author: mvemuri6642
"""

#Merge sort

def mergeSort(arr):
    if(len(arr)>1):
        mid=len(arr)//2
        l=arr[:mid]
        r=arr[mid:]
        mergeSort(l)
        mergeSort(r)
        i=j=k=0
        while(i<len(l) and j<len(r)):
            if(l[i]<r[j]):
                arr[k]=l[i]
                i+=1
            else:
                arr[k]=r[j]
                j+=1
            k+=1
        while(i<len(l)):
            arr[k]=l[i]
            i+=1
            k+=1
        while(j<len(r)):
            arr[k]=r[j]
            j+=1
            k+=1
 
def printList(arr):
    for i in range(len(arr)):
        print(arr[i],end=" ")


arr=list(map(int,input().split()))
mergeSort(arr)
printList(arr)