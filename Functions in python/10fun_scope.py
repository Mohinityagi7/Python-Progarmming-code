# scope
x = 5 #global variable
def func():
    global x
    x = 7  # local variable
    return x
print(func())
print(x)
