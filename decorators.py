'''
Decorators are often used in scenarios such as logging, 
authentication and memorization, allowing us to add additional 
functionality to existing functions or methods in a clean, reusable way.

A decorator takes another function as its argument, and enhances its functionality in some way.
'''

import time


def my_decorator(func):
  def my_logger():
    print('Before')
    func()
    print('After')
  return my_logger

@my_decorator # apply decorator to greet function
def greet():
  print("Hello World!")

greet()


def timer(func):
  def time_func():
    start = time.time()
    func()
    end = time.time()
    print("-- Elapsed Time = {:.2f} ms --".format(end-start))
  return time_func

@timer
def greet():
  a = 1
  for _ in range(0, 100_000):
    a *= 2
  print("Hello World! (timed)")

greet()