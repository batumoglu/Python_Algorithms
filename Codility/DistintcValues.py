def solution(A):
    seen = set()
    for num in A:
        if num not in seen:
            seen.add(num)
    return len(seen)

if __name__ == '__main__':
    print(solution([1,2,2,3,4,4,5,6,6,6,7,8]))