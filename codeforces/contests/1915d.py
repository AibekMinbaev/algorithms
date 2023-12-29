# Solved: Contest Solution 
for _ in range(int(input())): 
    n = int(input()) 
    s = input() 
    res = "" 

    l = 0 
    while l < n: 
        if s[l] in ["b","c","d"]: 
            res += s[l] 
            l += 1 
        else: 
            res += s[l] 
            l += 1 
            if l + 1 == n or (l + 1 < n and s[l + 1] in ["b", "c", "d"]): 
                res += s[l] 
                l += 1 
            res += "." 
    print(res[:-1]) 
