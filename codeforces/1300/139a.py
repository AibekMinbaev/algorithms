n = int(input()) 
arr = [int(elem) for elem in input().split()] 

md_left= n % sum(arr) 

if md_left == 0: 
    res = None
    for i in range(len(arr)): 
        if arr[i] != 0: 
            res = i + 1
    print(res)
    
else: 
    if md_left <= sum(arr[:1]):
        print(1) 
    elif md_left <= sum(arr[:2]): 
        print(2) 
    elif md_left <= sum(arr[:3]): 
        print(3) 
    elif md_left <= sum(arr[:4]): 
        print(4) 
    elif md_left <= sum(arr[:5]): 
        print(5) 
    elif md_left <= sum(arr[:6]): 
        print(6) 
    else: 
        print(7)




