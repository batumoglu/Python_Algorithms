def solution(A):
    profit = float('-inf')

    for i in range(len(A)):
        for j in range(i, len(A)):
            profit = max(profit, A[j]-A[i])
    return profit 


if __name__ == '__main__':
    print(solution([23171,21011,21123,21366,21013,21367]))