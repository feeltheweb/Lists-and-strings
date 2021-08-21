# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 21:14:32 2021

@author: anind
"""

#LIST
l1 = [1, 2, 3, "dog", 4, 5]
l2 = [5, 8, 7]
print(l1[0])
print(l1[3])
print(l1[0:4])

#add an element
print(l1.append("cat"))
#delete an element
print(l1.remove("cat"))
#reverse
print(l1.reverse())
#pop
print(l1.pop(0))
#insert
print(l1.insert(1, 5))
#index
print(l1.index("dog"))
#extend
print(l1.extend(l2))
#count
print(l1.count(5))
#copy
print(l1.copy())
print(l2.copy())
#sort
print(l2.sort())
#clear
print(l2.clear())

#STRING
s1 = "hope you have a great day"
s2 = "hello\tbro"
s3 = "my name is {}, I'm {}"
s4 = "HEYA"
s5 = "\u0033"
s6 = "#"
s7 = "Mike", "Biber"
s8 = "Thank you\nmy scooty"
print(s1[5])

#capitalize
print(s1.capitalize())
#casefold
print(s1.casefold())
#centre
print(s2.center(15,))
#count
print(s1.count("hope"))
#encode
print(s1.encode())
#endswith
print(s1.endswith("."))
#expandtabs
print(s2.expandtabs(4))
#find
print(s1.find("great"))
#format
print(s3.format("Anand", 21))
#index
print(s1.index("e", 16))
#isalnum
print(s1.isalnum())
#isalpha
print(s4.isalpha())
#isdecimal
print(s5.isdecimal())
#isdigit
print(s1.isdigit())
#isidentifier
print(s1.isidentifier())
print(s4.isidentifier())
#islower
print(s1.islower())
#isnumeric
print(s1.isnumeric())
#isprintable
print(s1.isprintable())
#isspace
print(s1.isspace())
#istitle
print(s2.istitle())
#isupper
print(s4.isupper())
#join
print(s6.join(s7))
#ljust/ #rjust
print(s4.ljust(3), "is my favorite word")
#lower
print(s4.lower())
#lstrip
print("of all words", s4.lstrip(), "is my favorite")
#partition/ #rpartition
print(s1.partition("have"))
#replace
print(s2.replace("bro", "buddy"))
#rfind/ #rindex
print(s2.rfind("o"))
#rsplit/ split
print(s1.rsplit())
#rstrip
print("of all words", s4.rstrip(), "is my favorite")
#splitlines
print(s8.splitlines())
#startswith
print(s3.startswith("my"))
#swapcase
print(s4.swapcase())
print(s1.swapcase())
#title
print(s1.title())
#translate
print(s4.maketrans("A", "O"))
print(s4.translate({65: 79}))
#zfill
print(s5.zfill(5))
















