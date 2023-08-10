#multiline
a = """To assign a multiline string
to a variable in Python, the
string literals are enclosed
in triple quotes."""

b = '''To assign a multiline string
to a variable in Python, the
string literals are enclosed
in triple quotes.'''

print(a)
print(b)

print("=================================")

print("string length")
a = "Hello World"
print("string length is: " , len(a))

print("=================================")

print("access single character in string")

a = "Hello World"
print(a[1])

print("=================================")
#slice
#string[start index : end index]
print("slice")
a = "Hello World"
print(a[6:11])
print(a[ : ]) #returns the original string
#below returns an empty string
print("empty string: " + a[2:2])

#string[-start index: -end index]
a = "4444 2222 5555 9999"
print(a[-19:-4])

print("=======================")

#Adding an additional : and a third index designates a stride (also called a step),
# which indicates how many characters to jump after retrieving each character in the slice.

#For example, for the string 'foobar', the slice 0:6:2 starts with the first character and
# ends with the last character (the whole string), and every second character is skipped
print("skipping characters when slicing")
s = 'foobar'
print(s[0:6:2]) #prints foa
print(s[0:6:3])
print("====================")
print("more splicing omitting characters")

s = '12345' * 5
print(s)
print(s[::5]) # print from start to end only the 5th character so prints 11111
print(s[4::5]) # starting from 4th character to the end, print the 5th character prints 55555
print(s[5:0:-2]) #prints 142 starting from 5th character up 0th print every 2nd character

print("============================")
print("splicing but reversing the string")
#When you are stepping backward, if the first and second indices are omitted,
# the defaults are reversed in an intuitive way: the first index defaults
# to the end of the string, and the second index defaults to the beginning.

print(s[::-5]) # prints 55555

#below reverses the string
t = 'If Comrade Napoleon says it, it must be right.'
print(t[::-1])

#What is the slice expression that gives every third character of string s,
# starting with the last character and proceeding backward to the first?
s = 'If Comrade Napoleon says it, it must be right.'
print(s[::-3])
#any of the below is correct
#s[::-3]
#s[-1::-3]
#s[:0:-3]
#s[-1:0:-3]

print("================foobar splicing==================")
s = 'foobar'
print(s[::5])
print(s[::-5])
print(s[::-1][::-5])
print(s[::-1][-1] + s[len(s)-1])
print(s[0] + s[-1])


print("=================================")
#concatenate
print("concat using +")
s = "foo"
t = "bar"
u = "fight"
print(s + t + u)

#multiply
print ("multiply string")
print( "s * 4 = " + s * 4)


print("=================================")
#to check if word os present use "in" or "not in" keywords
A = "This is a great world"
b = "great" in A
print(b)

C = "This is a great world"
d = "great" not in C
print(d)

print("=================================")
#format() method
# order_string is an inbuilt method you can call
order_string = "The cost price of this pen is {} and the selling price is {}"
formatted_string = order_string.format(10,15)
print(formatted_string)

x = "Hello I am {} years old and and my sister is {} years old"
y = order_string.format(20,10)
print(y)

print("=================================")
print("fstring")
n = 20
m = 25
prod = n * m
print(f'The product of {n} and {m} is {prod}')

print("=================================")

# to upper() method
a = "hello world"
result = a.upper()
print(result)
print ("===========================")
s = 'foo goo moo'
print("the double oo : " , s.count("oo"))
print("the double oo given start and end : " , s.count("oo", 0, 8))

print("===========================")
#'foo bar foo baz foo qux'.index('grault')


print("=================================")
# chr() Converts an integer to a character
#below prints "Z"
p = chr(90)
print(p)

print("============== lstrip ==================")
#strips white spaces to the left
a = '   foo bar baz   '
print(a.lstrip())

print("============== rstrip ==================")

b = '   foo bar baz   '.rstrip()
print(b)

print("============== strip ==================")

c = 'www.realpython.com'.strip('w.moc')
print(c)

print("========== strip -  ===============")
d = 'foo-bar-fizz'
print(d.strip('-'))

print("=========================")

s = 'foo'
t = 'bar'
print('barf' in 2 * (s + t))


x = ord('a')
print(x)

# ord only works on characters not strings
#below gives TypeError : ord() expected a character, but string of length 3 found
y = ord("foo")
print(y)