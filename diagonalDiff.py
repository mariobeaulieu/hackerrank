#!/usr/bin/env python3

import os
import random
import re
import sys

# Complete the diagonalDifference function below.
def diagonalDifference(n,arr):
    d=0
    for i in range(n):
        d+=arr[i][i]-arr[i][-1-i]
        print('%i-%i'%(arr[i][i],arr[i][-i]))
    return abs(d)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(n,arr)

    fptr.write(str(result) + '\n')

    fptr.close()
