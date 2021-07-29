'''Tuples Operation'''

#Creating an empty Tuple
Tuple1 = ()
print("empty Tuple: ")
print (Tuple1)
 
#Creating a Tuple with the use of string
Tuple1 = ('Pune', 'Maharashtra')
print("\nTuple with the use of String: ")
print(Tuple1)
 
# Creating a Tuple with the use of list
list1 = [1, 2, 4, 5, 6]
print("\nTuple using List: ")
print(tuple(list1))
 
#Creating a Tuple with the use of built-in function
Tuple1 = tuple('Pune')
print("\nTuple with the use of function: ")
print(Tuple1)

#Creating a Tuple with Mixed Datatype
Tuple1 = (5, 'Pune', 7, 'Maharashtra')
print("\nTuple with Mixed Datatypes: ")
print(Tuple1)

#Creating a Tuple with nested tuples
Tuple1 = (0, 1, 2, 3)
Tuple2 = ('python', 'Django')
Tuple3 = (Tuple1, Tuple2)
print("\nTuple with nested tuples: ")
print(Tuple3)

#Creating a Tuple with repetition
Tuple1 = ('Pune',) * 3
print("\nTuple with repetition: ")
print(Tuple1)

#Accessing Tuple with Index
Tuple1 = tuple("Pune")
print("\nFirst element of Tuple: ")
print(Tuple1[1])
 
 
#Tuple unpacking
Tuple1 = ("Pune", "Mumbai", "Nashik")
 
a, b, c = Tuple1
print("\nValues after unpacking: ")
print(a)
print(b)
print(c)

# Slicing of a Tuple
Tuple1 = tuple('MMAHARASHTRA')

# Removing First element
print("Removal of First Element: ")
print(Tuple1[1:])

# Reversing the Tuple
print("\nTuple after sequence of Element is reversed: ")
print(Tuple1[::-1])

# Printing elements of a Range
print("\nPrinting elements between Range 4-9: ")
print(Tuple1[4:9])

# Deleting a Tuple
 
Tuple1 = (0, 1, 2, 3, 4)
del Tuple1

def Remove(tuples):
    empty_tuples = [t for t in tuples if t]
    return empty_tuples
  
# Driver Code
tuples = [(), ('Pune','Mharashtra','1000000'), (), ('Mumbai', 'Maharashtra','10000000'), 
          ('Nashik', 'Mharashtra', '100000'), ('',''),()]
print(Remove(tuples))

print(id(tuples))

# Python code to demonstrate namedtuple() 
      
from collections import namedtuple 
      
# Declaring namedtuple()  
Emp = namedtuple('Neova',['name','age','DOB'])  
      
# Adding values  
E = Emp('ABC','19','2541997')  
      
# Access using index  
print ("The emp age using index is : ",end ="")  
print (E[1])  
      
# Access using name   
print ("The emp name using keyname is : ",end ="")  
print (E.name)

