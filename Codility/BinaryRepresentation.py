# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # write your code in Python 3.6
    binary = str(bin(N))[2:]
    print(binary)
    gap = 0

    for i in range(len(binary)-2, 0, -1):
        needle = '1'+i*'0'+'1'
        if needle in binary:
            gap = i
            return gap
    return gap



if __name__ == '__main__':
    print(solution(50))
    print(solution(1041))
    print(solution(32))