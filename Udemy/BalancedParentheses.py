def balance_check(s):
    chars = []
    matches = { ')':'(',
                ']':'[',
                '}':'{'}

    for c in s:
        if c in matches:
            if chars.pop() != matches[c]:
                return False
        else:
            chars.append(c)
    return chars == []

from nose.tools import assert_equal

class TestBalanceCheck(object):
    
    def test(self,sol):
        assert_equal(sol('[](){([[[]]])}('),False)
        assert_equal(sol('[{{{(())}}}]((()))'),True)
        assert_equal(sol('[[[]])]'),False)
        print ('ALL TEST CASES PASSED')
        
if __name__ == '__main__':
    t = TestBalanceCheck()
    t.test(balance_check)