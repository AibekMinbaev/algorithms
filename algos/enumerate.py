# It converts an iterable into an enumerate object where each element of the iterable is mapped to an index ( default at 0).  

#Code implementation: 

arr = ["hello", "hi", "bye"]  

enum_arr = enumerate(arr) # It save enumerate object with tuples 
for elem in enum_arr: 
    print(elem) 

#   Output 
#  (0, 'hello')
#  (1, 'hi')
#  (2, 'bye')


for ind, word in enumerate(arr): 
    print(ind, word) 

#   Output:  
#   0 hello
#   1 hi
#   2 bye 

for ind, word in enumerate(arr, 1): # the starting index can be changed 
    print(ind, word) 


#   Output:  
#   1 hello
#   2 hi
#   3 bye 
