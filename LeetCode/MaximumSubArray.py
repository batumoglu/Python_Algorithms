class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curSum = 0
        maxSum = float('-inf')
        
        for num in nums:
            curSum = max(num, curSum+num)
            if curSum > maxSum:
                maxSum = curSum
        return maxSum
    
if __name__ == '__main__':
    sol = Solution()
    print(sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
    print(sol.maxSubArray([]))
    print(sol.maxSubArray([-4,-6,-3,-7,-9,-1]))