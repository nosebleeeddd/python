# Regular Expressions
# Patterns that we can look for in strings
# or text.

import re

# Email Patterns Simplified
# \., escaped dot
# \-, escaped -
pattern = re.compile("^[a-zA-Z0-9\.\_]+@{1}[a-zA-Z0-9]+\.{1}[a-zA-Z]{2,3}$")
print(pattern.search("helloworld@gmail.com"))
print(pattern.search("mail_box@test.de"))
print(pattern.search("mymails@test.com"))
print(pattern.search("something@ting.com"))


# UPPER CASE ONLY
# ^$ , whole string must match from beginning,w/o finds anywhere inside string
# + , has to occur atleast once and can be as many times.
pattern = re.compile("^[A-Z]+$")
print(pattern.search("hello world"))
print(pattern.search("Hello World"))
print(pattern.search("HELLOWORLD"))                         #matches pattern


# ANY CASE W/ SPACE
# \s, can search for space in pattern
pattern = re.compile("^[a-zA-Z\s]+$")
print(pattern.search("hello WOrld"))
print(pattern.search("helloworld"))
print(pattern.search("hello World"))


# PATTERN #1
# {}, lets you set a limit
# ^ , second anchor says everything not in this, so special symbols here
pattern = re.compile("^[a-z]{3}[0-9]{3,5}[^a-zA-Z0-9]{1}[A-Z]{0,2}$")
print(pattern.search("hello WOrld"))
# 3 Lower case letters = [a-z]{3}
# 3-5 digits = [0-9]{3,5}
# one symbol = [^a-zA-Z0-9]{1}
# up to two uppercase characters = [A-Z]{0,2}


# PATTERN #2
# MATCHES ANY STRING WITH LENGTH OF 10
pattern = re.compile("^.{10}$")
print(pattern.search("123asd-212")
