def compress(s):
    count = {}
    r = ""

    for letter in s:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1
    
    for key, value in sorted(count.items()):
        r = r + str(key) + str(value)

    return r

from nose.tools import assert_equal

class TestCompress(object):

    def test(self, sol):
        assert_equal(sol(''), '')
        assert_equal(sol('AABBCC'), 'A2B2C2')
        assert_equal(sol('AAABCCDDDDD'), 'A3B1C2D5')
        print('ALL TEST CASES PASSED')


if __name__ == "__main__":
    t = TestCompress()
    t.test(compress)