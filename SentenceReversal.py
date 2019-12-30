def rev_words1(s):
    return " ".join(reversed(s.split()))

def rev_words2(s):
    return " ".join(s.split()[::-1])

from nose.tools import assert_equal

class ReversalTest(object):
    
    def test(self,sol):
        assert_equal(sol('    space before'),'before space')
        assert_equal(sol('space after     '),'after space')
        assert_equal(sol('   Hello John    how are you   '),'you are how John Hello')
        assert_equal(sol('1'),'1')
        print("ALL TEST CASES PASSED")
        
# Run and test
if __name__ == "__main__":
    t = ReversalTest()
    t.test(rev_words1)

    t = ReversalTest()
    t.test(rev_words2)