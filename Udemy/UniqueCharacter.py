def uni_char1(s):
    return len(set(s)) == len(s)

def uni_char2(s):
    chars = set()
    for letter in s:
        if letter in chars:
            return False
        else:
            chars.add(letter)
    return True

from nose.tools import assert_equal

class TestUnique(object):
    def test(self, sol):
        assert_equal(sol(''), True)
        assert_equal(sol('goo'), False)
        assert_equal(sol('abcdefg'), True)
        print('ALL TEST CASES PASSED')
        
if __name__ == "__main__":
    t = TestUnique()
    t.test(uni_char1)

    t = TestUnique()
    t.test(uni_char2)