class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)<=1:
            return strs[0]
        strs.sort()
        for i in range(len(strs[0])):
            if strs[-1][i] != strs[0][i]:
                    return strs[0][:i]
        return strs[0] 