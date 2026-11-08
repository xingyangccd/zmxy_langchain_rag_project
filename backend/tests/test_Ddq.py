from pycparser.c_ast import TypeOf


def createData(n):
    for i in range(n):
        yield i
# iterator

a=createData(5)
print(type(a))

print(next(a))
print(next(a))
print(next(a))
