def Squares(a, b):
    for i in range(a, b +1):
        yield i ** 2

a = int(input())
b = int(input())

gen = Squares(a, b)

for square in gen:
    print(square, end=", ")
