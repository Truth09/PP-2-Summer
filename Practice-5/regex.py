import re

txt = """
a

ab
abb
abbb
abbbbbbbbbbbb

ab_
abc_
hope_

Hope
Faith
Ashes
A
AA

arab
abba
aab
acb

no spaces, and also no dots.
"""

# 1. Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.

conc = re.findall(r"ab*", txt)

print(conc)

# 2. Write a Python program that matches a string that has an 'a' followed by two to three 'b'.

conc = re.findall(r"ab{2,3}\s", txt)

print(conc)

# 3. Write a Python program to find sequences of lowercase letters joined with a underscore.

conc = re.findall(r"[a-z]+_", txt)

print(conc)

# 4. Write a Python program to find the sequences of one upper case letter followed by lower case letters.

conc = conc = re.findall(r"[A-Z][a-z]+", txt)

print(conc)

# 5. Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.

conc = conc = re.findall(r"(a.*b)\s", txt)

print(conc)

# 6. Write a Python program to replace all occurrences of space, comma, or dot with a colon.

conc = re.sub(r"[ ,.]", 'X', txt)

print(conc)

# 7. Write a python program to convert snake case string to camel case string.

txt1 = "snakes_are_cute"

def snake2camel(txt):
	return re.sub(r'_([a-zA-Z])', lambda x: x.group(1).upper(), txt)

print(snake2camel(txt1))

# 8. Write a Python program to split a string at uppercase letters.

txt2 = "camelsAreAwesome"

conc = re.split(r"(?=[A-Z])", txt2)

print(conc)

# 9. Write a Python program to insert spaces between words starting with capital letters.

txt3 = "LookASharkIsBreaching!"

conc = re.sub(r"(?=[A-Z])", " ", txt3)

print(conc)

# 10. Write a Python program to convert a given camel case string to snake case.

def camel2snake(txt):
	return re.sub(r'([A-Z])', r'_\1', txt).lower()

print(camel2snake(txt2))
