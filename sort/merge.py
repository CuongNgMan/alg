#!/usr/bin/env python3.6

import sys
sys.path.append('../')

def merge(L:list,R:list):
    result = []
    i = j = 0
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            result.append(L[i])
            i+=1
        else:
            result.append(R[j])
            j+=1
    result+=L[i:]
    result+=R[j:]   
    return result


def merge_sort(L:list):
    if len(L) <= 1:
        return L
    mid = int(len(L)/2)
    left = merge_sort(L[:mid])
    right = merge_sort(L[mid:])
    return merge(left,right)

