# -*- coding: utf-8 -*-

'''
problems:
Several detectors are located in different places with Cartesian coordinates.
Each of the detectors get their own signal transmission radius.
Please find all the possible collectors.

Collector is a special detector which can be reach by all the other detectrs
directly or indirectly to collect the data.
'''

import numpy as np
import math
from bitarray import bitarray

'''
1. build graph
'''

num_detector = int(input())

detectors = []
for i in range(num_detector):
    line = input().strip().split(' ')    
    detectors.append(tuple(float(v) for v in line))
    
num_detector = len(detectors)
connect_matrix = np.zeros((num_detector, num_detector), dtype=int)

for j in range(num_detector):
    dj_x, dj_y, dj_r = detectors[j]
    connect_arr = connect_matrix[j]
    for i in range(num_detector):
        di_x, di_y, di_r = detectors[i]
        
        dist = math.sqrt((di_x - dj_x) ** 2 + (di_y - dj_y) ** 2)
        
        if dj_r >= dist:
            connect_arr[i] = 1
            
print('\nadjacency matrix:\n', connect_matrix)
        


'''
2. find collectors
'''


# transpose matrix chagne the meaning of "connect-to" to "connect-from"
connect_matrix = connect_matrix.transpose()

# use bit manipulation to speed up the calculation
# each relationship bitarray stands for that,
# if the other detectors can reach this one
bit_relationships = []
for i in range(num_detector):
    bitarr = bitarray(connect_matrix[i].tolist())
    bit_relationships.append(bitarr)

collectors = []

# exam each detector if it can be a collector
for u, relationship in enumerate(bit_relationships):
    # find all detectors which can deireclty connect to this one
    reachable = [i for i, v in enumerate(relationship) if v == 1]
    while len(reachable) > 0:
        # get the relationship array of k'th detector
        k = reachable.pop()
        bit_rk = bit_relationships[k]

        # extract the indirect paths
        ext = (relationship ^ bit_rk) & bit_rk
        ext = [i for i, v in enumerate(ext) if v == 1]
        
        # add the new paths to reachable list
        reachable.extend(ext)
        
        # integrate the connecting ability of k'th detector to this one
        relationship |= bit_relationships[k]

    
    # If all detectors can reach this one, it's a collector
    if relationship.all():
        collectors.append(u)

print('number of collectors: ', len(collectors))

print('collectors: ', collectors)




