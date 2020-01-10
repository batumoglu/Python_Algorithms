def solution(A):
    for i in range(1,len(A)+1):
        if i not in A:
            return i
    return len(A)+1

def solution2(A):
    pos = [0]*(len(A)+1)

    for i in range(len(A)):
        if A[i] < len(A)+1 and A[i]>0:
            pos[A[i]] += 1

    for i in range(1,len(pos)):
        if pos[i] == 0:
            return i
    return i+1

if __name__ == '__main__':
    print(solution2([1,3,6,4,1,2]))
    print(solution2([1,2,3]))
    print(solution2([-1,-3]))
    print(solution2([2]))
    print(solution2([-1]))