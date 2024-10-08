"""
print("Hi")
a = 0
match a:
    case 1:
        print("One")
    case 2:
        print("Two")
    case _:                     #default
        print("No")
    
def f(a):
    def bar():
        print(a*7)
    bar()
f(8)

def mydecorator(f):
    def g():
        print("greet")
        f()
        print("bye")
    return g

@mydecorator
def d():
    print("Im here")

d()
#global, nonlocal переменные в функции global - изменение из внешнего кода, nonlocal - сделать не локальной переменную
"""
a = lambda y: y + 10
print(a(4))
