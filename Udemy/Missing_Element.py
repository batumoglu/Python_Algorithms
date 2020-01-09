def finder1(arr1, arr2):
    return sum(arr1)-sum(arr2)

def finder2(arr1, arr2):
    count = 0
    for num in arr1:
        count += num

    for num in arr2:
        count -= num
    return count

def finder3(arr1, arr2):
    arr1 = sorted(arr1)
    arr2 = sorted(arr2)

    for num1, num2 in zip(arr1, arr2):
        if num1 != num2:
            return num1

from nose.tools import assert_equal

class TestFinder(object):
    
    def test(self,sol):
        assert_equal(sol([5,5,7,7],[5,7,7]),5)
        assert_equal(sol([1,2,3,4,5,6,7],[3,7,2,1,4,6]),5)
        assert_equal(sol([9,8,7,6,5,4,3,2,1],[9,8,7,5,4,3,2,1]),6)
        print('ALL TEST CASES PASSED')

if __name__ == "__main__":
    t = TestFinder()
    t.test(finder1)
    t.test(finder2)
    t.test(finder3)