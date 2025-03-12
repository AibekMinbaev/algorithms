t = int(input()) 

for _ in range(t): 
    n = int(input()) 
    arr = list(map(int, input().split())) 
    st = set(arr)
    arr.sort() 

    a = sum(arr[n:])  
    b = sum(arr[:n])  

    a_arr = arr[n:] 
    b_arr = arr[:n] 

    res = [] 
    if a - b > 0 and a-b in st: 
        for i in range(n - 1, -1, -1): 
            a -= arr[i+n] 
            a += arr[i] 

            b -= arr[i] 
            b += arr[i+n] 

            print(a-b) 

            if a - b > 0 and a - b not in st: 
                a_arr = arr[i:i+n] 
                b_arr = arr[:i] + arr[i+n:] 
                break 

    res.append(a-b) 
    for i in range(n): 
        res.append(a_arr[i]) 
        res.append(b_arr[i])  

    print(*res) 

        