def solution(S):
    brDict = {  ']':'[',
                '}':'{',
                ')':'('}

    seen = []

    for char in S:
        if char in brDict:
            if len(seen) == 0 or brDict[char] != seen[0]:
                return 0
            else:
                seen.pop(0)
        else:
            seen.insert(0, char)
    if len(seen)==0:
        return 1
    else:
        return 0

def isValidPair(left, right):
    if left == '(' and right == ')':
        return True
    if left == '[' and right == ']':
        return True 
    if left == '{' and right == '}':
        return True   
    return False
 
def solution2(S):
    stack = []
     
    for symbol in S:
        if symbol == '[' or symbol == '{' or symbol == '(':
            stack.append(symbol)
        else:
            if len(stack) == 0:
                return 0
            last = stack.pop()
            if not isValidPair(last, symbol):
                return 0
     
    if len(stack) != 0:
        return 0
             
    return 1

def solution3(S):
    brDict = {  ']':'[',
                '}':'{',
                ')':'('}

    seen = []

    for char in S:
        if char in brDict:
            if len(seen) == 0 or brDict[char] != seen[-1]:
                return 0
            else:
                seen.pop()
        else:
            seen.append(char)
    if len(seen)==0:
        return 1
    else:
        return 0

if __name__ == '__main__':
    #print(solution("{[()()]}"))
    #print(solution("([)()]"))
    print(solution(")("))
