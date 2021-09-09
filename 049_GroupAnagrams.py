class Solution:
    def groupAnagrams(self, strs):
        dict = {}
        for item in strs:
            key = tuple(sorted(item))
            dict[key] = dict.get(key, []) + [item]
            #print(dict)
        return list(dict.values())


print(Solution().groupAnagrams(strs = ["eat","tea","tan","ate","nat","bat"])) #[["bat"],["nat","tan"],["ate","eat","tea"]]
print(Solution().groupAnagrams(strs = [""]))
print(Solution().groupAnagrams(strs = ["a"]))