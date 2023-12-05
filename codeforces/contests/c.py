import collections

def main(finres): 
    n = int(input()) 
    s = input().split() 
    d = collections.defaultdict(int) 

    if n == 1: 
        return 1 
    cnt = 0 

    l = n // 2 
    r = l + 1 

    while r < n: 
        if s[l] != s[r]:
            cnt += 2 
            s[l], s[r] = "-", "-"

        
        if l - 1 == -1: 
            l = r 
        else: 
            l -= 1 
        r += 1
    finres.append(n - cnt) 
    
finres = [] 
T = int(input()) 
t = 1 
while t <= T: 
    main(finres) 
    t += 1 
print(finres) 
