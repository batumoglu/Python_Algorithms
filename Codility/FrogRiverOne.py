# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, A):
    pos = [0] * (X+1)
    pos[0] = 1
    count = 0

    for i in range(len(A)):
        if pos[A[i]] == 0:
            pos[A[i]] = 1
            count += 1
        if count == X:
            return i
    return -1

if __name__ == '__main__':
    print(solution(5, [1,4,3,5,4,1,3,2,5,4,3]))