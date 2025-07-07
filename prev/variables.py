#variables that are use as containers for storing data values
first_name = "rachel"
Second_name = "kobe"
age = 20
gender= "female"


print(first_name, Second_name, age, gender )

#----------CASTING-------------------
# for specify or define the data types of variable can be done with casting
a = int(7)
b = str(10)
c = float(1)
print( a,b,c )

#----------Get The Types--------------
a = 7
b = 'ram'
print( type(a),type(b) )

#----------Single or Double Quotes?----
a = 'ram'
a = "shyam" 
#no difference

#----------Case-Sensitive---------------
#variable names are case-sensitive.
a=2
A = 'ram'
# A and a is different

#variable Names that are legal to use
myvar = "ram"
my_var = "ram"
_my_var = "ram"
myVar = "ram"
MYVAR = "ram"
myvar2 = "ram"
#illegal variable names
    # 2myvar = "John"
    # my-var = "John"
    # my var = "John"

#Many Values to Multiple Variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#One Value to Multiple Variables
x = y = z = "Orange"
print(x)
print(y)
print(z)

#Unpack a Collection like list, tuple and etc.
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#