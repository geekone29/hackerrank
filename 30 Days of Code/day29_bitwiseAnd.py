# Day 29: Bitwise AND

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bitwiseAnd' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER N
#  2. INTEGER K
#

def bitwiseAnd(N, K):
    # Write your code here
    max_and = 0
    for A in range(N, 1, -1):
        for B in range(A - 1, 0, -1):
            current_and = A & B
            if current_and > max_and and current_and < K:
                max_and = current_and
            if max_and == K - 1:
                break
        if max_and == K - 1:
            break
    return max_and

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        count = int(first_multiple_input[0])

        lim = int(first_multiple_input[1])

        res = bitwiseAnd(count, lim)

        fptr.write(str(res) + '\n')

    fptr.close()
