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

if __name__ == '__main__':
    #print(solution("{[()()]}"))
    #print(solution("([)()]"))
    print(solution(")("))
