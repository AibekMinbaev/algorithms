t = int(input()) 

for _ in range(t): 
    x = int(input()) 

    for c in range(2, x): 
        y = x ^ c 
        if x > y > 1: 
            print(x, y, c) 
            break 
    else: 
        print(-1) 
