# function checks if passed argument is Harshad number or not.
# Harshad Numbers: https://en.wikipedia.org/wiki/Harshad_number

#----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- 
def sum_of_digits(a):
    summ=0
    if a<0: a=-a
    while a>0:
        dig=a%10
        a=a//10
        summ+=dig
    return(summ)
    
#----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- 
# main program
def is_harshad(b):
    if b%sum_of_digits(b)==0:
        return(True)
    else:
        return(False)

#----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- 
