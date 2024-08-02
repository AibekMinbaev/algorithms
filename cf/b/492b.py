#1st Solution: 
#Time: nlogn
#Space: 1 if not consider the input arr 

t = input().split() 
n = int(t[0])
l = int(t[1]) 

arr = list(set(map(int, input().split()))) 
arr.sort() 

mx = 0 
cur = 0 
for i in range(len(arr)): 
    if i == 0 and arr[i] != 0: 
        mx = max(mx, arr[i])
    else: 
        mx = max(mx, (arr[i] - cur)/2)
    cur = arr[i]

if arr[-1] != l: 
    mx = max(mx, l - arr[-1])

print(mx) 

