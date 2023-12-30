import math 

for _ in range(int(input())): 
    a, b = map(int, input().split()) 
    gcd = math.gcd(a, b) 

    temp = (a * b) // gcd

    if temp == b: 
        for i in range(1, b+1): 
            if i != 1 and b % i == 0: 
                temp *= i 
                break 
    print(temp) 

