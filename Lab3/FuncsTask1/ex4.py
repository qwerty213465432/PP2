def prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def filtprime(numbers):
    primenums = [num for num in numbers if prime(num)]
    return primenums


numbers = input()
list1 = list(map(int, numbers.split()))

primenums = filtprime(list1)
print( primenums)
