# recursive and iterative calculation of n^p.

# --- --- ---
def f(n,p):  # recursive
    if p==1:
        return(n)
    elif p==0:
        return(1)
    else:
        return(n*f(n,p-1))
    
# --- --- ---
def g(n,p):
    m=1
    while p>0:
       m*=n
       p-=1
    return(m)

# --- --- ---
    
