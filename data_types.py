a = "Hello World!"
print(a, " is of type ", type(a).__name__)
print(a, " is of type ", type(a))

a = 100
print(a, " is of type ", type(a).__name__)

a = 100.34
print(a, " is of type ", type(a).__name__)

a = 100j
print(a, " is of type ", type(a).__name__)

a = [10, 45, 23, 78, 19, 20, 14]
print(a, " is of type ", type(a).__name__)

a = (100, 503, 45)
print(a, " is of type ", type(a).__name__)

a = {"name":"Danny", "age": 27}
print(a, " is of type ", type(a).__name__)

a = {"apple", "grapes", "mango"}
print(a, " is of type ", type(a).__name__)

a = frozenset({56, 22, 17})
print(a, " is of type ", type(a).__name__)

a = b"Hello world!"
print(a, " is of type ", type(a).__name__)

a = bytearray("Hello world!", "utf-8")
print(a, " is of type ", type(a).__name__)

a = memoryview(bytes("Hello world!", "utf-8"))
print(a, " is of type ", type(a).__name__)

a = True
print(a, " is of type ", type(a).__name__)

a = range(10)
print(a, " is of type ", type(a).__name__)

a = bytearray("Hello world!", "utf-8")
print(a, "is of the type ", type(a).__name__)

a = bytes("Hello world!", "utf-8")
print(a, "is of the type ", type(a).__name__)

print("========================================================")
print("below is strings")
a = "Hello World"
print("length of string is : " + len(a))

a = "Hello World"
print(a[1])

a = "Hello World"
print(a[6:11])