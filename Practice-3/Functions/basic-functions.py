# Basic functions

def my_function():
  print("Hello from a function")

# Calling a function

def my_function():
  print("Hello from a function")

my_function()

# Why use functions? Reusability

def fahrenheit_to_celsius(fahrenheit):
  return (fahrenheit - 32) * 5 / 9

print(fahrenheit_to_celsius(77))
print(fahrenheit_to_celsius(95))
print(fahrenheit_to_celsius(50))

# Return value

def get_greeting():
  return "Hello from a function"

message = get_greeting()
print(message)
print(get_greeting())

# The pass Statement

def my_function():
  pass
