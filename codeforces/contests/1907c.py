from collections import Counter

res = [] 
for _ in range(int(input())): 
    n = int(input())
    s = input()
    d = Counter(s) 
    arr = list(d.values())
    arr.sort() 

    d1 = Counter(arr) 
    arr = [] 
    for k, v in d1.items(): 
        if v == 1: 
            arr.append(k) 

    arr.sort()
    arr.reverse()

    print(arr) 
    cnt = 0 
    if arr: 
        cnt = arr[0] 
        for i in range(1, len(arr)): 
            if cnt > 0: 
                cnt -= arr[i] 
            else: 
                cnt = arr[i] + abs(cnt) 
    # print(cnt) 
    res.append(cnt) 
print(res) 