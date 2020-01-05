class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        nums1.extend(nums2)
        nums1.sort()

        arrayLen = len(nums1)
        givenLen = m + n
        a = []

        for i in range(0, arrayLen):
            if nums1[i] == 0 and arrayLen>givenLen:
                a.append(i)
                arrayLen -= 1

        for i in a[::-1]:
            nums1.pop(i)

        return nums1

if __name__ == '__main__':
    sol = Solution()
    print(sol.merge([2,3,4,3],4,[4,2,1,3,4],5))
    print(sol.merge([],0,[],0))

    print(sol.merge([1,2,3,0,0,0],3,[2,5,6],3))