def range_even(x,y):  # print even numbers in range (x,y).
    if x%2==0:
        for i in range(x,y,2):
            print(i,end=" ")
    elif x%2!=0:
        for i in range(x+1,y,2):
            print(i,end=" ")

def range_odd(x,y):  # print odd numbers in range (x,y).
    if x%2!=0:
        for i in range(x,y,2):
            print(i,end=" ")
    elif x%2==0:
        for i in range(x+1,y,2):
            print(i,end=" ")

def range_even2(x,y):  # print even numbers in range (x,y).
    for i in range(x,y):
        if i%2==0:
            print(i,end=" ")

def range_odd2(x,y):  # print odd numbers in range (x,y).
    for i in range(x,y):
        if i%2!=0:
            print(i,end=" ")
