#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'maxPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY skillLevel
#  2. INTEGER minDiff
#

def maxPairs(skillLevel, minDiff):
    # Write your code here
    skillLevel.sort()
    n = len(skillLevel)
    i, j = 0, 1
    ans = 0
    
    while j < n:
        if skillLevel[j] - skillLevel[i] >= minDiff:
            ans += 1
            i += 1
            j += 1
        else:
            j += 1
        if i >= n // 2:
            break
            
    return ans
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    skillLevel_count = int(input().strip())

    skillLevel = []

    for _ in range(skillLevel_count):
        skillLevel_item = int(input().strip())
        skillLevel.append(skillLevel_item)

    minDiff = int(input().strip())

    result = maxPairs(skillLevel, minDiff)

    fptr.write(str(result) + '\n')

    fptr.close()
