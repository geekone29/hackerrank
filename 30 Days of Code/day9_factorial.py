# Day 9: Factorial

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'factorial' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def factorial(n):
    temp = 1
    for i in range(1, n+1):
        temp = temp * i
    return temp  # Return the factorial result instead of printing it

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = factorial(n)  # Capture the returned result

    fptr.write(str(result) + '\n')

    fptr.close()
