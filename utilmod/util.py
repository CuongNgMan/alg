from utilmod.gen import *
from utilmod.reader import *
from utilmod.writer import *

def write_result(L:list,filename:str='result') -> None:
    length = len(L)
    if length == 0:
        return None
    write(filename,L);

def new_numb(n:int=1001) -> None:
    new_numbs = gen_unique_numbs(n)
    write_result(new_numbs,'unique')
    return None

def get_input(filename:str='unique') -> list:
    L = read(filename);
    return L

    

