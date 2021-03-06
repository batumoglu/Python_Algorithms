def solution(A):
    n = len(A)
    size = 0
    for k in range(n):
        if size == 0:
            size += 1
            value = A[k]
        else:
            if value != A[k]:
                size -= 1
            else:
                size += 1
    candidate = -1
    if size > 0:
        candidate = value
    leader = -1
    count = 0
    for k in range(n):
        if A[k] == candidate:
            count += 1
    if count > n/2:
        leader = candidate
    else:
        return -1
    for i in range(n):
        if A[i] == leader:
            return i

if __name__ == '__main__':
    print(solution([3,4,3,2,3,-1,3,3]))