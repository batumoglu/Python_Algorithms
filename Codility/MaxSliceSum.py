def solution(A):
    curSlice = float('-inf')
    maxSlice = float('-inf')

    for num in A:
        curSlice = max(num, curSlice+num)
        maxSlice = max(curSlice, maxSlice)

    return maxSlice

if __name__ == '__main__':
    print(solution([3,2,-6,4,0]))
    print(solution([-10]))
