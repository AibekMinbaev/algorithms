#Solution after upsolving: 
# Time: nlog 
# Space: n 
# Topics: binary search 

# Todo: Upsolve 

res = [] 
for _ in range(int(input())): 
    n = int(input())  
    input_arr = list(map(int, input().split())) 
    arr = sorted(input_arr) 
    
    pref_sum = [] 
    sm = 0 
    for num in arr: 
        sm += num 
        pref_sum.append(sm) 
    
    d = {}
    for i in range(len(arr)): 
        target = pref_sum[i] 
    
        l, r = i, len(arr) - 1 

        while l < r: 
            m = (l + r) // 2 

            if arr[m] <= target: 
                l = m + 1
            else: 
                r = m - 1
        d[arr[i]] = l

    temp = []       
    for elem in input_arr: 
        print(d[elem]) 
        temp.append(d[elem])
    res.append(temp) 
print(res) 
     