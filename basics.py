# exception handling
def d(val):
    try:
        return 3/val
    except Exception as e:
        print(e)
        return None
#d(9)
#d(12)

#================The Multiple Assignment Trick=====================#
## long and repetative ##
cat = ['fat', 'black', 'loud']
size = cat[0]
color = cat[1]
disposition = cat[2]
## short and oneliner ##
cat = ['fat', 'black', 'loud']
size, color, disposition = cat

#================augment asssignment====================#
spam = 'Hello'
spam += ' world!'
print(spam)
#'Hello world!'

bacon = ['Zophie']
bacon *= 3
print(bacon)
#['Zophie', 'Zophie', 'Zophie']

####### methods #######
#====================================
# how to use list.method(parameters)
# index(value) <--- this one is useful -- rather than doing an If statement in for loop could simple get its index
# insert(where-to,what)
# sort(reverse=False)
# append(value)
# remove(value)
#====================================
# List-like Types: Strings and Tuples

name='James Bond'
print('first name',name[0:5])
print('ames' in name)
for i in name:
    print(i)
'''
Mutable and Immutable Data Types
But lists and strings are different in an important way. A list value is a mutable
data type: It can have values added, removed, or changed. However, a string
is immutable: It cannot be changed. Trying to reassign a single character in
a string results in a TypeError error, 
'''
#====================================
'''
The Tuple Data Type
The tuple data type is almost identical to the list data type, except in two
ways. First, tuples are typed with parentheses, ( and ), instead of square
brackets, [ and ]. 
'''
eggs = ('hello', 42, 0.5)
eggs[0]
#'hello'
eggs[1:3]
#(42, 0.5)
len(eggs)
#3

# but like strings they are inmuttable
# Tuples cannot have their values modified, appended, or removed.
'''
Converting Types with the list() and tuple() Functions
tupleList=list(tuple)
listTuple=tuple(list)
The copy Module’s copy() and deepcopy() Functions
import copy
a=[some list]
b=copy.copy(a)
'''

'''You can also split up a single instruction across multiple lines using the \
line continuation character at the end. Think of \ as saying, “This instruction
continues on the next line.” The indentation on the line after a \ line continua-
tion is not significant. For example, the following is valid Python code:
print('Four score and seven ' + \
'years ago...')
These tricks are useful when you want to rearrange long lines of Python
code to be a bit more readable.
'''

#dictionaries
'''
keys()
values()
items() <-- they are tuple of key and value :: (key,value)

The get() Method
It’s tedious to check whether a key exists in a dictionary before accessing
that key’s value. Fortunately, dictionaries have a get() method that takes two
arguments: the key of the value to retrieve and a fallback value to return if
that key does not exist.
---> get() can be used effectively in a flow to avoid `KeyError`

The setdefault() Method
You’ll often have to set a value in a dictionary for a certain key only if that
key does not already have a value

# keeping these dict methods might come handy when working with dicts
'''
#strings
'''
character escaping just like shell

--> string.method()

upper(),lower(),isupper(),islower()

isalpha(),isalnum(),isdecimal(),isspace(),istitle()

startswith(),endswith()

join(),split()

Justifying Text with rjust(), ljust(), and center()

## useful in formatting output

>>> 'Hello'.rjust(20, '*')
'***************Hello'
>>> 'Hello'.ljust(20, '-')
'Hello---------------'
>>> 'Hello'.center(20)
'   Hello   '
>>> 'Hello'.center(20, '=')
'=======Hello========'

'''