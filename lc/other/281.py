class ZigIter: 

    def __init__(self, v1, v2): 
        self.v1 = v1
        self.v2 = v2 
        self.ind1 = 0
        self.ind2 = 0 
        self.switch = 0  

    def next(self): 
        while True: 
            if self.switch == 0 and self.ind1 < len(self.v1): 
                res = self.v1[self.ind1]
                self.ind1 += 1 
                self.switch = 1 
                return res 
            self.switch = 1 
            if self.ind2 < len(self.v2): 
                res = self.v2[self.ind2]
                self.ind2 += 1 
                self.switch = 0 
                return res 
            self.switch = 0 

    def hasNext(self): 
        if self.ind1 < len(self.v1) or self.ind2 < len(self.v2): 
            return True 
        return False 


v1 = [2,4,6,8,10,11,12,13]
v2 = [1,3,5,7,9] 

i = ZigIter(v1, v2) 

res = [] 
while i.hasNext(): 
    res.append(i.next()) 

print(res) 
