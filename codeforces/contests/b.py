
def main(finres): 
    s = input() 
    ch_lower = [] 
    ch_upper = [] 

    res = ""
    for i in range(len(s)):
        if s[i] == 'b': 
            if ch_lower:
                ch_lower.pop() 
        elif s[i] == 'B': 
            if ch_upper: 
                ch_upper.pop() 
        else: 
            if s[i].islower(): 
                ch_lower.append((i, s[i]))
            else: 
                ch_upper.append((i, s[i]))
    
    i = 0 
    j = 0 
    while i < len(ch_lower) and j < len(ch_upper): 
        if ch_lower[i][0] < ch_upper[j][0]: 
            res += ch_lower[i][1] 
            i += 1 
        else: 
            res += ch_upper[j][1]
            j += 1 
    while i < len(ch_lower): 
        res += ch_lower[i][1]
        i += 1 

    while j < len(ch_upper): 
        res += ch_upper[j][1] 
        j += 1 
    
    # finres.append(res) 
    print(res) 



T = int(input()) 
t = 1 
res = []
while t <= T: 
    main(res) 
    t += 1 
# print(res) 