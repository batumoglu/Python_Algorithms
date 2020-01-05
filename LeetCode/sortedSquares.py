class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        B = []
        for num in A:
            B.append(num * num)
        return sorted(B)

class Solution2(object):
    def sortedSquares(self, A):
        return sorted([x*x for x in A])

if __name__ == '__main__':
    sol = Solution2()
    print(sol.sortedSquares([-4,5,2,8,-11]))
    print(sol.sortedSquares([-3,-6,-2,-1,-8]))
    print(sol.sortedSquares([]))