t = int(input()) 


for _ in range(t): 
    n = int(input()) 
    res = 1 + (n // 15) * 3 + min(n % 15, 2) 
    print(res) 


