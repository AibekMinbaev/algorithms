s = input() 
word = "hello" 

ind = 0 
cnt = 0 
while ind < len(s) and cnt < 5: 
    if word[cnt] == s[ind]: 
        cnt += 1 
    ind += 1 

if cnt == 5: 
    print("YES") 
else: 
    print("NO") 


