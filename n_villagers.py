# -*- coding: utf-8 -*-

'''
problems:
Friendships between n villagers are given.
Base on friend's friend is also firend, 
please find how much friend groups in this village.
'''

import numpy as np


num_villager = int(input())
num_relationship = int(input())

relationship_matrix = np.zeros((num_villager, num_villager), dtype=int)

while True:
    line = input().strip()
    if not line:
        break
    
    line = line.split(' ')
    v1, v2 = [int(v)-1 for v in line]
    
    relationship_matrix[v1][v2] = 1
    relationship_matrix[v2][v1] = 1
    
visited = np.zeros(num_villager, dtype=int)
num_visited = 0

num_cluster = 0
stack = [0]
visited[0] = 1
while num_visited < num_villager:
    p = stack.pop()
    num_visited += 1
    relationship_arr = relationship_matrix[p]
    for i, v in enumerate(relationship_arr):
        if v == 1 and visited[i] == 0:
            visited[i] = 1
            stack.append(i)
    if len(stack) == 0:
        num_cluster += 1
        for i, v in enumerate(visited):
            if v == 0:
                visited[i] = 1
                stack.append(i)
                break

print('number of cluster: {}'.format(num_cluster))
