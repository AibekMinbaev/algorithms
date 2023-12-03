n = int(input()) 

arr = [] 
for i in range(n): 
    temp = input().split() 
    arr.append((int(temp[0]), int(temp[1]))) 

res = 0 
for i in range(len(arr)): 
    temp = [0,0,0,0] 
    x = arr[i][0]
    y = arr[i][1] 

    for j in range(len(arr)): 
        if i != j: 
            x1 = arr[j][0]
            y1 = arr[j][1] 

            if x == x1 and y < y1: 
                temp[0] = 1 
            elif x == x1 and y > y1: 
                temp[1] = 1 
            elif x < x1 and y == y1: 
                temp[2] = 1 
            elif x > x1 and y == y1: 
                temp[3] = 1 
    if sum(temp) == 4: 
        res += 1 
print(res) 
