n = int(input()) 

evens = [] 
odds = [] 

if n < 4 and n > 1: 
    print("NO SOLUTION") 
else:
    for i in range(1, n + 1): 
        if i % 2 == 0: 
            evens.append(i) 
        else: 
            odds.append(i) 

res = evens + odds 
print(*res) 
