n = int(input()) 

arr = [] 
for i in range(n + 1): 
    temp = set(str(i))
    if len(temp) == 2: 
        if "4" in temp and "7" in temp: 
            arr.append(i) 
    elif len(temp) == 1: 
        if "4" in temp or "7" in temp: 
            arr.append(i) 
    
res = "NO"
for elem in arr: 
    if n % elem == 0: 
        res = "YES" 
        break 
print(res) 