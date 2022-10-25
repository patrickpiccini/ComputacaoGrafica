#!/bin/python3

import math
import os
import random
import re
import sys



def minSwapsRequired(s):
    def verify_palindromo(n):
        return n == n[::-1]

    # def palin(s: str, n: int = 0) -> int:
    #     if verify_palindromo(s): 
    #         return 0
        
    #     if n >= len(s): 
    #         return 0
    
    #     m = -1
    #     for j in range(len(s)-1):
    #         new_str = swap(s, j, j+1)
    #         l = palin(new_str, n+1)
    #         if m == -1 or l < m:
    #             m = l
        
    #     return m + 1
        
    def palin(s: str, n: int = 0) -> int:
        if verify_palindromo(s): 
            return n
        
        if n >= len(s): 
            return n
    
        m = -1
        for j in range(n,len(s)-1):
            new_str = swap(s, n, j)
            l = palin(new_str, n+1)
            if m == -1 or l < m:
                m = l
        
        return m
        
        
    def swap(s: str, i: int, j: int) -> str:
        s = list(s)
        s[i], s[j] = s[j], s[i]
        return "".join(s)
    
        
    l = len(s)
    if ((l % 2 == 0) and (s.count("1") % 2)):
        return -1
    
    if l <= 2:
        return 0
        
    return palin(s)
        
        
        
        

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = minSwapsRequired(s)
    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
