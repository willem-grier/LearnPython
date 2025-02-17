'''
List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.
'''


x = ["geeks", "for", "geeks"]  # list 
x = ("geeks", "for", "geeks")  # tuple
x = {"geeks", "for", "geeks"} # set
x = {"name": "Suraj", "age": 24} # dict


li = ['apple', 'orange', 'peach']
li[1:2] = ['kiwi', 'grapefruit']
# ['apple', 'kiwi', 'grapefruit', 'peach']

# list operations
li.insert(0, 'grape')
li.pop(1) # remove by index
li.remove('peach') # remove by value
li.append('orange')
li.extend(li)

li.remove('grapefruit') # removes only first instance
print(li)
li.sort()

del li[2] # delete list items

[print(x) for x in li]

# Join Lists
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

list3.clear() # remove all items from list
print(list3)

# Reverse List Order
li.reverse()

# Copy a List
li2 = li.copy()
li2 = list(li)
li2 = li[:]




# Tuple items cannot be changed.
# However, the workaround is:
mytuple = (0, 1, 2)
li = list(mytuple)
li.append(3)
newtuple = tuple(li)
del newtuple, mytuple, li

# Tuples can be added to form a new tuple
t1 = (0,1,2)
t2 = (3,4,5)
t3 = t1 + t2
print(t3)

t3 = t1 * 3
print(t3)


# Unpacking Tuples
fruits = ('apple', 'banana', 'cherry', 'grape')
(x, *y, z) = fruits
print(y)











# Sets
fruits = {"apple", "banana", "cherry", "grape"}
# Add item
fruits.add("peach")
# Remove item
fruits.remove("peach")
fruits.discard("peach") # does not throw an error if the item doesn't exist

# Add multiple items from another collection (set, list, tuple)
other_fruits = ["pineapple", "mango"]
fruits.update(other_fruits)

s3 = fruits.union(other_fruits) # return the combination of two sets
s4 = s3 | fruits | fruits # combine sets

s5 = fruits.intersection(other_fruits) # keep only duplicates

fruits.clear() # remove all members





# Dictionaries
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# Access
print(car.get("model"))
# Modify
car["year"] = 1988
# Add new field
car["color"] = "red"
# Update (modify and add fields)
car.update({
  "year": 1988,
  "miles": 22000
})
# Remove
car.pop("miles")
# or
del car["brand"]

# Duplicate
car2 = car.copy()
car3 = dict(car2)

# Loop
for x in car.values():
  pass
for x in car.keys(): # or "for x in car:"
  pass
for key, value in car.items():
  pass