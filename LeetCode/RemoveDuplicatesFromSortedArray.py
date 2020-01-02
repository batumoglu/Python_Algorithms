class Solution(object):
    def removeDuplicates(self, nums):
        myLen = len(nums)
        i = 0
        while i < myLen:
            if nums[i-1] == nums[i] and myLen > 1:
                nums.remove(nums[i])
                myLen = len(nums)
            else:
                i += 1
        return myLen

if __name__ == '__main__':
    sol = Solution()
    print(sol.removeDuplicates([1,2,2,3,4,4,4,5]))
    print(sol.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
    print(sol.removeDuplicates([1,1]))
