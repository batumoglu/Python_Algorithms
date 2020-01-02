class Solution(object):
    def isPalindrome(self, s):
        s = s.lower()
        s = "".join([ c if c.isalnum() else '' for c in s ])

        rev = s[::-1]
        if rev == s:
            return True
        return False

if __name__ == '__main__':
    sol = Solution()
    print(sol.isPalindrome('A man, a plan, a canal: Panama'))
    print(sol.isPalindrome('race a car'))
    print(sol.isPalindrome('ab@a'))
