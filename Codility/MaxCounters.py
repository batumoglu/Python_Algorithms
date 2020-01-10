# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N, A):
    pos = [0] * N
    for i in range(len(A)):
        if A[i] == N+1:
            pos = [max(pos)] * N
        else:
            pos[A[i]-1] += 1
    return pos

def solution2(N,A):
    pos = [0] * N
    maxCount = 0
    for i in range(len(A)):
        if A[i] == N+1:
            pos = [maxCount] * N
        else:
            pos[A[i]-1] += 1
            if pos[A[i]-1] > maxCount:
                maxCount = pos[A[i]-1]
    return pos

def solution3(N, A):
    # write your code in Python 2.7

    M = len(A)
    counters = [0] * N

    max_result = max_counter = 0
    for ind in range(M):
        if A[ind] == N + 1:
            max_result = max(max_result, max_counter)
        else:
            if counters[A[ind] - 1] < max_result:
                counters[A[ind] - 1] = max_result

            counters[A[ind] - 1] += 1
            max_counter = max(max_counter, counters[A[ind] - 1])

    for ind in range(N):
        counters[ind] = max(max_result, counters[ind])

    return counters

if __name__ == '__main__':
    print(solution3(5,[3,4,4,6,1,4,4]))