# return list of digits of a passed integer

# --- --- ---
def f(x):
    if x<0: x=-x
    if x==0: return([0])
    l=[]
    while x>0:
        l.append(x%10)
        x=x//10
    l.reverse()
    return(l)

# --- --- ---
def g(x):
    if x<0: x=-x
    l=[]
    for i in str(x):
        l.append(int(i))
    return(l)

# --- --- ---
