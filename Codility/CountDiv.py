def solution(A, B, K):
    count = 0
    for num in range(A, B+1):
        if num % K == 0:
            count += 1
    return count

def solution2(A, B, K):
    count = 0
    num = A

    if K == 1:
        return B - A + 1

    while num <= B:
        if num % K == 0:
            count += 1
            num = num + K
        else:
            num += 1
    return count


    
if __name__ == '__main__':
    print(solution3(3,10,2))
    print(solution3(6,11,2))
    print(solution3(6,11,1))
