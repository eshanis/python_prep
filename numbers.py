#complex() function is used to convert a string, int or float value to complex type.
# This method accepts two optional arguments and returns a complex number.

a = "177"
b = 50
c = 140.64

#convert from string to complex using single parameter
print(complex(a))

#convert from int to complex using double parameters
print(complex(b, 5))

#convert from float to complex using double parameters
print(complex(c, 7))

print("==================================")

a = "10"
b = 20.28
c = 21

#convert from string to int
print(int(a))
print(float(a))
#convert from float to int
print(int(b))
#convert from int to float
print(float(c))