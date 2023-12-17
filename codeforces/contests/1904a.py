# Solution after upsolving 
for _ in range(int(input())): 
    a, b = list(map(int, input().split())) 

    xk, yk = list(map(int, input().split()))
    xq, yq = list(map(int, input().split())) 

    moves = [(a, b),  (-a, b), (a, -b), (-a, -b), (b, a), (b, -a), (-b, a), (-b, -a)] # new 

    kset = set() 
    for m in moves: 
        new_position = (xk + m[0], yk + m[1])
        kset.add(new_position)

    cnt = 0 
    qset = set() 
    for m in moves: 
        new_position = (xq + m[0], yq + m[1]) 
        if new_position not in qset and new_position in kset: 
            cnt += 1 
            qset.add(new_position) 
    print(cnt)

