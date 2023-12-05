t = input().split() 
n = int(t[0]) 

arr = list(map(int, input().split())) 

res = arr[0] - 1  

for i in range(1, len(arr)): 
    dif = arr[i] - arr[i-1] 
    if dif >= 0: 
        res += dif  
    else:
        res += n - abs(dif)  
print(res) 