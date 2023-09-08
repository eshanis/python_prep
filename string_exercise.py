# https://pynative.com/python-string-exercise/
# 1a
str10 = "James"
# expected out put Jms
print("1: ", str10[::2])

# option2
str1 = 'James'
print("Original String is", str1)
# Get first character
res = str1[0]
print("first character is : ", res)

# Get string size
l = len(str1)
# Get middle index number
mi = int(l / 2)
print("middle index number is: ", mi)
# Get middle character and add it to result
res = res + str1[mi]
print("middle character added to result is: " + res)

# Get last character and add it to result
res = res + str1[l - 1]
print("last character is: " + str1[l - 1])
print("New String:", res)
print("=========================")

# Exercise 1B: Create a string made of the middle three characters
# output Dip and Son
str1 = "JhonDipPeta"
s1 = (str1[4:7])
print("1a: ", s1)

str2 = "JaSonAy"
s2 = str2[2:5]
print("1b: ", s2)


# option 2:
def get_middle_three_chars(str1):
    print("Original String is", str1)

    # first get middle index number
    mi = int(len(str1) / 2)
    print("middle index number: ", mi)

    # use string slicing to get result characters
    res = str1[mi - 1:mi + 2]
    print("Middle three chars are:", res)


get_middle_three_chars("JhonDipPeta")
get_middle_three_chars("JaSonAy")

print("============ 2 =============")

# Exercise 2: Append new string in the middle of a given string
s1 = "Ault"
s2 = "Kelly"
s3 = s1[0:2] + s2 + s1[2:]
print(s3)


# option 2:
def append_middle(s1, s2):
    print("Original Strings are", s1, s2)

    # get middle index number
    mi = int(len(s1) / 2)
    print(mi)
    # get character from 0 to the middle index number from s1
    x = s1[:mi:]
    print(x)
    # concatenate s2 to it
    x = x + s2
    print("concat x is : ", x)
    # append remaining character from s1
    x = x + s1[mi:]
    print("After appending new string in middle:", x)


append_middle("Ault", "Kelly")

print("=========== 3 ==============")

# Exercise 3: Create a new string made of the first, middle, and last characters of each input string
s1 = "America"
s2 = "Japan"
# output AJrpan

s3 = s1[0] + s2[0] + s1[3] + s2[2] + s1[6] + s2[4]
print(s3)


# option2
def append_middle(s1, s2):
    print("Original Strings are", s1, s2)
    # get middle index number
    mi = int(len(s1) / 2)
    mi2 = int(len(s2) / 2)
    # get character from 0 to the middle index number from s1
    x = s1[0] + s2[0]  # appending the two first characaters
    x = x + s1[mi] + s2[mi2]  # now adding the middle to the first
    x = x + s1[6] + s2[4]  # adding the last characters to the above
    print("the new string is:", x)


append_middle("America", "Japan")

print("============== 4 ====================")

# Exercise 4: Arrange string characters such that lowercase letters should come first
str1 = "PyNaTive"
# expected output yaivePNT

s1 = sorted(str1)
print("sorted is: ",s1)  # doesnt work

# option2
print("original string is: ", str1)
lower = []
upper = []
for char in str1:
    if char.islower():
        lower.append(char)
    else:
        upper.append(char)
final = lower + upper  # this is not the expected result
print(final)  # this does not work

# Join both list
sorted_str = ''.join(lower + upper)
print('Result:', sorted_str)

print("=========== 5 ===========")

# Exercise 5: Count all letters, digits, and special symbols from a given string
str1 = "P@#yn26at^&i5ve"
# expected outcome
# Chars = 8
# Digits = 3
# Symbol = 4

print("original string is: ", str1)
chars = []
digits = []
symbols = []
for char in str1:
    if char.isalpha():
        chars.append(char)
    elif char.isdigit():
        digits.append(char)
    else:
        symbols.append(char)
new_string = (chars + digits + symbols)
print(new_string)

print("++++++++++++++++++++++++")


def find_digits_chars_symbols(sample_str):
    char_count = 0
    digit_count = 0
    symbol_count = 0
    for char in sample_str:
        if char.isalpha():
            char_count += 1
        elif char.isdigit():
            digit_count += 1
        # if it is not letter or digit then it is special symbol
        else:
            symbol_count += 1

    print("Chars =", char_count, "Digits =", digit_count, "Symbol =", symbol_count)


sample_str = "P@yn2at&#i5ve"
print("total counts of chars, Digits, and symbols is \n")
find_digits_chars_symbols(sample_str)

print("============= 6 ==================")

# Exercise 6: Create a mixed String using the following rules
s1 = "Abc"
s2 = "Xyz"
# expected output AzbycX

# get string length
s1_length = len(s1)
s2_length = len(s2)

# get length of a bigger string
length = s1_length if s1_length > s2_length else s2_length
result = ""

# reverse s2
s2 = s2[::-1]

# iterate string
# s1 ascending and s2 descending
for i in range(length):
    if i < s1_length:
        result = result + s1[i]
    if i < s2_length:
        result = result + s2[i]

print(result)

print("=========== 7 =============")


# Exercise 7: String characters balance Test
# Write a program to check if two strings are balanced. For example, strings s1 and s2 are
# balanced if all the characters in the s1 are present in s2. The character’s position doesn’t matter.

def string_balance_test(s1, s2):
    flag = True
    for char in s1:
        if char in s2:
            continue
        else:
            flag = False
    return flag


s1 = "Yn"
s2 = "PYnative"

