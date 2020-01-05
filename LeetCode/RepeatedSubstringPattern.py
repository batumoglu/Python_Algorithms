class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        root = ""
        for i in range(int(len(s)/2)):
            root += s[i]
            piece = int(len(s)/len(root))
            if s == root * piece:
                return True
        return False

if __name__ == '__main__':
    sol = Solution()
    print(sol.repeatedSubstringPattern('abcabcabcabc'))
    print(sol.repeatedSubstringPattern('a'))
    print(sol.repeatedSubstringPattern('abcdaabcdaabcda'))
    print(sol.repeatedSubstringPattern('abc'))