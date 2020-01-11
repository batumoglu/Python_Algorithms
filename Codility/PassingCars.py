# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
def prefix(A):
    pref = [0] * (len(A)+1)
    for i in range(1, len(A)+1):
        pref[i] = pref[i-1] + A[i-1]
    return pref

def countTotal(P, left, right):
    return P[right] - P[left]

def solution(A):
    pref = prefix(A)
    n = len(A)
    pairs = 0
    for i in range(len(A)):
        if A[i] == 0:
            pairs += countTotal(pref, i, n)
        if pairs > 1000000000:
            return -1
    return pairs




if __name__ == '__main__':
    #print(solution([0,0,0,0,1,1,1,0,1,0,1,0,1,0]))
    print(solution([0,1,0,1,1]))