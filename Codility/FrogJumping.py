# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import math

def solution(X, Y, D):
    # write your code in Python 3.6
    distance = abs(X - Y)
    jumps = math.ceil(distance / D)
    return jumps

if __name__ == '__main__':
    print(solution(10, 85, 30))