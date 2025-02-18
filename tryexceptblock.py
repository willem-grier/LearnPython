try:
  print('Try')
  raise Exception('Custom Exception')
except NameError as e:
  print(e.args[0])
except Exception as e:
  print(e.args[0])
else:
  print('else: runs if there is no exception')
finally:
  print('finally: always runs')