#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'numberOfWays' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY roads as parameter.
#

from collections import deque

def numberOfWays(roads):
    n = len(roads) + 1
    adj = [[] for _ in range(n)]
    for i, j in roads:
        adj[i - 1].append(j - 1)
        adj[j - 1].append(i - 1)
    
    # BFS function to calculate distances from a source node
    def bfs(src):
        dist = [-1] * n
        queue = deque([src])
        dist[src] = 0
        while queue:
            x = queue.popleft()
            for y in adj[x]:
                if dist[y] == -1:
                    dist[y] = dist[x] + 1
                    queue.append(y)
        return dist

    # Calculate distances from every node
    all_distances = [bfs(i) for i in range(n)]
    
    ans = 0

    # Iterate over all combinations of (i, j, k) such that i < j < k
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if all_distances[i][j] == all_distances[i][k] and all_distances[j][i] == all_distances[j][k]:
                    ans += 1
    return ans
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    roads_rows = int(input().strip())
    roads_columns = int(input().strip())

    roads = []

    for _ in range(roads_rows):
        roads.append(list(map(int, input().rstrip().split())))

    result = numberOfWays(roads)

    fptr.write(str(result) + '\n')

    fptr.close()
