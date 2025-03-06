t = int(input()) 

for _ in range(t): 
    n = int(input()) 
    arr = input().split() 

    for i in range(1, len(arr)): 
        if i > 0 and i < len(arr)-1 and arr[i] == "0": 
            if arr[i-1] == "1" and arr[i+1] == "1": 
                print("NO") 
                break 
    else: 
        print("YES") 
    
