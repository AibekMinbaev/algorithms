# Solution after upsolving
# Time: log(max(r)) * n 
# Space: 1 if do not count the input array 
# Topic: binary search 
# Notes: it was quite tricky to 

for _ in range(int(input())): 
    n = int(input()) 
    arr = [] 
    mx = 0 
    for i in range(n): 
        p = input().split() 
        arr.append((int(p[0]), int(p[1])))
        mx = max(mx, int(p[1])) 
    
    l, r = 0, mx 

    temp = 0 
    while l < r: 
        m = (l + r) // 2 

        status = True 
        left = 0 
        right = 0 
        for pair in arr: 
            left -= m 
            right += m 

            left = max(left, pair[0]) 
            right = min(right, pair[1]) 

            if left > right: 
                status = False
                break 
        if status: 
            r = m
        else: 
            l = m + 1 

    print(r) 