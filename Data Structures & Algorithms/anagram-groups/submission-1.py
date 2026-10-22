class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h = defaultdict(list)
        for string in strs:
            key = "".join(sorted(string))
            h[key].append(string)

        return list(h.values())
            

            
            