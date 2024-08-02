#Solution after upsolving: 
#Topics: math, gcd 
#Time: n log max(arr) | Space: n 

from math import gcd # new function

def main(): 
    n = int(input()) 
    arr = [int(elem) for elem in input().split()] 

    if n == 1: return 1 
    arr.sort()
    
    all_diffs = set() 
    for i in range(1, len(arr)): 
        all_diffs.add(arr[i] - arr[i-1]) 

    all_diffs = list(all_diffs) 
    com_div = all_diffs[0]

    for elem in all_diffs: # total: n log max(arr) 
        com_div = gcd(elem, com_div) # if the implementation euclidian algo then time is log max(arr) in worst case
    
    res = 0 
    mx = max(arr) 
    for elem in arr: 
        res += (mx - elem)//com_div 

    st = set(arr) 
    new_elem = mx 
    cnt = 0 
    while new_elem in st: 
        new_elem -= com_div 
        cnt += 1 

    res += min(cnt, len(arr))
    return  res 

T = int(input()) 
t = 1 
while t <= T: 
    print(main()) 
    t += 1 
