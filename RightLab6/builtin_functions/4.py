import time, math

def root(number, ms):
    time.sleep(ms / 1000)  
    square_root = math.sqrt(number)
    print(f"Square root of {number} after {ms} ms is {square_root}")


number = int(input())
mills = int(input())
root(number, mills)
