# calculte y=1+(1/(x+(1/(x+...)))) till n steps.

# ----- ----- -----
def f(x,n):  # recursive approach.
   if n==0:
      return(0)
   else:
      return((1/(x+f(x,n-1))))

print(f(2,100))

# ----- ----- -----
def g(x):  # formulated approach when n is infinity
   a=(x**2)+4
   return(((a**0.5)-x)/2)

print(g(2))

# ----- ----- -----
