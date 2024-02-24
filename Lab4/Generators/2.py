def evens(n):
    for num in range(n):
        if num % 2 == 0:
            yield num
            
            
def fun():
    n = int(input())
    evnum = evens(n)
    for num in evnum:
        print(num, end=", " )
        
  
fun()
