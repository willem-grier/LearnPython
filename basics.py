# Data Types
x = "Hello World" # string
x = 50  # integer
x = 60.5  # float
x = 3j  # complex
x = ["geeks", "for", "geeks"]  # list 
x = ("geeks", "for", "geeks")  # tuple
x = {"name": "Suraj", "age": 24} # dict
x = {"geeks", "for", "geeks"} # set
x = True  # bool
x = b"Geeks" # binary

# Get Type
print(type(x))

# Multiple Assignment
a = b = c = 100 # all are equal to 100
a, b, c = 1, 2, 3 # multiple assignments are different, but on one line

# Command Line Input
# val = input("Enter a number: ") # string output
val = 3
# Output formatting types
print("You entered {:.2f}".format(float(val)))
# Sep and End (End will remove newline character)
print(f"You entered {val}", sep='-', end='END')
print("You entered %s" % (val))
print(f"You entered {val}") # easiest


# Taking three inputs at a time
# x, y, z = input("Enter three values separated by '-': ").split('-') # default split is SPACE
# print("inputs: ", x, y, z)

# If-Else Statement
x = 20
if (x < 20):
  print("x < 20")
elif (x == 20):
  print("x == 20")
else:
  print("x > 20")

# For Loop
for i in range(0,20,2):
  # do something
  pass

li = ["geeks", "for", "geeks"]
for i in li:
  print(i)
    
tup = ("geeks", "for", "geeks")
for i in tup:
  print(i)
    
s = "Geeks"
for i in s:
    print(i )
for i in range(0, len(s)):
   print(s[i])
    
d = dict({'x':123, 'y':354})
for i in d:
  print("%s  %d" % (i, d[i]))
    
set1 = {1, 2, 3, 4, 5, 6}
for i in set1:
  print(i)

# Nested loops
for i in range(1, 5):
    for j in range(i):
        print(i, end=' ') # use 'end' to remove newline character
    print()


# Continue and Break keywords in for loops
def isVowel(letter):
  return (letter == 'a') | (letter == 'e') | (letter == 'i') | (letter == 'o') | (letter == 'u')
for letter in "abzcde":
  if isVowel(letter):
    continue
  if letter == 'z':
    break
  print(f'Consonant: {letter}')

# Function definition
y = z = 20
def isEqual():
  global z
  y = 10
  if y == z:
    print(f"{y} == {z}")
  else:
    print(f"{y} != {z}")
isEqual()

def isOdd(x):
  return x % 2
# Type casting: int(), str(), bool(), float()
if isOdd(int(val)):
  print("{} is odd".format(val))
else:
  print("{} is even".format(val))

del y,z
# print(y,z) # NameError



# Inside For Loops
fruits = ["apple", "orange", "kiwi"]
iter_obj = iter(fruits)
while True:
  try:
    fruit = next(iter_obj)
    print(fruit)
  except StopIteration:
    break

num1 = "5"
num2 = 3
result = num1 * num2
print(result)


# Enhance readability
z = 1_000_000
print(type(z)) # integer

# Variable number of arguments
def addAll(*args):
  return sum(args)

def dictArgs(**kwargs):
  for k, val in kwargs.items():
    print(k,val)
dictArgs(a=1, b=2, c=3)

def fun(*args, **kwargs):
  print("Positional arguments: ", args) # tuple
  print("Keyword Arguments: ", kwargs)  # dictionary
fun(1,2,3,a=1,b=2,c=3)

# Default parameter value example
def my_function(country = "Norway"):
  print("I am from " + country)