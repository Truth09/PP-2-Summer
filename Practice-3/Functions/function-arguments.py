# Arguments

def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

# Parameters vs Arguments

def my_function(name): # name is a parameter
  print("Hello", name)

my_function("Emil") # "Emil" is an argument

# Number of Arguments

def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")

# Default Parameter Values

def my_function(name = "friend"):
  print("Hello", name)

my_function("Emil")
my_function("Tobias")
my_function()
my_function("Linus")

# Keyword Arguments

def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function(animal = "dog", name = "Buddy")

# Positional Arguments

def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function("dog", "Buddy")

# Mixing Positional and Keyword Arguments

def my_function(animal, name, age):
  print("I have a", age, "year old", animal, "named", name)

my_function("dog", name = "Buddy", age = 5)

# Passing Different Data Types

def my_function(fruits):
  for fruit in fruits:
    print(fruit)

my_fruits = ["apple", "banana", "cherry"]
my_function(my_fruits)

# Positional-Only Arguments

def my_function(name, /):
  print("Hello", name)

my_function("Emil")

# Keyword-Only Arguments

def my_function(*, name):
  print("Hello", name)

my_function(name = "Emil")

# Combining Positional-Only and Keyword-Only

def my_function(a, b, /, *, c, d):
  return a + b + c + d

result = my_function(5, 10, c = 15, d = 20)
print(result)
