"""Introduction to Tuples."""
# t = 'a', 'b', 'c'
#
# print(t)
welcome = ('Welcome to my Nightmare', 'Alice Cooper', 1975)
bad = ('Bad Company', 'Bad Company', 1974)
budgie = ('Nightflight', 'Budgie', 1981)
imelda = ('More Mayhem', 'Emilda May', 2011)
metallica = ('Ride the Lightning', 'Metallica', 1984)

print(metallica)
print(metallica[0])
print(metallica[1])
print(metallica[2])

# The following code causes errors and won't run
# metallica[2] = 1986
# print(metallica)

metallica2 = list(metallica)
metallica2[2] = 1986
print(metallica2)
