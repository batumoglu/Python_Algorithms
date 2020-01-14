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



if __name__ == '__main__':
    print(slowLeader([5,1,5,2,5,3,5,4,5,6,5,7,5,8,5,9,5]))