def hourGlass(arr):
    maxValue = float("-inf")
    for i in range(1,len(arr)-1):
        for j in range(1,len(arr[i])-1):
            value = arr[i][j] + arr[i-1][j-1] + arr[i-1][j] + arr[i-1][j+1] + arr[i+1][j-1] + arr[i+1][j] + arr[i+1][j+1]
            if value > maxValue:
                maxValue = value
    print(maxValue)
    return maxValue       

if __name__ == '__main__':
    hourGlass([[-9, -9, -9, 1, 1, 1],[0, -9, 0, 4, 3, 2],[-9, -9, -9, 1, 2, 3],[0, 0, 8, 6, 6, 0],[0, 0, 0, -2, 0, 0],[0, 0, 1, 2, 4, 0]])