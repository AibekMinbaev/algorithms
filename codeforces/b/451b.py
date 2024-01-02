def helper(arr): 
    one = 0 
    l, r = -1, -1 

    for i in range(1, len(arr)): 
        if arr[i-1] > arr[i]: 
            if one: 
                return [0]
            if l == -1: 
                l = i - 1 
        else: 
            if l != -1 and not one: 
                r = i - 1 
                one = 1 

    if l == -1 and (r == -1 or r != -1): 
        return [1, 1, 1]
    else: 
        if l != -1 and r == -1: 
            r = n - 1 

        if (l == 0 or arr[r] >= arr[l - 1]) and (r == n - 1 or arr[l] <= arr[r+1]): 
            return [1, l+1, r+1] 
        else: 
            return [1] 


n = int(input()) 
arr = list(map(int, input().split())) 

res = helper(arr) 
if len(res) == 1: 
    print("no") 
else: 
    print("yes") 
    print(res[1], res[2])
