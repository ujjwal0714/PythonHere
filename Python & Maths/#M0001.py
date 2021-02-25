# calculation of z=y+(y/(x+(y/(x+...)))) till n steps.

# ----- ----- -----
def f(x,y,n):  # recursive approach.
   if n==0:
      return(y)
   else:
      return((y/(x+f(x,y,n-1))))

print(f(2,1,20))

# ----- ----- -----
def g(x,y):  # formulated approach when n is taken infinity.
   import math as m
   a=(x**2)+(4*y)
   return((m.sqrt(a)-x)/2)

print(g(1,1))
print(g(1,2))

# ----- ----- -----
