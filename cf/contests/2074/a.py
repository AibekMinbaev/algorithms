t = int(input()) 

for _ in range(t): 
    a, b, c, d = map(int, input().split()) 

    if len(set([a,b,c,d])) == 1: 
        print("YES") 
    else: 
        print("NO") 