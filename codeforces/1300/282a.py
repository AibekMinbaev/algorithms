n = int(input()) 

res = 0 

for i in range(n): 
    temp = set(input()) 
    if "+" in temp: 
        res += 1 
    else: 
        res -= 1 
print(res) 
