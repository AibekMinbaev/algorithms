m, s = map(int, input().split()) 

s1 = s2 = s 
mn, mx = [],[] 

for i in range(m): 

    for j in range(0, 10): 
        if i == 0 and j == 0: 
            continue 

        if s1 - j >= 0 and (s1 - j) / 9 <= m - i - 1: 
            mn.append(j)
            s1 -= j 
            break  
    else: 
        mn.append(0) 
    

    for k in range(9, -1, -1):   
        if s2 - k >= 0:  
            mx.append(k) 
            s2 -= k
            break 
    else: 
        mx.append(0) 


if sum(mx) != s or sum(mn) != s or (len(mx) != 1 and mx[0] == 0) or (len(mn) != 1 and mn[0] == 0): 
    print(-1,-1) 
else: 
    print("".join(map(str, mn)), "".join(map(str,mx))) 

