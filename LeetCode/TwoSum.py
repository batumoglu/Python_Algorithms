class Solution(object):
    def twoSum(self, nums, target):
        seen = {}
        output = []   

        for i in range(len(nums)):
            k = target - nums[i]
            if k in seen:
                output.append(seen[k])
                output.append(i)
  
                del seen[k]  
            else:
                seen[nums[i]] = i
        return output

class Solution2(object):
    """
    If there is exactly one solution
    """
    def twoSum(self, nums, target):
        h = {}
        for i, num in enumerate(nums):
            n = target - num
            if n not in h:
                h[num] = i
            else:
                return [h[n], i]

if __name__ == '__main__':
    sol = Solution()
    print(sol.twoSum([2,7,11,15], 9))
    print(sol.twoSum([3,3], 6))