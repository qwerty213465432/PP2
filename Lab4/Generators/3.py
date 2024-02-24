def neednum(n):
    for num in range(n):
        if num % 3 == 0 and num % 4 == 0:
            yield num
            
            
def fun():
    n = int(input())
    nums = neednum(n)
    for num in nums:
        print(num, end=", " )
        
  
fun()
