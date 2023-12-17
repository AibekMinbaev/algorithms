n  = int(input()) 
arr = list(map(int, input().split())) 

sm = sum(arr) 
arr.sort(reverse=True) 

cnt = 0 
for i in range(len(arr)): 
    cnt += arr[i] 
    sm -= arr[i] 
    if cnt > sm: 
        print(i+1) 
        break 

