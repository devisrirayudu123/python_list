## ADVANCE DATA TYPES

#1.LIST:- it is collection of data
#=>list is a mutable 
#=> list can be represent by using[,]
#A list is a collection of items that are ordered and can be 
# defined in different ways depending on the programming language and context. 

#int
a=[1,2,3,4,5]
print(a)

#char-string
b=['devisri','rayudu']
print(b)

#float
c=[1.2,3.4]
print(c)

#mixed types
mix=[1,7,3.4,True,34j,'devi']
print(mix)

rollno=[1,2,5,4]
print(rollno)

multiple=['devi', 3,8.07,5j,5>6]
print(multiple)

#TWO TYPES OF INDEX
#=>POSITIVE INDEX:- Python uses a string index to retrieve a specific character from a string using the syntax string[n] . All strings use zero-based indexing.
#  Positive indexing increments the index from zero to infinity  from left to right.

devi=['devi',23,'hyd',575.86,7>6]
print(devi[0])

pooja=['pooja',22,'madhapur',475765.7,98<67]
print(pooja[2])

tiru=['tiru',24,'kondapur',97765.7,34<67,]
print(tiru[4])

mahi=['mahi',30,'madhapur',67497765.7,98<67+9>4]
print(mahi[3])


marks=['name',22,'b.com',8.0,10<67]
print(marks[1])

priya=['sri',45,'bgl',]
print(priya[2])

chandu=['mba',24,756.87,7>7]
print(chandu[1])

nandu=['it',87<98,'vjd',45]
print(nandu[3])

course=['b.com',12,'computers',56>75+6<8]
print(course[3])

exam=['income tax',23,564.87,]
print(exam[0])

#=>NEGITIVE INDEX:- (-1 to -infinity) from right to left
# the whole numbers lesser than 0 are referred to as negitive index



marks=['exam',45,9875.876,7<8]
print(marks[-2])

college=['cmr',45,76875.876,7>8,'hyd']
print(college[-5])

trip=['araku',45,24587.657,'location',10<8]
print(trip[-4])

score=['exam',100,9.87,7<8]
print(score[-2])

age=['name',45,76875.876,7>8,'hyd']
print(age[-5])

faculty=['sravani',25,245.6,'sub-bl',7<8]
print(faculty[-4])

a=['anu',24,65876.86,'hyd']
print(a[-3])

num1=['laxmi',45,45>76]
print(num1[-2])

hyd=['location',23,56.76>67.98,'devi']
print(hyd[-3])

score=['exam',100,9.87,7<8]
print(score[-2])


#SLICER:-Slicing is the extraction of a part of a string, list, or tuple. 
# It enables users to access the specific range of elements by mentioning their indices. 
#its take starting index: ending index

name=[1,'devi','b.com',8.7,56>897]
print(name[2:4])

name=[2,'pooja','b.com',9.01,56<897,'kataru']
print(name[2:5])

name=[3,45.456,45>466,'tiru','majjiga']
print(name[1:4])

name=[4,87567.8969,'mahi',87<45]
print(name[-2:4])

num=[1,2,3,4,5,6,7,8]
print(num[-5:-3])

details=['devi',7487476,875.876,'kondapur',87>78,4]
print(details[-7:-4])

movie=['name',2,87577.5667,5.87,'place']
print(movie[-4:-3])

detailslocation='hyd'
print(detailslocation)

movie2=5
print(movie2)

namelast='Rayudu'
print(namelast)



#ALL METHODS
#1.append():-it will add single element at end to list
#it is a  a pre-defined method used to add a single item to certain collection types. Without the append method,
#  developers would have to alter the entire collection's code for adding a single value or item

num=['devi','pooja','chandu','sri']
num.append('ayesha')
print(num)

#2.EXTEND:- it will add more then two
# extend() method is used to add items from one list to the end of another list.
#  This method modifies the original list by appending all items from the given iterable.

name=[34,65,76,98]
name1=[45,12,32,5]
name.extend(name1)
print(name)


#3 POP():- it will remove the last element
# it is a pre-defined, in-built function that removes an item at the specified index from the list.


name=[34,65,76,98]
name1=[45,12,32,5]
name.pop()
print(name)

#4.LENGTH():-it will give lenght of list

num=['devi','pooja','chandu','sri']
num1=['ayesha','mahi']
print(len(num))

#4.count:-it is frequance of particular element
# it is a built-in function that returns the number of elements (lenth)in an iterator/object passed to the function.

total=[1,3,5,7,86,6,34,2,5,5]
total1=[9,10,76]
print(total.count(5))


#5.INDEX:-it will give value of a index
#Index method involves multiplying an original construction cost by 
# a multiplier that is reached based on the margin of increase in construction costs since a property was built.

#WHY:-As discussed earlier, the index() in Python returns the position of the element in the specified list or the characters in the string.






