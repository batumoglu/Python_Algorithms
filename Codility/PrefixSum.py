def prefix_sum(A):
    P = [0] * (len(A)+1)

    for k in range(1,len(A)+1):
        P[k] = P[k-1] + A[k-1]
    return P

def count_total(P, x, y):
    return P[y+1] - P[x]

def mushrooms(A, k, m):
    n = len(A)
    result = 0
    pref = prefix_sum(A)

    # m is max steps, k is start of array
    for p in range(min(m,k)+1):
        left_pos = k - p
        right_pos = min(n-1, max(k, k+m-2*p))
        result = max(result, count_total(pref, left_pos, right_pos))
    # (m+1) max steps, (n-k) is end of array
    for p in range(min(m+1, n-k)):
        right_pos = k + p
        left_pos = max(0, min(k, k- (m-2*p)))
        result = max(result, count_total(pref, left_pos, right_pos))
    return result

def slow_solution(A, k, m):
    n = len(A)
    result = 0
    # First right, then left
    for p in range(min(m+1, n-k)):
        right_pos = k+p
        left_pos = max(0, min(k, k-m+2*p))
        result = max(result, sum(A[left_pos: right_pos+1]))
    # First left, then right
    for p in range(min(m,k)+1):
        left_pos = k-p
        right_pos = min(n-1, max(k, k+m-2*p))
        result = max(result, sum(A[left_pos: right_pos+1]))
    return result

if __name__ == '__main__':
    #print(prefix_sum([1,2,3,4,5,6,7]))
    #print(mushrooms([1,2,3,4,5,6,7], 4, 6))
    print(mushrooms([2,3,7,5,1,3,9], 4, 6))
    print(slow_solution([2,3,7,5,1,3,9], 4, 6))