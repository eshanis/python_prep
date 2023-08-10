#Set is an unordered and unindexed collection of values or elements
# which do not allow duplicate values and are placed within the curly braces.

names = {"Jonny", "Danny", "Kelly", "Jane"}
for i in names:
    print(i)

print("========add names  ======")
names = {"Jonny", "Danny", "Kelly", "Jane"}
names.add("Peter")
print(names)
names.add("Danny") # not added since it is duplicate
print(names)

print("=== update ==========")
fruits = {"apple", "banana", "mango", "grapes"}
fruits.update({"watermelon", "guava", "cherry"})
print(fruits)

print("=== set constructor ==========")
foods = (("bread", "butter", "milk", "egg"))
print(foods)

print("=== length ==========")
foods = (("bread", "butter", "milk", "egg"))
print(len(foods))


print("=== remove ==========")
foods = {"bread", "butter", "milk", "egg"}
foods.remove("butter")
print(foods)


print("=== discard ==========")

foods = {"bread", "butter", "milk", "egg"}
foods.discard("milk")
print(foods)



print("=== clear removes items from the set ==========")

foods = {"bread", "butter", "milk", "egg"}
foods.clear()
print(foods)

print("=== join using union() and update() ==========")
set1 = {"bread", "butter", "milk", "egg"}
set2 = {"fish", "meat"}
set3 = set1.union(set2)
print("union method: ", set3)

set1 = {"bread", "butter", "milk", "egg"}
set2 = {"fish", "meat"}
set1.update(set2)
print("update method: ", set1)


print("=== if exists ==========")

foods = {"bread", "butter", "milk", "egg"}
if "butter" in foods:
    print("butter exist")


print("=== delete : gives error food is not defined==========")
foods = {"bread", "butter", "milk", "egg"}
del foods