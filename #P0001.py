# return digits of a passed integer.

# --- --- ---

def f(x):
    if x<0:
        x=-x
    l=[]
    while x>0:
        d=x%10
        l.append(d)
        x=x//10
    l.sort()
    return(l)

# --- --- ---
