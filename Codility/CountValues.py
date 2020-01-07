def solution(A):
    # write your code in Python 3.6
    bag = set()
    last = 0
    
    for i in range(len(A)):
        if A[i] not in bag:
            bag.add(A[i])
            last = i
    return last

if __name__ == '__main__':
    print(solution([1,3,4,2,5,4,3,2,1,3,4,5]))
    print(solution([]))
    print(solution([1,1,1,1,1,1,1]))