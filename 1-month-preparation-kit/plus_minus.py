#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    pos_num = 0
    neg_num = 0
    zero_num = 0
    for num in arr:
        if num > 0:
            pos_num += 1
        elif num < 0:
            neg_num += 1
        else:
            zero_num += 1
    print('{:.6f}'.format(round(pos_num / len(arr), 6)))
    print('{:.6f}'.format(round(neg_num / len(arr), 6)))
    print('{:.6f}'.format(round(zero_num / len(arr), 6)))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

# Test case 1
# Input (stdin)
# 6
# -4 3 -9 0 4 1
# Expected Output
# 0.500000
# 0.333333
# 0.166667

# Test case 11
# Input (stdin)
# 8
# 1 2 3 -1 -2 -3 0 0
# Expected Output
# 0.375000
# 0.375000
# 0.250000