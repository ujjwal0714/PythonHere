# return value of nCr when n and r are passed to function.

# --- --- ---
import math
m=math.factorial
def f(n,r):
    if n<r:
        return(False)  # undefined value.
    else:
        a=m(n)/(m(n-r)*m(r))
        return(int(a))

# --- --- ---

    
