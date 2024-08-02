t = int(input()) 

res = 0 
cur = 0 

for i in range(t): 
    pair = input().split() 
    cur += int(pair[1]) - int(pair[0])
    res = max(res, cur)
print(res)  

