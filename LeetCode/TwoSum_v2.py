class Solution(object):
    def twoSum(self, numbers, target):
        myDict = {}
        for i, num in enumerate(numbers):
            value = target - num
            if value in myDict:
                return [myDict[value], i]
            else:
                myDict[num] = i

if __name__ == '__main__':
    sol = Solution()
    print(sol.twoSum([2,7,11,15], 9))
    print(sol.twoSum([3,3], 6))