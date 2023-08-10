#joining lists and strings.
#iterating through the list and creating a string
a = ', '.join(['foo', 'bar', 'baz', 'qux'])
print(a)

print("========= from string to list=============")
b = list('corge')
print(b)

print("======================")
c = ":".join("corge")
print(c)

print("======== if 23 is not put in as '23' the below will fail since 23 is an int ==============")
d = '---'.join(['foo', '23', 'bar'])
e = '-x-'.join(['foo', str(23), 'bar'])
print(d)
print(e)


print("========== real python ============")

s = 'foo-bar-baz'
a = '-'.join(s.split('-'))
print("a is : " , a)
b = s.strip('-')
print("b is : " , b)
c = s.upper().lower()
print("c is : " , c)
d = '-'.join(s.partition('-'))
print("d is : " , d)
e = s.center(15)
print("e is : ", e)

print("=========== below gives exception error since you cannot combine strings and bytes==============")

x = list((b'abcde' + 'fghi')[3:6])
print(x)

print("======================")


