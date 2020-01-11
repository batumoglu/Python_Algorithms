# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
def syncValue(S):
    values = [0] * len(S)
    myDict = {'A': 1, 'C': 2, 'G':3, 'T':4}
    for i in range(len(S)):
        values[i] = myDict[S[i]]
    return values

def solution(S, P, Q):
    values = syncValue(S)
    res = [0] * len(P)
    for i in range(len(P)):
        res[i] = min(values[P[i]:Q[i]+1])
    return res

    
if __name__ == '__main__':
    print(solution('CAGCCTA', [2,5,0], [4,5,6]))