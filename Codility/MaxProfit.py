def solution(A):
    profit = float('-inf')

    for i in range(len(A)):
        for j in range(i, len(A)):
            profit = max(profit, A[j]-A[i])
    return profit 

def solution2(A):
    max_profit = 0
    min_day = float('inf')
     
    for day in A:
        min_day = min(min_day, day)
        max_profit = max(max_profit, day-min_day)
     
    return max_profit

if __name__ == '__main__':
    print(solution2([23171,21011,21123,21366,21013,21367]))