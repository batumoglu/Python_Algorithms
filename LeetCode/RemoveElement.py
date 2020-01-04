class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        
        while val in nums:
            nums.remove(val)
        
        return len(nums)
    

if __name__ == '__main__':
    sol = Solution()
    print(sol.removeElement([1,2,3,4,5,4,3,2],2))
    print(sol.removeElement([],2))
    print(sol.removeElement([2,2,2,2,2,2,2,2,2],2))