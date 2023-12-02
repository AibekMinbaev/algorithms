t = int(input()) 

res = [0, 0, 0] 
for i in range(t): 
    input_ = [int(elem) for elem in input().split()]
    res[0] += input_[0] 
    res[1] += input_[1] 
    res[2] += input_[2]

if res[0] == 0 and res[1] == 0 and res[2] == 0:
    print("YES") 
else: 
    print("NO")


