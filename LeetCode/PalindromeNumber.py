class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x >= 0:
            number = str(x)
            rev = number[::-1]
            if x == int(rev):
                return True
        return False

if __name__ == '__main__':
    sol = Solution()
    print(sol.isPalindrome(12321))
    print(sol.isPalindrome(120))
    print(sol.isPalindrome(-121))
