# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    bag = set()

    for number in A:
        if number in bag:
            bag.remove(number)
        else:
            bag.add(number)
    return bag.pop()

if __name__ == '__main__':
    print(solution([4,6,1,3,4,6,1]))