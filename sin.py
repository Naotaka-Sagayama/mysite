path = './sin.txt'
f = open(path, 'w')

import math
#x = range (0,361)
#y = [math.sin(math.radians(theta)) for theta in x]

x=0
y=0
while x <= 2*math.pi:
    #y = math.sin(x)
    #y = math.sin(x)+math.sin(2*x)
    y = 1*math.sin(x)+0.333*math.sin(3*x)+0.2*math.sin(5*x)+0.143*math.sin(7*x)
    f.write(str(x)+"\t"+str(y)+"\n")
    x = x + 0.01