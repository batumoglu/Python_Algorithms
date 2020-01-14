def slowLeader(A):
    """
    O(n^2)
    """
    n = len(A)
    leader = -1
    for k in range(n):
        candidate = A[k]
        count = 0
        for i in range(n):
            if A[i] == candidate:
                count += 1
        if count > n/2:
            leader = candidate
    return leader

def fastLeader(A):
    n = len(A)
    leader = -1
    A.sort()
    candidate = A[int(n/2)]
    count = 0
    for i in range(n):
        if A[i] == candidate:
            count += 1
    if count > n/2:
        leader = candidate
    return leader

def goldenLeader(A):
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
    return leader


if __name__ == '__main__':
    print(slowLeader([5,1,5,2,5,3,5,4,5,6,5,7,5,8,5,9,5]))
    print(fastLeader([5,1,5,2,5,3,5,4,5,6,5,7,5,8,5,9,5]))
    print(goldenLeader([5,1,5,2,5,3,5,4,5,6,5,7,5,8,5,9,5]))