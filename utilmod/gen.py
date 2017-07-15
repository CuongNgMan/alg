#!/usr/bin/env python3.5
import random as r

def gen_unique_numbs(n:int=1001) -> list:
    l = [x for x in range(n)]
    r.shuffle(l)
    return l

def gen_random_numbs(n:int=1001,minval:int=0,maxval:int=1001) -> list:
    l = [r.randint(minval,maxval) for _ in range(0,n)]
    return l