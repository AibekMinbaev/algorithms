t = int(input()) 

for i in range(t): 
    x, n = map(int, input().split()) 

    res = 1 
    i = 1 
    while i * i <= x: 
        if x % i == 0:  
            if n <= x // i: 
                res = max(res, i) # we can add excess to another 2 2 2 2 2  = 2 4 4 
            
            if n <= i: 
                res = max(res, x//i) 
        
        i += 1 
    print(res) 



