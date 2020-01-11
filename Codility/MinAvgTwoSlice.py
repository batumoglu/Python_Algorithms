def solution(A):
    minAvg = [float('inf')] * len(A)
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            minAvg[i] = min(minAvg[i], sum(A[i:j+1])/(j-i+1))
    
    minValue = minAvg[0]
    count = 0
    
    for i in range(len(minAvg)):
        if minAvg[i] < minValue:
            minValue = minAvg[i]
            count = i
    return count

if __name__ == '__main__':
    print(solution2([4,2,2,5,1,5,8]))