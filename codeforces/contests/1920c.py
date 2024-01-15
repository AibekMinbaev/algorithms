for _ in range(int(input())): 
    n = int(input()) 
    arr = list(map(int, input().split())) 

    res = 1 
    arr = [] 
    for i in range(1, n + 1): 
        if n % i == 0: 
            arr.append(i) 
        
    print(arr) 
    
    