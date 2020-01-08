# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
def solution(A):
    left = A[0]
    right = sum(A[1:])
    minDiff = abs(left-right)

    for i in range(1, len(A)):
        diff = abs(left-right)
        if minDiff>diff:
            minDiff = diff
        left += A[i]
        right -= A[i]
    return minDiff

if __name__ == '__main__':
    print(solution([5]))
    print(solution([5,9]))
    print(solution([1,2,3,4,5,6]))
    print(solution( [-10, -20, -30, -40, 100]))

