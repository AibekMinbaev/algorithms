t = int(input()) 

for _ in range(t): 
    n = int(input()) 
    arr = list(map(int, input().split())) 
    st = set(b)  

    a = 0 
    b = 0 
    for i in range(len(arr)): 
        if i % 2 != 0: 
            a += arr[i] 
        else: 
            b -= arr[i]  
        
    x = a + b 
    i = 
    if x not in st: 
        print([x] + arr) 
    

        
    
            
