#Tuple is an ordered collection of data or elements which are immutable
# and placed within the round brackets.

fruits = ("mango", "grapes", "guava", "apple", "watermelon")
print("fruit tuple is : ", fruits)

print(" ------accessing items using index number =========")
fruits = ("mango", "grapes", "guava", "apple", "watermelon")
print(fruits[2])

print(" ------accessing items using -ve index number =========")
fruits = ("mango", "grapes", "guava", "apple", "watermelon")
print("Item at index -1 is " + fruits[-1])
print("Item at index -2 is " +fruits[-2])
print("Item at index -3 is " +fruits[-3])

print("========accessing tuple using range and iteration======")
fruits = ("mango", "grapes", "guava", "apple", "watermelon")

print("using range from 1-3: ", fruits[1:3])
print()

print("using negative index range: ", fruits[-3:-1])


for i in fruits:
	print("looping through the tuple: ", i)


for i in range(len(fruits)):
	print("using length of tuple: ", fruits[i])

print("============= check if item exists =======================")

if "apple" in fruits:
	print("apple exists")



print("==== adding tuples together =========")
fruits = ("mango", "grapes", "guava", "apple", "watermelon")
colors = ("white", "green", "yellow", "blue", "red")
tuples = fruits + colors
print(tuples)

print("=====cannot add or delete items, below shows error since tuples are immutable =======================")
fruits = ("mango", "grapes", "guava", "apple", "watermelon")
fruits[2] = "banana"
print("fruits added : ", fruits)