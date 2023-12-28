import math 

for _ in range(int(input())): 
    n = int(input()) 
    arr = list(map(int, input().split())) 
    sm = sum(arr) 

    if float(math.sqrt(sm) % 1) == float(0): 
        print("YES") 
    else: 
        print("NO") 