flag = string_balance_test(s1, s2)
print("s1 and s2 are balanced:", flag)

s1 = "Ynf"
s2 = "PYnative"
flag = string_balance_test(s1, s2)
print("s1 and s2 are balanced:", flag)

print("============= 8 =============")

# Exercise 8: Find all occurrences of a substring in a given string by ignoring the case
# Write a program to find all occurrences of “USA” in a given string ignoring the case.

str1 = "Welcome to USA. usa awesome, isn't it?"
# expected outcome: The USA count is: 2

new = str1.lower()
sub_str = "usa"

# use count function
count = new.count(sub_str)
print("The USA count is:", count)

print("============== 9 =============")

# Exercise 9: Calculate the sum and average of the digits present in a string
# Given a string s1, write a program to return the sum and average of the digits
# that appear in the string, ignoring all other characters.

input_str = "PYnative29@#8496"
# Expected Outcome:Sum is: 38 Average is  6.333333333333333
print("original string is : ", input_str)

total = 0
cnt = 0
for char in input_str:
    if char.isdigit():
        total += int(char)
        cnt += 1

# average = sum / count of digits
avg = total / cnt
print("Sum is:", total, "Average is ", avg)

print("=========== 10 =============")

#Exercise 10: Write a program to count occurrences of all characters within a string
str1 = "Apple"
#expected output : {'A': 1, 'p': 2, 'l': 1, 'e': 1}
print("original string is: ", str1)

# create a result dictionary
char_dict = dict()

for char in str1:
    count = str1.count(char)
    # add / update the count of a character
    char_dict[char] = count
print('Result:', char_dict)

print("========= 11 ============")
#Exercise 11: Reverse a given string
str1 = "PYnative"
#expected : evitanYP
print("original string is : ", str1)
str2 = str1[::-1]
print("reversed string is : ", str2)

print("========== 12 ===========")
#Exercise 12: Find the last position of a given substring
#Write a program to find the last position of a substring “Emma” in a given string
str1 = "Emma is a data scientist who knows Python. Emma works at google."
#expected : Last occurrence of Emma starts at index 43
print("original string is: ", str1)

index = str1.rfind("Emma")
print("Last occurrence of Emma starts at index:", index)

print("======== 13 =============")
#Exercise 13: Split a string on hyphens
#Write a program to split a given string on hyphens and display each substring.

str1 = "Emma-is-a-data-scientist"
#expected output: Displaying each substring

#Emma
#is
#a
#data
#scientist

x = str1.split("-")
print("splitting in hyphen: ", x)
print("Displaying each substring")
for sub in x:
    print(sub)

print("======== 14 =============")
#Exercise 14: Remove empty strings from a list of strings
str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
print("original string is: " , str_list)

#expected output After removing empty strings
#['Emma', 'Jon', 'Kelly', 'Eric']

str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
res_list = []
for s in str_list:
    # check for non empty string
    if s:
        res_list.append(s)
print(res_list)

print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]

# use built-in function filter to filter empty value
new_str_list = list(filter(None, str_list))

print("After removing empty strings")
print(new_str_list)

print("===============  15 ====================")
#Exercise 15: Remove special symbols / punctuation from a string
str1 = "/*Jon is @developer & musician"
#expected output: "Jon is developer musician"

import string

str1 = "/*Jon is @developer & musician"
print("Original string is ", str1)

new_str = str1.translate(str.maketrans('', '', string.punctuation))
print(string.punctuation)
print("New string is ", new_str)

print("++++++++++++++++++++++++++++++++++++++")

import re

str1 = "/*Jon is @developer & musician"
print("Original string is ", str1)

# replace special symbols with ''
res = re.sub(r'[^\w\s]', '', str1)
print("New string is ", res)

print("==============  16  ==============")

#Exercise 16: Removal all characters from a string except integers
str11 = 'I am 25 years and 10 months old'
#expected output : 2510

print("Original string is ", str11)
digit = []
for char in str11:
    print(char)
    if char.isdigit():
        print("digit found")
        digit.append(char)
print("new string is: ", "".join(digit)) # to convert list to a string


print("+++++++++++++++++++++++")

str1 = 'I am 25 years and 10 months old'
print("Original string is", str1)

# Retain Numbers in String
# Using list comprehension + join() + isdigit()
res = "".join([item for item in str1 if item.isdigit()])

print(res)

print("========  17  =============")
#Exercise 17: Find words with both alphabets and numbers
#Write a program to find words with both alphabets and numbers from an input string.

#expected outcome: Emma25
#                  scientist50

str1 = "Emma25 is Data scientist50 and AI Expert"
print("The original string is : " + str1)

res = []
# split string on whitespace
temp = str1.split()

# Words with both alphabets and numbers
# isdigit() for numbers + isalpha() for alphabets
# use any() to check each character

for item in temp:
    if any(char.isalpha() for char in item) and any(char.isdigit() for char in item):
        res.append(item)

print("Displaying words with alphabets and numbers")
for i in res:
    print(i)

print("========  18  =============")
#xercise 18: Replace each special symbol with # in the following string
str1 = '/*Jon is @developer & musician!!'
#expected: ##Jon is #developer # musician##
import string

str1 = '/*Jon is @developer & musician!!'
print("The original string is : ", str1)

# Replace punctuations with #
replace_char = '#'

# string.punctuation to get the list of all special symbols
for char in string.punctuation:
    str1 = str1.replace(char, replace_char)

print("The strings after replacement : ", str1)

print("========  end :)  =============")

