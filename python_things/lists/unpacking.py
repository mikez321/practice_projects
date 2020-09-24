"""Unpacking Tuples."""
a = b = c = d = e = f = 42
print(c)

x, y, z = 1, 2, 72
print(x)
print(y)
print(z)
# Interestingly enough, this is a tuple.  Below we'll write it differently

print("Unpacking a tuple")

data = (1, 2, 72)
x, y, z = data
print(x)
print(y)
print(z)

# And you can 'unpack' anything!

print("Unpacking a list")

data_list = [12, 13, 69]
p, q, r = data_list
print(p)
print(q)
print(r)
