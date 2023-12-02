n = int(input()) 
arr = [ int(elem) for elem in input().split()] # calculate the time complexity here 
n1 = int(input()) 
arr_rqst = [int(elem) for elem in input().split()] 

d = {} 

for i in range(n): 
    d[arr[i]] = (i+1, n - i) 

cnt1 = 0 
cnt2 = 0 

for elem in arr_rqst: 
    cnt1 += d[elem][0] 
    cnt2 += d[elem][1] 

print(cnt1, cnt2) 

