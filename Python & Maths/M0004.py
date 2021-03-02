# return factors of integer passed.

# --- --- ---
def f(x):
    if x<0:
        x=-x
    l=[]
    for i in range(1,(x//2)+1):
        if x%i==0:
            l.append(i)
    l.append(x)
    return(l)

# --- --- ---
        
        
