for _ in range(int(input())): 
    n = int(input()) 
    arr = list(map(int, input().split())) 

    zero = False 
    neg = 0 
    for num in arr: 
        if num < 0: 
            neg += 1 
        elif num == 0: 
            zero = True 
    
    if not zero: 
        if neg % 2 == 0: 
            print(1) 
            print(1,0) 
        else: 
            print(0) 
    else:
        print(0) 
    
