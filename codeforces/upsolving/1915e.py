# Solution: after upsolving 
# Time: n 
# Space: n 
# Topics: prefix sum 
# Notes: in python dictionary it is faster to use string as a key rather than int as a key 

for _ in range(int(input())): 
    n = int(input()) 
    arr = list(map(int, input().split())) 

    d = set()
    d.add(0) 

    sm = 0 
    res = "NO"  

    for i in range(n): 
        if i % 2 == 0: 
            sm += arr[i] 
        else: 
            sm -= arr[i] 
        
        if sm in d: 
            res = "YES" 
            break 
        d.add(sm) 

    print(res)