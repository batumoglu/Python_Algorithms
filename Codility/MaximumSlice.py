def slow_max_slice(A):
    n = len(A)
    result = 0

    for p in range(n):
        for q in range(p, n):
            sum = 0
            for i in range(p, q+1):
                sum += A[i]
            result = max(result, sum)
    return result

if __name__ == '__main__':
    print(slow_max_slice([4,6,-5,1,2,-16,7]))