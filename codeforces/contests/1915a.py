# Solved: Contest solution 
for _ in range(int(input())): 
    a, b, c = list(map(int, input().split())) 

    if a == b: 
        print(c) 
    elif a == c: 
        print(b) 
    else: 
        print(a) 
