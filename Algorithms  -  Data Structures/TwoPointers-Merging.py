n, m = map(int, input().split()) 
arr1 = list(map(int, input().split())) 
arr2 = list(map(int, input().split())) 

i = j = 0 
res = [0 for i in range(n + m)] 

while i < n or j < m: 
    if j == m or (i < n and arr1[i] < arr2[j]): 
        res[i + j] = arr1[i] 
        i += 1 
    else: 
        res[i + j] = arr2[j] 
        j += 1 

for i in range(m + n): 
    print(res[i])  
