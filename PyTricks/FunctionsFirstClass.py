# Functions are first-class citizens in Python:

# They can be passed as arguments to other functions,
# returned as values from other functions, and
# assigned to variables and stored in data structures.

def myFunc(a, b):
    return a+b

if __name__ == '__main__':
    funcs = [myFunc]
    print(funcs[0](2,3))