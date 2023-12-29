#Unsolved: Solution during the contest: 
# Notes: Got TLE during the contest 
# Time: n ^ 2 

for _ in range(int(input())): 
    n = int(input()) 
    arr = [] 

    for i in range(n): 
        a, b = map(int, input().split()) 
        arr.append((a,b)) 
    
    arr = sorted(arr, key=lambda x: x[0]) 
    
    cnt = 0 

    for i in range(n): 
        temp = arr[i][1]
        for j in range(i + 1, n): 
            if arr[j][1] < temp: 
                cnt += 1 
    print(cnt)
