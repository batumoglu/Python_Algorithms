def solution(S):
    seen = 0

    for char in S:
        if char == ')':
            if seen==0:
                return 0
            else:
                seen -= 1
        else:
            seen += 1
            
    if seen == 0:
        return 1
    else:
        return 0

if __name__ == '__main__':
    print(solution('(()(())())'))
    print(solution('())'))
    print(solution(')('))