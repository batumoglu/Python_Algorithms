def large_cont_sum(arr): 
    maxSum = 0
    curSum = 0
    for num in arr:
        curSum = max(curSum+num, num)
        maxSum = max(maxSum, curSum)
    return(maxSum)

from nose.tools import assert_equal

class LargeContTest(object):
    def test(self,sol):
        assert_equal(sol([1,2,-1,3,4,-1]),9)
        assert_equal(sol([1,2,-1,3,4,10,10,-10,-1]),29)
        assert_equal(sol([-1,1]),1)
        print('ALL TEST CASES PASSED')
        
if __name__ == "__main__":
    t = LargeContTest()
    t.test(large_cont_sum)