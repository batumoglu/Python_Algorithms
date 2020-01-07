# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    idealSum = (len(A)+1)*(len(A)+2)/2
    arraySum = sum(A)
    return int(idealSum-arraySum)

if __name__ == '__main__':
    print(solution([9,8,6,5,1,2,4,3]))
    print(solution([1,3]))
    print(solution([2]))
