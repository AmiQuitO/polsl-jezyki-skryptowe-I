import random

def Monte_Carlo(n):
    pointsin = 0
    for i in range(n):
        x = random.uniform(-1,1)
        y = random.uniform(-1,1)
        if x**2 + y**2 <= 1:
            pointsin += 1
    print(4*pointsin/n)

Monte_Carlo(1000)
Monte_Carlo(10000)
Monte_Carlo(100000)
Monte_Carlo(1000000)
