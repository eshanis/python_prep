# print("enter x: ")
# x = int(input())
# print("enter y: ")
# y = int(input())
# print("enter z: ")
# z = int(input())
# print("enter n: ")
# n = int(input())
#
# print(list([i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1)  if i+j+k !=n))

# for i in range(x+1):
# 	print(i)
# for j in range(y+1):
# 	print(j)
# for k in range(z+1):
# 	print(k)
# 	if (i+j+k != n):
# 		print(i,j,k)

print("===========================")

#find second highest score

# Steps Used in solving the problem -
# Step 1: First n will take an integer type input of n scores.
# Step 2: then, arr will make a list of these n scores.
# Step 3: After this, we converted our list to set so, it will not store multiple same integers.
# Step 4: then, I sorted my list of scores.
# Step 5: In the last step I printed the second-last integer of my list. And, it is the runner-up score.

print("enter one integer:")
n = int(input())  # not needed
print("enter integers separated by space: ")
arr = list(map(int, input().split()))
arr1 = set(arr)
arr2 = sorted(arr1)
print(arr2[-2])

print("======================")



