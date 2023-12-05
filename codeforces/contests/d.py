
def main(): 
    s = input() 
    res = [] 
    for ch in s: 
        if ch == 'b' or ch == 'B': 
            if res: res.pop() 
        else:
            res.append(ch) 
    print("".join(res))

T = int(input()) 
t = 1 
while t <= T: 
    main() 
    t += 1 