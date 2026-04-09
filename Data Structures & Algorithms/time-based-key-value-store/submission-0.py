class TimeMap:

# KEY VALUE SO HASHMAP

    def __init__(self):
        self.store  ={} # key = string, value = list of [val, timestep]
        

    def set(self, key: str, value: str, timestamp: int) -> None:

        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])

        
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store: 
            return ""
        
        l = 0 
        listSearch = self.store[key]
        r = len(listSearch) - 1
        big = 0
        
        res = ""

        
        while l<=r:
            mid = (l+r)//2
            if listSearch[mid][1] > timestamp: # timestampe at mid
                r = mid-1
            else:
                if listSearch[mid][1]> big:
                    res = listSearch[mid][0] # 0 is for value
                    big = listSearch[mid][1]

                l = mid + 1
        return res 



            
            
            
            
        
       

        
        
        
