#DICTIONARY:-It is a sequence of key-value pairs separated by commas and surrounded by curly braces. 
#=>it is a multable
#=>it is a usefull for mapping and it will represented by {} curly braces, and fact value is sepereted by (,)

name={"name":"manisha","age":25,"location":"hyd","education":"inter"}
print(type(name))

name={"name":"manisha","age":25,"location":"hyd","education":"inter"}
print(name["age"])

details={"name":"pooja","age":21,"location":"madhapur","salary":10000}
print(type(details))

#Dictionary methods
#1.key():-The keys() method returns a view object. The view object contains the keys of the dictionary, as a list.
course={"name":"python","duration":6,"fees":30000,"location":"hitech city"}
print(course.keys())

course={"name":"python","duration":6,"fees":30000,"location":"hitech city"}
print(course.values())

#2.ITEMS:-The items () method in the dictionary is used to return each item in a dictionary as tuples in a list.

selfintro={"name":"devisri","education":"degree","marks":8.7,"passedout":24}
print(selfintro.items())

#3.pop:-its remove the last item
# The pop method is used to remove an item at the specified position in a list or dictionary and return it.
course={"name":"python","duration":6,"fees":30000,"location":"hitech city"}
print(course.pop("fees"))
print(course)

#4.GET():-it is used retrie the specific key

selfintro={"name":"devisri","education":"degree","marks":8.7,"passedout":24}
print(selfintro.get("nae","not found"))

#5.clear():- it is clean the entair the dictionary


education={"name":"b.com","duration":"three years","fees":150000,"location":"hitech city"}
print(education.clear())

#UPDATE:-update() method updates the current set by adding items from another iterable, such as a set, list, tuple, or dictionary. 
education={"name":"b.com","duration":"three years","fees":150000,"location":"hitech city"}
education1={"name":"BBA","duration":"three years","fees":200000,"location":"madhapur"}
print(education.update(education1))
print(education1)










