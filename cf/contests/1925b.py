import math 

for _ in range(int(input())): 
    x, n = map(int, input().split()) 

    cur = x - n + 1
    cnt = 1 
    while cur - (n - 1) > 0 and math.gcd(cur - (n-1), cnt +1) > 1: 
        print(cur) 
        cnt += 1
        cur -= n - 1 
    
    print(cnt) 

