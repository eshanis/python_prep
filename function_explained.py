# Python program to illustrate functions
# can be treated as objects

print("Example 1: Treating the functions as objects.")
def shout(text):
	return text.upper()


print(shout('Hello'))

yell = shout

print(yell('Hello'))

print("=============================")


print("Example 2: Passing the function as an argument")

# Python program to illustrate functions
# can be passed as arguments to other functions
def shout(text):
	return text.upper()


def whisper(text):
	return text.lower()


def greet(func):
	# storing the function in a variable
	greeting = func("""Hi, I am created by a function passed as an argument.""")
	print(greeting)


greet(shout)
greet(whisper)

print("===================================")

print("Example 3: Returning functions from another function.")

# Python program to illustrate functions
# Functions can return another function

def create_adder(x):
	def adder(y):
		return x+y

	return adder

add_15 = create_adder(15)

print(add_15(10))

print("==============================")

# decorator
# defining a decorator
def hello_decorator(func):
	# inner1 is a Wrapper function in
	# which the argument is called

	# inner function can access the outer local
	# functions like in this case "func"
	def inner1():
		print("Hello, this is before function execution")

		# calling the actual function now
		# inside the wrapper function.
		func()

		print("This is after function execution")

	return inner1


# defining a function, to be called inside wrapper
def function_to_be_used():
	print("This is inside the function !!")


# passing 'function_to_be_used' inside the
# decorator to control its behaviour
function_to_be_used = hello_decorator(function_to_be_used)

# calling the function
function_to_be_used()

print("===========================================")
print("  ")
print("DECORATOR EXAMPLE 1")
#find out the execution time of a function using a decorator.
# importing libraries
import time
import math


# decorator to calculate duration
# taken by any function.
def calculate_time(func):
	# added arguments inside the inner1,
	# if function takes any arguments,
	# can be added like this.
	def inner1(*args, **kwargs):
		# storing time before function execution
		begin = time.time()

		func(*args, **kwargs)

		# storing time after function execution
		end = time.time()
		print("Total time taken in : ", func.__name__, end - begin)

	return inner1


# this can be added to any function present,
# in this case to calculate a factorial
@calculate_time
def factorial(num):
	# sleep 2 seconds because it takes very less time
	# so that you can see the actual difference
	time.sleep(2)
	print(math.factorial(num))


# calling the function.
factorial(10)
print("==================================")

print("DECORATOR EXAMPLE 2: returning")
#What if a function returns something or an argument is
# #passed to the function?
#In all the above examples the functions didn’t return
# #anything so there wasn’t an issue, but one may need the #returned value.

def hello_decorator(func):
	def inner1(*args, **kwargs):
		print("before Execution")

		# getting the returned value
		returned_value = func(*args, **kwargs)
		print("after Execution")

		# returning the value to the original frame
		return returned_value

	return inner1


# adding decorator to the function
@hello_decorator
def sum_two_numbers(a, b):
	print("Inside the function")
	return a + b


a, b = 1, 2

# getting the value through return of the function
print("Sum =", sum_two_numbers(a, b))

print("==========================")

print("DECORATOR EXAMPLE3:Chaining Decorators")

#In simpler terms chaining decorators means decorating a function with multiple decorators.

# code for testing decorator chaining
def decor1(func):
	def inner():
		x = func()
		return x * x
	return inner

def decor(func):
	def inner():
		x = func()
		return 2 * x
	return inner

@decor1
@decor
def num():
	return 10

@decor
@decor1
def num2():
	return 10

print(num())
print(num2())

print("=====================================")

