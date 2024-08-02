import collections 
res = []
for _ in range(int(input())): 
    n = int(input()) 
    s = input() 

    d = collections.Counter(s) 

    cnt = 0 
    for k, v in d.items(): 
        if ord(k) - 64 <= v: 
            cnt += 1 
    res.append(cnt) 
    print(cnt) 
# print(res) 