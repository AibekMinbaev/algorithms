t = int(input()) 

for _ in range(t): 
    n, k, p = map(int, input().split()) 

    if abs(k) > n * p: 
        print(-1) 
    else: 
        res = abs(k) // p 
        res += 1 if abs(k) % p !=0 else 0 
        print(res) 
