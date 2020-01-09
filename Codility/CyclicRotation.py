# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, K):
    # write your code in Python 3.6
    if not A:
        return A
    for i in range(K):
        value = A.pop(-1)
        A.insert(0, value)
    return A

def solution2(A, K):
    for i in range(K):
        last_value = A[-1]
        for j in range(len(A)-1, 0, -1):
            A[j] = A[j-1]
        A[0] = last_value
    return A


if __name__ == '__main__':
    print(solution([1,2,3,4,5], 3))
    print(solution2([1,2,3,4,5], 3))
    print(solution([], 1))
    print(solution2([4,2,8,6,0], 5))
