class Node(object):
    def __init__(self, value):
        self.value = value
        self.next_node = None

def cycle_check(node):
    fast, slow = node, node
    while fast and fast.next_node:
        fast = fast.next_node
        if fast == slow:
            return True
    return False

from nose.tools import assert_equal

class TestCycleCheck(object):
    def test(self,sol):
        a = Node(1)
        b = Node(2)
        c = Node(3)

        a.next_node = b
        b.next_node = c
        c.next_node = a

        x = Node(1)
        y = Node(2)
        z = Node(3)

        x.next_node = y
        y.next_node = z

        assert_equal(sol(a),True)
        assert_equal(sol(x),False)
        
        print ("ALL TEST CASES PASSED")

if __name__ == '__main__':
    t = TestCycleCheck()
    t.test(cycle_check)
        