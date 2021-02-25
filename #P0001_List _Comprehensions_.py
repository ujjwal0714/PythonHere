# list comprehensions

# list comprehensions make the code cleaner as well works faster than normal looping.

# ----- ----- -----
l=[i for i in range(10)]  # integer list from 0 to 10.

# this is equivalent to:
l1=[]
for i in range(10):
    l1.append(i)
    
# ----- ----- -----
m=[i**2 for i in range(10)]  # list of square of integers from 1 to 10.

# this is equivalent to:
m1=[]
for i in range(10):
    m1.append(i**2)
    
# ----- ----- -----
n=[print(1) for i in range(10)]  # print loop comprehended in a list.
# executing line 22 returns n=[None, None, None, None, None, None, None, None, None, None]
# this is equivalent to:
for i in range(10):
    print(1)
    
# ----- ----- -----
o=[i for i in range(10) for j in range(10)]  # double loops comprehended into lists.

# this is equivalent to:
o1=[]
for i in range(10):
    for j in range(10):
        o1.append(i)
        
# ----- ----- -----
p=[i.upper() for i in "splitted"]

# this is equivalent to:
p1=[]
for i in "splitted":
    p1.append(i.upper())

# ----- ----- -----
q=[i for i in ["apple","banana","papaya"] if "a" in i]  # using if condition in list comprehension.

# ----- ----- -----
r=[i if i%2==0 else i+1 for i in range(10)]  # if-else condition comprehended into list.

# this is equivalent to:
r1=[]
for i in range(10):
    if i%2==0:
        r1.append(i)
    else:
        r1.append(i+1)

# ----- ----- -----
