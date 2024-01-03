t, k = map(int, input().split()) 

mod = 1000000007
dp = [-1 for i in range(10 ** 5 + 1)]

def helper(num):
    res = 1 

    return res 


for _ in range(t): 
    a, b = map(int, input().split()) 

    cnt = 0 
    for i in range(a, b+1): 
        if dp[i] > -1: 
            cnt += dp[i]  
        else: 
            w = helper(i) 
            cnt += w 
            dp[i] = w 

    print(cnt % mod)  