
def solve(n, x, k, s):
    time = 0 
    for dir in s: 
        if dir == "L": 
            x -= 1 
        else: 
            x += 1  
        time += 1 
        
        if x == 0: 
            break  
    else: 
        return 0 
    
    if k < time: 
        return 0 

    k -= time  

    time = 0 
    for dir in s: 
        if dir == "L": 
            x -= 1 
        else: 
            x += 1  
        time += 1 
        
        if x == 0: 
            break   
    else: 
        return 1
    
    return k // time + 1 
    



t = int(input()) 

for _ in range(t): 
    n, x, k = map(int, input().split()) 
    s = input()  
    print(solve(n,x,k,s))
