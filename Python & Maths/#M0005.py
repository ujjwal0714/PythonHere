# generate n terms of fibonacci series iteratively.

# --- --- ---
def f(n):  # iterative
    a,b=0,1
    c=0
    l=[]
    while c<n:
        c+=1
        a,b=a+b,a
        l.append(a)
    return(l)

# --- --- ---

    
