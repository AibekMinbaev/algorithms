n, m = map(int, input().split()) 
arr = list(map(int, input().split()))
arr.sort() 

res = float("inf") 

l, r = 0, n - 1 
while r < m: 
    res = min(res, arr[r] - arr[l])  
    l += 1 
    r += 1 

print(res) 