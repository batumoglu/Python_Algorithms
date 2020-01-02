class Solution(object):
    def validPalindrome(self, s):
        if s == s[::-1]:
            return True

        i = 0
        j = len(s)-1

        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                noi = s[:i] + s[(i+1):]
                noj = s[:j] + s[(j+1):]
                if noi == noi[::-1] or noj == noj[::-1]:
                    return True
                else:
                    return False
        return True

if __name__ == '__main__':
    sol = Solution()
    #print(sol.validPalindrome('abca'))
    #print(sol.validPalindrome('abcddcba'))
    print(sol.validPalindrome('pidbliassaqozokmtgahluruufwbjdtayuhbxwoicviygilgzduudzgligyviciowxbhuyatdjbwfuurulhagtmkozoqassailbdip'))
