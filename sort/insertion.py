#!/usr/bin/env python3.6
"""
for j=2 to A.length
    key = A[j]
    i = j - 1
    while A[i] > key and i > 0
        A[i+1] = A[i]
        i--
    A[i+1] = key
"""
import sys
sys.path.append('../')

from utilmod.util import *
new_numb(20)
input_array = get_input()   

def insertion_sort(L:None) -> list:
    for j in range(1,len(L)):
        key = L[j]
        i = j - 1
        while i >= 0 and L[i] < key:
            L[i+1] = L[i]
            i = i - 1
        L[i+1] = key
    return L

result = insertion_sort(input_array)
write_result(result,'result')
