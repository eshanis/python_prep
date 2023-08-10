#Dictionary in Python is a collection of data with key-value pairs
# which are unordered, unindexed and mutable. This type allows no duplicate keys.

user = {
"first_name":"Danny",
"last_name":"Brown",
"email":"danny@tutorialsbuddy.com"
}
print(user)
print("keys are : ", user.keys())
print("values are: ", user.values())
print("item values are: ", user.items())
for first, last in user.items():
    print(f"info is {first} {last}")

print("=========== access using get() method ====================")
#The get() method takes a key as an argument and returns the value which is associated with that key.

user = {
"first_name":"Danny",
"last_name":"Brown",
"email":"danny@tutorialsbuddy.com"
}

first_name = user.get("first_name")
last_name = user.get("last_name")
email = user.get("email")

print(first_name)
print(last_name)
print(email)



print("============= using square brackets ==================")
user = {
"first_name":"Danny",
"last_name":"Brown",
"email":"danny@tutorialsbuddy.com"
}

first_name = user["first_name"]
last_name = user["last_name"]
email = user["email"]

print(first_name)
print(last_name)
print(email)


print("=============chekc if hey exists ==================")
user = {
"first_name":"Danny",
"last_name":"Brown",
"email":"danny@tutorialsbuddy.com"
}

if "email" in user:
    print("Email Key Exists")

print("======= to add item to dictionary ========================")

user = {
"first_name":"Danny",
"last_name":"Brown",
"email":"danny@tutorialsbuddy.com"
}

user["course"] = "Computer"
print(user)

print("===========pop item ====================")
user = {
"first_name":"Danny",
"last_name":"Brown",
"email":"danny@tutorialsbuddy.com"
}

user.pop("last_name")
print(user)

print("======== delete =======================")
user = {
"first_name":"Danny",
"last_name":"Brown",
"email":"danny@tutorialsbuddy.com"
}

del user["email"]
print(user)

print("=========== length ====================")
user = {
"first_name":"Danny",
"last_name":"Brown",
"email":"danny@tutorialsbuddy.com"
}
print(len(user))


print("============== clear =================")
user = {
"first_name":"Danny",
"last_name":"Brown",
"email":"danny@tutorialsbuddy.com"
}
user.clear()
print(user)


print("============= copy ==================")

dict1 = {"name" : "Peter", "email" : "peter@tb.com", "customer_id" : "ABC123"}
dict2 = dict1.copy()
print(dict2)

print("=========== constructor ====================")
customer = dict(name = "Peter", email = "peter@tb.com", customer_id = "ABC123")
print(customer)

print("=========== nested dictionary ====================")
dict1 = {
"nested_dict1" : {
    "name" : "Peter",
    "email" : "peter@tb.com",
    "customer_id" : "ABC123"
    },
"nested_dict2" : {
    "name" : "Danny",
    "email" : "danny@tb.com",
    "customer_id" : "ABC545"
    }
}

print(dict1)

print("======== dict comprehension ========")

squares = {x : x * x for x in range(6)}
print(squares)


ranks = [("Picard", "Captain"), ("Riker", "Commander"),("Worf", "Lietenent")]
rank_dict = {name:rank for name,rank in ranks}
print(rank_dict)