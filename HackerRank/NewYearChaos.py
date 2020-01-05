"""
def minimumBribes(q):
    switches = {}
    for i in range(len(q)):
        for i in range(len(q)-1, 0, -1):
            for j in range(i):
                if q[j] > q[j+1]:
                    temp = q[j]
                    q[j] = q[j+1]
                    q[j+1] = temp
                    if q[j] in switches:
                        switches[q[j]] += 1
                    else:
                        switches[q[j]] = 1
                    if switches[q[j]] > 2:
                        return "Too chaotic"
    print(switches)
    return sum(switches.values())
"""

def minimumBribes(Q):
    moves = 0 
    Q = [P-1 for P in Q]
    for i,P in enumerate(Q):
        if P - i > 2:
            print("Too chaotic")
            return
        for j in range(max(P-1,0),i):
            if Q[j] > P:
                moves += 1
    print(moves)

if __name__ == '__main__':
    minimumBribes([2,1,5,3,4])
    minimumBribes([2,5,1,3,4])
