import json

# JSON objects are represented as dictionaries in Python

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse string to dictionary:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])

# json to string
# json.dumps(y, indent=4)

print(json.dumps({"name": "John", "age": 30}, indent=4, separators=(";","=")))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))