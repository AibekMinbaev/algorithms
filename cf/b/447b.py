s = input() 
k = int(input()) 

arr = list(map(int, input().split())) 
mx = max(arr) 

cnt = 0 
for i, char in  (s): # enumerate works with any iterable, 2nd argument is starting position 
    cnt += arr[ord(char) - 97] * (i + 1) 

for i in range(len(s) + 1, k + len(s) + 1): 
    cnt += mx * i 

print(cnt) 