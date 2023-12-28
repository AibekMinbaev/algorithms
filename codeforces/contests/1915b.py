for _ in range(int(input())): 
    a = set(input())
    b = set(input())
    c = set(input())

    if "?" in a: 
        if "A" in a and "B" in a: 
            print("C") 
        elif "A" in a and "C" in a: 
            print("B") 
        else: 
            print("A") 
 
    elif "?" in b: 
        if "A" in b and "B" in b: 
            print("C") 
        elif "A" in b and "C" in b: 
            print("B") 
        else: 
            print("A") 
    else: 
        if "A" in c and "B" in c: 
            print("C") 
        elif "A" in c and "C" in c: 
            print("B") 
        else: 
            print("A") 

