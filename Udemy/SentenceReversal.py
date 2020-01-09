def rev_words1(s):
    return " ".join(reversed(s.split()))

def rev_words2(s):
    return " ".join(s.split()[::-1])

def rev_words3(s):
    words = []
    length = len(s)
    space = [' ']

    i = 0

    while i < length:
        if s[i] not in space:
            word_start = i

            while i < length and s[i] not in space:
                i += 1
            words.append(s[word_start:i])
        i += 1
    return " ".join(reversed(words))

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

    t = ReversalTest()
    t.test(rev_words3)