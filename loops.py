for l in 'Jhon':
   if l == 'o':
      pass
   print(l, end=", ")

print("======================")

x = 0
a = 5
b = 5
if a > 0:
    if b < 0:
        x = x + 5
    elif a > 5:
        x = x + 4
    else:
        x = x + 3
else:
    x = x + 2
print(x)

print("========================")

for num in range(10, 14):
   for i in range(2, num):
       if num%i == 1:
          print(num)
          break

print("=======================")

for num in range(-2,-5,-1):
    print(num, end=", ")

print("========================")

numbers = [10, 20]
items = ["Chair", "Table"]

for x in numbers:
  for y in items:
    print(x, y)

print("======================")

x = 0
a = 0
b = -5
if a > 0:
    if b < 0:
        x = x + 5
    elif a > 5:
        x = x + 4
    else:
        x = x + 3
else:
    x = x + 2
print(x)

print("===============================")
a, b = 12, 5
if a + b:
    print('True')
else:
  print('False')