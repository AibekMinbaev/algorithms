class TimeMap:

    def __init__(self): 
        self.d = {} 

    def set(self, key: str, value: str, timestamp: int) -> None: 
        if key in self.d: 
            self.d[key].append((value, timestamp))
        else: 
            self.d[key] = [(value, timestamp)] 

    def get(self, key: str, timestamp: int) -> str: 
        ans = ""
        if key in self.d: 
            l = 0 
            r = len(self.d[key]) - 1 
            while l <= r: 
                m = (r + l) // 2
                if self.d[key][m][1] <= timestamp: 
                    ans = self.d[key][m][0]
                    l = m + 1
                else: 
                    r = m - 1
        return ans
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

