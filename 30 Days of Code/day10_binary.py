# Day 10: Binary Numbers

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    data = bin(n)[2:]

    maximum = 0
    current = 0
    
    for i in data:
        if i == '1':
            current += 1
        else:
            maximum = max(maximum, current)
            current = 0
            
    print(max(maximum, current))
            