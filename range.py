x = 0
for i in range(10): # from 0-9 so 10 numbers
  for j in range(-1, -10, -1): # from -1 to -9 so 9 numbers
    x += 1
    print(x) # answer is 90 (10 x 9 = 90)


print("=============================")

var = 10
for i in range(10):
    for j in range(2, 10, 1):
        if var % 2 == 0:
            continue
            var += 1
    var+=1
else:
    var+=1
print(var)

print("================================")
for num in range(2,-5,-1):
    print(num, end=", ")