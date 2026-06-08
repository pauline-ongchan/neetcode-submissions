class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}
        for word in strs:
            key = "".join(sorted(word))
            if key not in group:
                group[key] = []
            group[key].append(word)
        
        result =[]
        for key,val in group.items():
            result.append(val)
        return result