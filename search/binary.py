# !/usr/bin/env python3.6
def bi_search(v:int,L:list=None):
    low = 0
    high = len(L)
    while low < high:
        mid = int((high+low)/2)
        if L[mid] == v:
            return mid
        elif v > L[mid]:
            low = mid+1
        else:
            high = mid-1
    return False