n = list(map(int, input())) 

l = n[-1] 
cur = -1 

for i in range(len(n)): 
    if n[i] % 2 == 0: 
        if l > n[i]: 
            cur = i 
            break 
        else: 
            cur = i  

if cur == -1: 
    print(-1) 
else: 
    temp = n[cur] 
    n[cur] = l 
    n[-1] = temp  
    print("".join(map(str, n)))
