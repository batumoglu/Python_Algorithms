class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        needLen = len(needle)
        if needLen == 0:
            return 0

        for i in range(len(haystack)-needLen+1):
            if haystack[i:i+needLen] == needle:
                return i
        return -1


if __name__ == '__main__':
    sol = Solution()
    print(sol.strStr('hello', 'll'))
    print(sol.strStr('abcdesa', 'dd'))
    print(sol.strStr('You can find you needle in here', 'needle'))
    print(sol.strStr('', 'll'))
    print(sol.strStr('a', 'a'))
    print(sol.strStr('mississippi', 'pi'))