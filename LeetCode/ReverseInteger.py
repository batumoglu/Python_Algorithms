class Solution(object):
    def reverse(self, x):
        if x > 0:
            myStr = str(x)
            rev = myStr[::-1] 
        else:
            x = abs(x)
            myStr = str(x)
            rev = '-'+myStr[::-1]
        rev = int(rev)

        if rev > 2147483648 or rev < -2147483648:
            return 0
        else:
            return rev
        

if __name__ == '__main__':
    sol = Solution()
    print(sol.reverse(1534236469))
    print(sol.reverse(12345))
    print(sol.reverse(-12345))
    print(sol.reverse(-120))