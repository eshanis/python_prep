#Python Casting
#Casting is the conversion of a variable data or an object from one data type to another.
# For example, converting from int to string or string to int.
# The str() function is used to convert from any data type such as int type or float type to string type.
x = 10
y = 20.28

#convert from int to string
a = str(x)

#convert from float to string
b = str(y)

print(type(a))
print(type(b))
print(a)
print(b)

print("==========")

x = 10
y = 20.28

#convert from int to string
a = float(x)

#convert from float to string
b = str(y)

print(type(a))
print(a)

print(type(b))
print(b)

print("=================")

x = 0
y = "1"

#convert from int to boolean
a = bool(x)

#convert from string to boolean
b = bool(int(y))
c = bool(y)

print(type(a))
print(type(b))
print(type(c))
print(a)
print(b)
print(c)

print("===============")