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

def solution2(A):
    min_idx = 0
    min_value = float('inf')
 
    for idx in range(0, len(A)-1):
        if (A[idx] + A[idx+1])/2.0 < min_value:
            min_idx = idx
            min_value = (A[idx] + A[idx+1])/2.0
        if idx < len(A)-2 and (A[idx] + A[idx+1] + A[idx+2])/3.0 < min_value:
            min_idx = idx
            min_value = (A[idx] + A[idx+1] + A[idx+2])/3.0
 
    return min_idx

if __name__ == '__main__':
    print(solution2([4,2,2,5,1,5,8]))