class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        rels = {')':'(',
                ']':'[',
                '}':'{'}
        
        chars = []

        for char in s:
            if char in rels:
                if len(chars)>0 and chars[-1] == rels[char]:
                    del chars[-1]
                else:
                    return False
            else:
                chars.append(char)
        if chars:
            return False
        else:
            return True

if __name__ == "__main__":
    sol = Solution()
    print(sol.isValid(""))
    print(sol.isValid("()"))
    print(sol.isValid("()[]{}"))
    print(sol.isValid("([)]"))
    print(sol.isValid("{[]}"))
    print(sol.isValid("["))
    print(sol.isValid("]"))