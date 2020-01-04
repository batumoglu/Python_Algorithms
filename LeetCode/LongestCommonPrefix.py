class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = ""
        if strs:
            minLen = max(min(len(word) for word in strs),0)
        else:
            return prefix

        for i in range(minLen):
            check = set()
            for word in strs:
                letter = word[i]
                check.add(letter)
                if len(check)>1:
                    return prefix
            prefix += letter
        return prefix
        
if __name__ == '__main__':
    sol = Solution()
    print(sol.longestCommonPrefix(["flower","flow","flight"]))
    print(sol.longestCommonPrefix(["dog","racecar","car"]))
    print(sol.longestCommonPrefix([]))