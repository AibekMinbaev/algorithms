t = int(input()) 

for _ in range(t): 
    n, m, k = map(int, input().split())     

    res = [i for i in range(1, n + 1)]
    tail = res[:m] 
    head = res[m:][::-1]
    finres = head + tail 
    print(*finres) 
