# Day 28: RegEx, Patterns, and Intro to Databases

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input().strip())
    names = []
    
    for _ in range(N):
        first_multiple_input = input().rstrip().split()
        firstName = first_multiple_input[0]
        emailID = first_multiple_input[1]
    
        if emailID.endswith("@gmail.com"):
            names.append(firstName)
    
    names.sort()

    for name in names:
        print(name)
