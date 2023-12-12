# Solution after upsolving
# Time: n 
# Space: n 
# Topics: Implementatino 
# Notes: The deletion order does not matter. If some amount of some char is greater than n//2 then that number will remain. 


orda = ord("a") 
for _ in range(int(input())): 
    n = int(input()) 
    s = input()
    cnt = [0] * 26 # for all chars in english 
    for char in s: 
        cnt[ord(char) - orda] += 1 
    mx = max(cnt) # elem that appears most 

    print(max(n % 2, 2 * mx - n)) 