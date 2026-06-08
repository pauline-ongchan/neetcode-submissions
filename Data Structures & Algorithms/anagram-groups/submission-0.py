class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}
        for word in strs:
            key = "".join(sorted(word))
            if key not in group:
                group[key] = []
            group[key].append(word)
        return list(group.values())




        # ans = []
        # curr =[]
        # working =[]
        # # divide list by length 
        # # take the first
        # # compare the length, if equal
        #     # if it doesnt exist yet, add to hashmap 
        #     # if it exists, can skip 
        # # if not equal, 
        #     # 

        

        # for x in range(len(strs)):
        #     length = len(strs[0])
        #     for j in range(x+1, len(strs)):
        #         if len(strs[x]) == len(strs[j]):
        #             countI, countJ = {}, {}
        #             for i in range(len(strs[x])):
        #                 countI[strs[i]] = 1 + countI.get(strs[i], 0)
        #                 countJ[strs[j]] = 1 + countJ.get(strs[j], 0)
        #             if countI == countJ:
        #                 curr.append(strs[i])
        #                 curr.append(strs[j])
                
        #     ans.append(curr) 
        # return ans
        # #for those with same length, check each character frequency

        # #if the same, then same list
        
        