def myRange(stop):
    start = 0
    while start < stop:
        yield start
        start += 1
x=int(input())
nums = list(myRange(x+1))
num=nums[::-1]

print(num)