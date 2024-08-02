t = int(input()) 


for _ in range(t): 
    n, k = map(int, input().split()) 
    arr = list(map(int, input().split()))  
    
    res = 0 

    arr.sort() 
    arr.pop() 

    for e in arr: 
        res += e + e - 1 
    print(res) 
    

