# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    idealSum = (len(A))*(len(A)+1)/2
    curSum = sum(A)
    if idealSum == curSum:
        return 1
    else:
        return 0

def solution2(A):
    A = sorted(A)

    for i in range(len(A)):
        if not i == A[i]-1:
            return 0
    return 1
if __name__ == '__main__':
    print(solution2([6,5,4,3,2,1]))
    print(solution2([4,3,2,1,7,6]))