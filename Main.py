def says(say: str) -> str:
    return say

print(says("Main"))

def function2(func) -> str:
    return func

print(says("function 2"))

def function1(func: str) -> str:
    return func

print(function1("function 1"))