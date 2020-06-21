import math

def nextSquareRoot(num):
    if math.sqrt(num) // 1 == math.sqrt(num):
        return int(math.sqrt(num) // 1)
    else:
        return int(math.sqrt(num) // 1) + 1
    
    
def getArrangement(num):
    arr = []
    
    nsr = nextSquareRoot(num)
    while num != 0:
        row = min(nsr, num)
        num -= row
        arr += [row]
        
    return arr

for i in range(1,100):
    print(getArrangement(i))

