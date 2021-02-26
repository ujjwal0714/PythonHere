# recursive and iterative calculation of factorial.

def f(x):  # recursive
  if x==0:
    return(1)
  return(x*f(x-1))

def g(x):  # iterative
  if x>=0:
    p=1
  else:
    return(False)  # Factorial Not Defined
  while x>0:
    p*=x
    x-=1
  return(p)
