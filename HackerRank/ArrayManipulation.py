def arrayManipulation2(n, queries):
    arr = [0]*n
    for i in range(len(queries)):
        start = queries[i][0]-1
        end = queries[i][1]-1
        value = queries[i][2]

        arr[start:end]
        for j in range(n):
            if j >= start and j <= end:
                arr[j] = arr[j] + value
    return max(arr)

def arrayManipulation(n, queries):
    array = [0] * (n+1)
    
    for query in queries: 
        start = query[0] - 1
        end = query[1]
        value = query[2]
        array[start] += value
        array[end] -= value
        
    max_value = 0
    running_count = 0
    for i in array:
        running_count += i
        if running_count > max_value:
            max_value = running_count
            
    return max_value


if __name__ == '__main__':
    #print(arrayManipulation(10, [[1,5,3],[4,8,7],[6,9,1]]))
    #print(arrayManipulation(5, [[1,2,100],[2,5,100],[3,4,100]]))
    print(arrayManipulation(10, [[2,6,8],[3,5,7],[1,8,1],[5,9,15]]))