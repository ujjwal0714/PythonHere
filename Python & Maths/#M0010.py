#----- ----- -----
# function prints sum of digits of passed argument.

#----- ----- -----
def sum_of_digits(a):
    s=0  # sum
    if a<0: a=-a
    while a>0:
        dig=a%10
        a=a//10
        summ+=dig
    return(summ)

#----- ----- -----
