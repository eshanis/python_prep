print("enter a number: ")
n = int(input())

for i in range (1, n+1):
 print(i,end='') # end is to convert to string

print("=====================")

print("enter a number: ")
n = int(input().strip())
if n % 2 != 0:
	print("Weird")
elif (n % 2 == 0) and n in range(2,6):
	print("Not Weird")
elif (n % 2 == 0) and n in range(6,21):
	print("Weird")
elif (n % 2 == 0) and n > 20:
	print("Not Weird")

print("=======================")

print("enter a number for square root: ")
n = int(input())
for i in range(0,n):
	print(i ** 2,",")

print("========================")
print("enter x: ")
x = int(input())
print("enter y: ")
y = int(input())
print("enter z: ")
z = int(input())
print("enter n: ")
n = int(input())
for i in range(x+1):
	for j in range(y+1):
		for k in range(z+1):
			if (i+j+k != n):
				print(i)



