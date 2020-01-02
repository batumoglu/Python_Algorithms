class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        myDict = {}
        myDict['I'] = 1
        myDict['V'] = 5
        myDict['X'] = 10
        myDict['L'] = 50
        myDict['C'] = 100
        myDict['D'] = 500
        myDict['M'] = 1000

        total = 0
        i = 0

        while i < len(s)-1:
            if s[i] == 'I':
                if s[i+1] == 'V':
                    total = total + 4
                    i += 2
                elif s[i+1] == 'X':
                    total = total + 9
                    i += 2
                else:
                    total = total + 1
                    i += 1
            elif s[i] == 'X':
                if s[i+1] == 'L':
                    total = total + 40
                    i += 2
                elif s[i+1] == 'C':
                    total = total + 90
                    i += 2
                else:
                    total = total + 10
                    i += 1
            elif s[i] == 'C':
                if s[i+1] == 'D':
                    total = total + 400
                    i += 2
                elif s[i+1] == 'M':
                    total = total + 900
                    i += 2
                else:
                    total = total + 100
                    i += 1
            else:
                total = total + myDict[s[i]]
                i += 1
        if i == len(s)-1:
            total = total + myDict[s[i]]
        return total

class Solution2(object):
    def romanToInt(self, s):
        myDict = {  'I':1,
                    'V':5,
                    'X':10,
                    'L':50,
                    'C':100,
                    'D':500,
                    'M':1000}
        
        out = 0
        last_char = s[0]
        queue = myDict[last_char]

        for char in s[1:]:
            char_val = myDict[char]

            if myDict[last_char] < char_val:
                queue = char_val - queue
            else:
                out = out + queue
                queue = char_val
            last_char = char
        return queue + out
        

if __name__ == '__main__':
    sol = Solution2()
    print(sol.romanToInt('IV'))
    print(sol.romanToInt('CXLII'))
    print(sol.romanToInt('MCMXCVIII'))
            
