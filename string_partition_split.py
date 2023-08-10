#partitions

a = 'foo.bar'.partition('.')
print(a)

b = 'foo@@bar@@baz'
print(b.partition("@@"))

#If <sep> is not found in s, the returned tuple contains s followed by two empty strings:
c = 'foo.bar'.partition('@@')
print(c)

#split ar right partition
d = 'foo@@bar@@baz'
print(d.rpartition("@@"))

print("xxxxxxxxxxxxxxx SPLIT  xxxxxxxxxxxxxxxxx")

# Splits a string into a list of substrings

e = 'foo bar baz qux'.rsplit()
print(e)

f = 'fooo\n\tbarr   bazz\r\fquxx'
print(f.rsplit())

g = 'ffoo.bbar.bbaz.qqux'
print(g.rsplit("."))

h = 'www.realpython.com'
print(h.rsplit('.', maxsplit=1))

i = 'www.realpython.com'
print(i.rsplit('.'))

print("========= split same as r split but counted from left======")
j = 'www.realpython.com'
print(j.split('.', maxsplit=1))

print("=====If <maxsplit> is not specified, .split() and .rsplit() are indistinguishable.=====")

k = 'www.realpython.com'
print(k.split('.'))

