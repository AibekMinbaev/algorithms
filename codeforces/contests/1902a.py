# Solution after upsolving:

def main(): 
    n = int(input()) 
    s = input() 
    for i in range(n):
        if s[i] == '0': 
            return "YES" 
    return "NO" 
        
T = int(input()) # New way of taking input 
t = 1 
while t <= T: 
    print(main())
    t += 1


# Solution during the contest: 

# t = int(input()) 

# for k in range(t): 
#     temp = input()
#     arr = input() 
#     res = "NO"
#     for elem in arr: 
#         if elem == "0": 
#             res = "YES" 
#             break 
#     print(res) 