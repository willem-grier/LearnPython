a = "Hello World!"

# Strings are arrays
# Indexing
print(a[3])
# Looping
for letter in a:
  print(letter, end=' ')
print()

# Search string for characters
if "!" in a:
  print(f"'{a}' contains '!'")


# Slicing
b = a[3:5]
b = a[5:]
b = a[:2]

# String Modification
b = a.upper()
b = a.lower()
b = a.strip() # remove whitespace
b = a.replace('H', 'h')
print(a.split())
# Concatenation
c = b + a

# String Formatting
price = 2.0
txt = f"The price is {price:.2f} dollars"