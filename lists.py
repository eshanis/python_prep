#lists
#List is an ordered collection of data or elements which are mutable
# and placed within the square brackets.
fruits = ["mango", "grapes", "guava", "apple", "watermelon"]
print(fruits)

print("===============")
#access item list

fruits = ["mango", "grapes", "guava", "apple", "watermelon"]
print("Item at index 0 = "+ fruits[0])
print("Item at index 1 = "+ fruits[1])
print("Item at index 2 = "+ fruits[2])
print("===============")

#accessing items with -ve index

names = ["Joe", "Danny", "Tom", "Ronie", "Victory", "Kelly", "Peter"]
print("Item at negative index -1 = " + names[-1])
print("Item at negative index -2 = " + names[-2])
print("Item at negative index -3 = " + names[-3])

print("===============")
#accessing items using range
colors = ["blue", "white", "red", "green", "orange", "purple", "brown"]
print(colors[0:3])
print(colors[4:]) # no end index specified to it goes ot the end of the list

print("===============")

#looping through lists
colors = ["blue", "white", "red", "green", "orange", "purple", "brown"]
for i in colors:
   print(i)


print("===============")

#list length
print(len(colors))

print("===============")
#looping using range
colors = ["blue", "white", "red", "green", "orange", "purple", "brown"]
for i in range(len(colors)):
   print(colors[i])


print("===============")
#add items tolist using append() function

nums = [12, 33, 45, 77, 23]
nums.append(100)
print(nums)

print("===============")

#insert using insert() function
#Syntax
#insert(index, item)

nums.insert(2,55)
print(nums)

print("===============")

#add multiple items to list using extend() function
nums = [10, 20, 30, 40, 50]
nums.extend([60, 70, 80, 90, 100])
print(nums)

print("===============")

#remove() function to remove item from list
fruits = ["apple", "mango", "carrot", "grapes", "orange"]
fruits.remove("carrot")
print(fruits)

print("===============")
#pop item using the index number
#if index number not specified last item is popped
fruits = ["apple", "mango", "carrot", "grapes", "orange"]
fruits.pop(2)
print(fruits)
fruits.pop()
print(fruits)

print("===============")
#find max number
#find min number

nums = [20,77,33,45,10,40,56]
max_num = max(nums)
print("max number is : ", max_num)

min_num = min(nums)
print("min number is : " , min_num)

print("======= joining two lists ========")

#join two lists using extend() function
list1 = [2,3,4,5]
list2 = [6, 7, 8, 9, 10]
list1.extend(list2)
print("extended list is : " , list1)

#join two lists using "+"
list1 = [2,3,4,5]
list2 = [6, 7, 8, 9, 10]
total = list1 + list2
print("total is : ", total)

#join using append()

list1 = [2,3,4,5]
list2 = [6, 7, 8, 9, 10]
for i in list2:
	list1.append(i)
print("iterated list is : ", list1)

print("=======making copies of list ========")
#copy lists using copy() and list() functions

fruits = ["apple", "mango", "banana"]
new_fruits = fruits.copy()
print(new_fruits)

fruits = ["apple", "mango", "banana"]
new_fruits = list(fruits)
print(new_fruits)


print("===============")

#list() Constructor
#In Python, you can use the list() constructor to create a new list.

colors = list(("black", "white", "pink", "blue"))
print(colors)

print("===============")

#check if item exists in list
colors = ["green", "blue", "green", "white"]
if "blue" in colors:
    print("blue Exists")


print("=======joining convert list to string ========")
colors = ["green", "blue", "green", "white", "red"]
print(":".join(colors))