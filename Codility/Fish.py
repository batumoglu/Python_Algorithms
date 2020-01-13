def solution(A, B):
    n = len(A)
    i = 0
    while i<n:
        if B[i] == 1 and B[i+1] == 0:
            if A[i] > A[i+1]:
                A.pop(i+1)
                B.pop(i+1)
            else:
                A.pop(i)
                B.pop(i)
        else:
            i += 1
        n = len(A)
    return n

def solution2(A, B):
    survivals = 0
    stack = []
     
    for idx in range(len(A)):
        if B[idx] == 0:
            while len(stack) != 0:
                if stack[-1] > A[idx]:
                    break
                else:
                    stack.pop()
                         
            else:
                survivals += 1
        else:
            stack.append(A[idx])
             
    survivals += len(stack)
     
    return survivals

if __name__ == '__main__':
    print(solution2([4,3,2,1,5],[0,1,0,0,0]))
    print(solution2([0,1],[1,1]))