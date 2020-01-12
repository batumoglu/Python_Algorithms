# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    A = sorted(A)
    maxProduct = float('-inf')
    
    if A[0] * A[1] * A[-1] > maxProduct:
        maxProduct = A[0] * A[1] * A[-1]
    if A[-1] * A[-2] * A[-3] > maxProduct:
        maxProduct = A[-1] * A[-2] * A[-3]
    
    return maxProduct