# r = read-only (default)
# w = write; overwrites pre-existing file; creates file if dne
# a = append; adds to existing content; create file if dne
# x = create file; error if file exists
# t = text mode (default)
# b = binary mode

f = open('test.txt', 'wt')
f.write('Hello World!')

f = open('test.txt', 'rt') 

num_chars = 4
print(f.read(num_chars))
print(f.readline())

# Loop through lines
for line in f:
  print(line)

try:
  file = open('test.txt', 'x')
  file.close()
except FileExistsError as e:
  print(e.args)


f.close()

# Delete files
import os
if os.path.exists('test.txt'):
  os.remove('test.txt')
else:
  print('File does not exist')