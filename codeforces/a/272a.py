n = int(input()) 
arr = [int(elem) for elem in input().split()] 

res = 0 
sm_arr = sum(arr) 

for i in range(1, 6): 
    if ((sm_arr + i) % (n + 1)) != 1:
        res += 1 
print(res) 
