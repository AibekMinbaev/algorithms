res = [] 

for _ in range(int(input())): 
    n = int(input()) 
    cnt = 0 
    last = (0,0) 
    ans = 0 
    for i in range(n):
        s = input().split() 
        cur = (int(s[0]), int(s[1])) 

        if last[0] <= cur[0] <= last[1] or last[0] <= cur[0] <= last[1]: 
            continue  
        else: 
            ans = max(ans, min(abs(cur[0] - last[1]), abs(cur[1] - last[0]))) 
            last = cur 
    # print(ans) 
    res.append(ans) 
print(res) 