import math
#the function to be integrated:
def f(x):

  m=abs(math.sin(x))

  return m
 
#define a function to do integration of f(x) btw. a and b:
def I(f, n, a, b):
    h = (b - a) / float(n)
    intgr = 0.0
    for i in range(1, int(n)):

      intgr = intgr + h * f(h*(float(i)+1/2)+a)

    return intgr


l=[10,100,100,1000,10000,100000,1000000]
results=[]
a=0
b=3.14159
for i in l:
  integ=I(f,i,a,b)
  results.append(integ)
  print (integ)