def slow_max_slice(A):
    n = len(A)
    result = 0

    for p in range(n):
        for q in range(p, n):
            total = 0
            for i in range(p, q+1):
                total += A[i]
            result = max(result, total)
    return result

def quadratic_max_slice(A):
    n = len(A)
    result = 0
    for p in range(n):
        total = 0
        for q in range(p, n):
            total += A[q]
            result = max(result, total)
    return result

def golden_max_slice(A):
    max_ending = 0
    max_slice = 0
    for a in A:
        max_ending = max(0, max_ending + a)
        max_slice = max(max_slice, max_ending)
    return max_slice

if __name__ == '__main__':
    print(slow_max_slice([4,6,-5,1,2,-16,7]))
    print(quadratic_max_slice([4,6,-5,1,2,-16,7]))
    print(golden_max_slice([4,6,-5,1,2,-16,7]))