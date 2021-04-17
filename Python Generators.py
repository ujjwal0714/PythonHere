# --- --- ---
# Python Generator Functions
# --- --- ---
# a generator function returns an object which we can iterate over.
# generator functions contain one or more yield statements.
# we can iterate through items using next() function as python automatically implements __iter__() and __next__() funtions.
# function is paused and control is transferred to caller once the function yields.
# StopIteration exception is raised on further calls.
# while a return statement terminates a function entirely, yield statement pauses the function saving all its states and later continues from there on successive calls.
# --- --- --- 
# generator function
def f():
    n=1
    yield(n)
    n+=1
    yield(n)
    yield(n)
    n+=1
    yield(n)
        # --- --- ---
print(f()) # returns an object which we can iterate over
a=f()
        # --- --- ---
# method 1 to iterate over a
print(next(a))  
print(next(a))
print(next(a))
print(next(a))
# """ print(next(a))  # raises StopIteration exception.
        # --- --- ---
# method 2 to iterate over a
for i in f():  
    print(i)

# --- --- ---
# a generator object can only be iterated once. for further iterations, we need to create another generator object.
# --- --- ---
# P: printing elements of a string by use of generator function.
def g(b):
    for i in b:
        yield(i)

for j in g("hello"):
    print(j)

# --- --- ---
# [Generator Expressions]
# List Comprehension and Generator Expressions are very similar.
# the major difference between a List Comprehension and a Generator Expression is that a List Comprehension produces the entire list while the Generator Expression produces one item at a time.
# the generator expression have lazy execution as they produce output one element at a time and when asked for.
gen=(i**2 for i in range(3))
print(gen)  # returns Generator Object.
print(next(gen))  # returns 0
print(next(gen))  # returns 1
print(next(gen))  # returns 4
# """ print(next(gen))  # raises StopIteration exception.

# --- --- ---
# [Pipelining Generators]
def fibonacci_numbers(nums):
    x, y = 0, 1
    for _ in range(nums):
        x, y = y, x+y
        yield x
        # --- --- ---
def square(nums):
    for num in nums:
        yield num**2
        # --- --- ---
print(sum(square(fibonacci_numbers(10)))) # Pipelining

# --- --- ---
