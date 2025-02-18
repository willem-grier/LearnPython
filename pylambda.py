# lambda: keyword
# arguments: comma-separated list
# expression: single expression only



fun = lambda x,y: print(x,y)
fun(2,3)


isPos = lambda x: "Positive" if x > 0 else "Negative" if x < 0 else "Zero"
print(isPos(-2))

# List Comprehension
# [ expression for item in list if condition]
li = [lambda arg=x : arg * 10 for x in range(1,5) if x % 2] # li is a list of lambda functions that return integers
for i in li:
  print(i())

# Filter even numbers from a list
n = [1, 2, 3, 4, 5, 6]
# filter( function, list )
even = filter(lambda x: x % 2 == 0, n) # filter() returns an iterator
print(list(even)) # convert iterator to list

# Map( function, list )
# Example: Double each number in a list
a = [1, 2, 3, 4]
b = map(lambda x: x * 2, a) # map() return an iterator
print(list(b)) # convert iterator to list

# reduce( function, iteratable [, initial])
# Example: Find the product of all numbers in a list
a = [1, 2, 3, 4]
from functools import reduce
b = reduce(lambda x, y: x * y, a, 10)
print(b)

