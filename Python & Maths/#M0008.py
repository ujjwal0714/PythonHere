# return count of odd & even numbers in passed range (x,y) iteratively and efficiently. 
# --- --- ---
def f(x,y):  # return count of odd & even numbers in passed range (x,y) iteratively.
    if y<x:
        x,y=y,x
    c1=0  # count of odd numbers.
    c2=0  # count number of even numbers.
    for i in range(x,y+1):
        if i%2==0:
            c2+=1
        else:
            c1+=1
    return(c1,c2)

# --- --- ---
def g(x,y):  # optimised approach.
    if y<x:
        x,y=y,x
    a=(y-x)//2
    c1,c2=a,a  # c1 and c2 are count of odd and ecven numbers respectively.
    if (x%2==0 and y%2==0) or (x%2!=0 and y%2!=0):
        if y%2==0:
            c2+=1
        else:
            c1+=1
    else:
        c1+=1
        c2+=1
    return(c1,c2)

# --- --- ---
            
