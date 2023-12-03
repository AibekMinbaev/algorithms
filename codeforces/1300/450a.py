t = input().split() 
n = int(t[0]) 
m = int(t[1]) 

arr = [int(elem) for elem in input().split()] 

mx = 0 
res = None 
for i in range(len(arr)): 
    temp = arr[i] // m 
    if arr[i] % m == 0: 
        temp -= 1
        
    if temp >= mx: 
        mx = temp 
        res = i + 1 
print(res) 


