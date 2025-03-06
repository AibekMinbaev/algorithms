t = int(input()) 

for _ in range(t):  
    n, x = map(int, input().split()) 
    
    res = [x]
    if n == 1: 
        print(res)
    
    else: 
        num = 0 
        while len(res) < n: 
            if (num | x) == x: 
                res.append(num) 
            num += 1 
    
        print(res) 



