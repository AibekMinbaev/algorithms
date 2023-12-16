def dfs(d, key, seen, cnt):  
    for elem in d[key]:
        if elem not in d: 
            cnt += 1 
        else: 
            seen.add(elem) 
            cnt += dfs(d, elem, seen, 0) 
    return cnt 

res = [] 
for _ in range(int(input())): 
    n = int(input()) 
    d = {} 
    for i in range(n - 1): 
        t, b = list(map(int, input().split())) 

        if t in d: 
            d[t].append(b) 
        else: 
            d[t] = [b] 
    
    cnt = 0 
    seen = set() 
    for k in d.keys(): 
        if k not in seen: 
            seen.add(k) 
            cnt += dfs(d, k, seen, 0) 
    
    res.append((cnt - 1) // 2 + 1 ) 
print(res)
  
