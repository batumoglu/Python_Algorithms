import math

def add_patch():
    # Write the code that goes here
    module = __import__("math")
    def log100(num):
        return math.log(num, 100)
        setattr(module, "log100", log100)
        
# Example case.
# add_patch()      
# print(math.log100(10))
print(add_patch())
print(math.log100(10))