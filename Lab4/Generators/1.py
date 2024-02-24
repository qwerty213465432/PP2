def SquaresRange(stop):
    start = 0
    while start < stop:
        yield start ** 2
        start += 1
        
x=int(input())
nums = list(SquaresRange(x))

print(nums)