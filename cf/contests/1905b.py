#Solution after upsolving: 
# Time: n 
# Space: n 
# Topics: tree, implementation 
# Notes: be carefull when couting the leaf of the tree, because the root can become a leaf sometimes. 

from collections import defaultdict

for _ in range(int(input())): 
    n = int(input()) 
    d = defaultdict(int) 
    for i in range(n - 1): 
        t, b = list(map(int, input().split())) 
        d[t] += 1 
        d[b] += 1 

    cnt = 0 
    for k,v in d.items():  # Counting leafs 
        if v == 1:
            cnt += 1 
    print((cnt - 1) // 2 + 1 )
