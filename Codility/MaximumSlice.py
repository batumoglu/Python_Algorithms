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

if __name__ == '__main__':
    print(slow_max_slice([4,6,-5,1,2,-16,7]))
    print(quadratic_max_slice([4,6,-5,1,2,-16,7]))