n = int(input()) 
scores = input().split() # split with  spaces 

mx = int(scores[0]) 
mn = int(scores[0]) 

cnt = 0 
for i in range(1, len(scores)): 
    if int(scores[i]) > mx: 
        cnt += 1 
        mx = int(scores[i]) 
    elif int(scores[i]) < mn: 
        cnt += 1 
        mn = int(scores[i]) 

print(cnt) 



