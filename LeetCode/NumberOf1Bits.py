class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        binary = bin(n)
        print('Binary Value: ', binary)
        for digit in binary:
            if digit =='1':
                count += 1
        return count

if __name__ == '__main__':
    sol = Solution()
    print(sol.hammingWeight(34536))