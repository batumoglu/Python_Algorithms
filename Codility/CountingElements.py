def slow_swap(A, B):
    """
    This is a N(O^2) solution
    """
    n = len(A)
    sumA = sum(A)
    sumB = sum(B)

    for i in range(n):
        for j in range(n):
            change = B[j] - A[i]
            sumA += change
            sumB -= change

            if sumA == sumB:
                return True, A[i], B[j]
            sumA -= change
            sumB += change
    return False

def counting(A, m):
    n = len(A)
    count = [0] * (m+1)
    for k in range(n):
        count[A[k]] += 1
    return count

def fast_swap(A, B, m):
    n = len(A)
    sumA = sum(A)
    sumB = sum(B)
    change = sumB - sumA

    if change%2 == 1:
        return False
    count = counting(A, m)
    for i in range(n):
        if 0 < B[i] - change and B[i] - change <= m and count[B[i]-change]>0:
            return True
    return False

def mySwap(A, B, m):
    sumA = sum(A)
    sumB = sum(B)
    change = sumB - sumA
    count = counting(A, m)

    for i in range(len(B)):
        seek = B[i] - change
        if count[seek] > 0:
            return True
    return False
        

if __name__ =='__main__':
    print(slow_swap([1,2,3,4],[2,3,4,5],5))
    print(fast_swap([1,2,3,4],[2,3,4,5],5))
    print(mySwap([1,2,3,4],[2,3,4,5],5))
