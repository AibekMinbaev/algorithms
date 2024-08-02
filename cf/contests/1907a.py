
#Solution during the contest: 
# Time: n 
# Space: 1 ( if we don't count the space for input)
# Topics: Implementation

def main(): 
    s = input()
    ch = s[0] 
    num = int(s[1]) 
    for i in range(1, 9): 
        if i != num: 
            print(ch + str(i)) 
    chars = "abcdefgh" 
    for i in chars: 
        if i != ch:
            print(i + str(num))  

T = int(input()) 
t = 1 
while t <= T: 
    main() 
    t += 1 
