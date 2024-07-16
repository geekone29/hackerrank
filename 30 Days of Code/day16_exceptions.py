# Day 16: Exceptions

#!/bin/python3

import math
import os
import random
import re
import sys


S = input()

try:
    n = int(S)
    print(n)
except ValueError:
    print('Bad String')