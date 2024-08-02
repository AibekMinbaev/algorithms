n = int(input()) 
arr = []

for i in range(n): 
    a, b = map(int, input().split()) 
    arr.append((a,b)) 
    
cnt = 0 

for i in range(n): 
    for j in range(n): 
        if i != j: 
            if arr[i][0] == arr[j][1]: 
                cnt += 1 

print(cnt) 