# STRING TYPE
#1.A string is a sequence of characters enclosed in either single quotes ('') or double quotes (“”). 
 #the Python language provides various built-in methods and functionalities to work with strings efficiently.

pooja='kataru'
print(type(pooja))

devi="rayudu"
print(type(devi))

mahi="""k"""
print(type(mahi))

chandu='silver'
print(type(chandu))

koti="""O"""
print(type(koti))

sub="income tax"
print( type(sub))

group='b.com'
print(type(group))

section= """A section"""
print(type(section))

movie="mla"
print(type(movie))

job='Hr'
print(type(job))

#sciling:-Slicing is the extraction of a part of a string, list, or tuple. 
# It enables users to access the specific range of elements by mentioning their indices.

element="i am devisri"
print(element[6])

element="hello  every one"
print(element[-8])

college="fortune  schoole  of business "
print(college[4:10])

add='kondapur hyderabad  '
print(add[-6])

name='  anusha '
print(name[-6:-4])

course="python full stack  "
print(course[7])

college="fortune  schoole  of business "
print(college[-14:-9])

name='i am   sravani'
print(name[9])

element="hello  every one"
print(element[-10])

ele="hello  all"
print(ele[4])

#concatenation:- String concatenation means add strings together.
#=>in there are a few ways to concatenate or combine strings.
#  The new string that is created is referred to as a string object.

name1="devi"
name2="sri"
con= name1 +" "+name2
print(con)

num1="first"
num2="secound"
con=num1+" "+num2
print(con)

name2="first name"
name5="middle name"
con=name2+" "+name5
print(con)

sub1="bl"
sub2="english"
con=sub1+" "+sub2
print(con)

num1="sec"
num2="a sce"
con=num1+" "+num2
print(con)

#Repetion
#A repetitive statement is notion that allows to execute one or a group of statements at multiple times. 
name="devisri"
print(name*5)

rep="welcome"
print(rep*3)

pooja="kataru"
print(pooja*7)

mahi="k"
print(mahi*7)

month="oct"
print(month*8)

#LENGTH:-The len() function is used to return an integer value which indicates the number of items in an object.

word="place"
print(len(word))

#UPPER:-The toUpperCase() method returns the value of the string converted to uppercase. 

name="devisri"
print(name.upper())

#LOWER:-The to LowerCase() method converts a string to lower case letters.

name="POOJa"
print(name.lower())

#COUNT:-Count() is a built-in function that returns the number of times an object appears in a list,
# It returns the number of times a given value occurs in a string or a list, as the name implies.
name1="i am devisree "
print(name1.count('e'))

#STRIP:-The strip() method removes any leading, and trailing whitespaces. Leading means at the beginning of the string, trailing means at the end.
#  You can specify which character(s) to remove, if not, any whitespaces will be removed.
place=" hyd  "
strp=place.strip()
print(len(strp))

#SPLIT:-Split is used to break a delimited string into substrings.
#  You can use either a character array or a string array to specify zero or more delimiting characters or strings.

intro="i am devisri from hyderabad"

print(intro.split())

#JOIN:-The join() method takes all items in an iterable and joins them into one string.
#  A string must be specified as the separator.
 
name=['i','am','devisri','from','hyd']
print(' '.join(name))

#start with:-startswith() method in Python is a built-in string method that checks whether a given string starts with a specific prefix.

name="pooja"
print(name.startswith("pooja"))

#END WITH:-In  the endswith() function for a String object determines whether the string ends with a specified suffix,
#  and returns True if it does, or False if it does not. 

movie="darling"
print(movie.endswith("darling"))

#REPLACE:- The replace() function returns a copy of the original string with some or all occurrences of a 
# substring replaced with another desired substring.
movie="kalki"
print(movie.replace("kalki","python"))

#3.TUPLE
#it is a collection of elements and it can be represented by useing comas (,)
#it can be immutable

devi=(1,2,3,4,5,6)
print(devi)

#METHODS
#1.COUNT,INDEX

pooja=("a","b","c","d","e","f","g",)
print(pooja.count("f"))

name=("devi","mahi","nandu","sravani")
print(name.index("nandu"))

#string formating
#1.  (.format()method)

name="mahi"
age=24
print("my name is {} and i am {}years old". format(name,age))

movie="bahubali"
date=10
print("movie name is {} and movie release date {}".format(movie,date))

#2. FSTRING:-
name="sravani"
age=20
print(f'my name is {name} and i am {age} year old')

course="python"
duration=6
print(f'i am learning {course} and it is {duration}  months duration')













