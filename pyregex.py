import re

# Regex Docs
# https://www.w3schools.com/python/python_regex.asp

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
print(x)
print(x.pos)

x = re.search("in", txt)
print(x.span()) # tuple of index positions of the match
print(x.group()) # returns matched section of the string

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())
x = re.search(r"\bS.+", txt)
print(x.group())