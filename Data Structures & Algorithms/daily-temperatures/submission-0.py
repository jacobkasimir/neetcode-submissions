class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        s = []
        res = [0] * (len(temperatures)) 
        for i in range(len(temperatures)):
            if not s:
                s.append(i)
            else:
                while(s and temperatures[s[-1]] < temperatures[i]):
                    res[s.pop()] = i - s[-1]
                s.append(i)
                    

        return res
                    
