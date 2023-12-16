class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = [] 

        for elem in tokens: 
            if elem not in ["*", "+", "/", "-"]: 
                stack.append(int(elem)) 
            else: 
                b = stack.pop() 
                a = stack.pop() 
                sm = None 
                if elem == "*":
                    sm = a * b 
                elif elem == "/": 
                    sm = int(a / b) # int trancates to zero 

                    # if (b < 0 and a < 0) or (b > 0 and a > 0): 
                    #     sm = math.floor(a / b) 
                    # else: 
                    #     sm = math.ceil(a / b)
                      
                elif elem == "+": 
                    sm = a + b 
                else: 
                    sm = a - b 
                stack.append(sm) 
        return stack[-1] 